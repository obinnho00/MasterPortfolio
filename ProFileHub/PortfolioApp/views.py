import os
import re
import sys
import json
import base64
import requests
import markdown2

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.urls import reverse
from django.db import connection

from django.utils.text import slugify
from django.utils import timezone
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from PortfolioApp.gitconfig.gitconfig import GITHUB_API_URL, USERNAME, TOKEN

from .models import AboutMe, Project, TechnicalSkill, User, BugReport, Comment, CV
from .forms import CommentForm
from google.cloud import storage
from datetime import timedelta, datetime


class Home(View):
    def get(self, request):
        return render(request, 'home.html')
    

class Introduction(View):

    def get(self, request):
        """
        Handle GET request to fetch data and render the template.
        """
      
        query = "SELECT id, introduction FROM about_me"
        with connection.cursor() as cursor:
            cursor.execute(query)
            content = cursor.fetchall()  
        return render(request, 'intro.html', {'content': content})
    


class ProjectView(View):

    def get_public_repos(self):
        url = f"{GITHUB_API_URL}/users/{USERNAME}/repos"
        headers = {"Authorization": f"token {TOKEN}"}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_latest_commit(self, repo_name):
        url = f"{GITHUB_API_URL}/repos/{USERNAME}/{repo_name}/commits"
        headers = {"Authorization": f"token {TOKEN}"}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            commits = response.json()
            if commits:
                latest_commit = commits[0]
                return {
                    "sha": latest_commit.get("sha"),
                    "author": latest_commit["commit"]["author"]["name"],
                    "message": latest_commit["commit"]["message"],
                    "date": latest_commit["commit"]["author"]["date"],
                    "url": latest_commit["html_url"],
                }
            return {"error": "No commits found"}
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_readme(self, repo_name):
        url = f"{GITHUB_API_URL}/repos/{USERNAME}/{repo_name}/readme"
        headers = {"Authorization": f"token {TOKEN}"}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            readme_data = response.json()
            if "content" in readme_data:
                return base64.b64decode(readme_data["content"]).decode("utf-8")
            return "No README.md found"
        except Exception as e:
            return {"error": str(e)}
        


class CurrentProjectView(ProjectView):
    def get(self, request, *args, **kwargs):
        # Fetch public repositories
        repos = self.get_public_repos()
        if "error" in repos:
            return HttpResponse(repos["error"], status=500)

        results = []
        for repo in repos:
            repo_name = repo["name"]
            latest_commit = self.get_latest_commit(repo_name)
            readme_content = self.get_readme(repo_name)

            # Always use the default image
            image_url = "images/default.png"

            # Extract the Overview section from the README
            overview = "No Overview available"  # Default message
            if readme_content:
                # Search for the "Overview" section
                match = re.search(r"#\s*Overview(.*?)(?=\n#|\Z)", readme_content, re.S)
                if match:
                    overview = match.group(1).strip()

                # Convert the extracted Overview markdown to HTML
                overview_html = markdown2.markdown(overview)
            else:
                overview_html = "<p>No Overview available</p>"

            # Append the repository details
            results.append({
                "repo_name": repo_name,
                "latest_commit": latest_commit,
                "readme": overview_html,  # Use Overview instead of full README
                "image_url": image_url,
            })

        # Sort results by commit_date in descending order
        results.sort(key=lambda x: x["latest_commit"].get("date"), reverse=True)

        # Render the template with repositories
        return render(request, 'repo.html', {'repositories': results})


    
class PastProjectView(ProjectView):
    def get(self, request, *args, **kwargs):
        try:
            query = "SELECT * FROM projects"
            with connection.cursor() as cursor:
                cursor.execute(query)
                columns = [col[0] for col in cursor.description]  # Get column names
                data = [
                    dict(zip(columns, row)) for row in cursor.fetchall()
                ]  # Map rows to dictionaries

            return render(request, "project-Table.html", {"projects": data})
        except Exception as e:
            return HttpResponse(f"Database error: {str(e)}", status=500)
        

class SkillListView(View):
    template_name = 'skill.html'

    def get(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, proficiency, created_at, updated_at, picture FROM skills")
            skills = [
                {
                    'id': row[0],
                    'name': row[1],
                    'proficiency': row[2],
                    'created_at': row[3],
                    'updated_at': row[4],
                    'picture': row[5],
                }
                for row in cursor.fetchall()
            ]
        print(skills)  # Debug log
        return JsonResponse({'Technical_skill': skills})  # Temporary for debugging



class Technical_Skills(View):
    template_name = 'technical_skill.html'
    def get(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, proficiency, created_at, updated_at, picture FROM skills")
            skills = [
                {
                    'id': row[0],
                    'name': row[1],
                    'proficiency': row[2],
                    'created_at': row[3],
                    'updated_at': row[4],
                    'picture': row[5],
                }
                for row in cursor.fetchall()
            ]
        
       
        context = {'Technical_skill': skills}  
        return render(request, self.template_name, context)
    

class WebsitePolicyView(View):
    """
    Class-based view to handle the display of website policies using a raw SQL query.
    """

    def get(self, request):
        # Raw SQL query to fetch policy data
        query = "SELECT policy_statement, created_at, updated_at FROM website_policy"
        with connection.cursor() as cursor:
            cursor.execute(query)
            policies = [
                {
                    "policy_statement": row[0],
                    "created_at": row[1],
                    "updated_at": row[2],
                }
                for row in cursor.fetchall()
            ]

        # Render the template with policies data
        return render(request, 'policy_popup.html', {'policies': policies})



import logging

logger = logging.getLogger(__name__)

class ReferenceView(View):
    def get(self, request):
        # Use raw SQL for fetching data (if required)
        query = "SELECT name, email, company, role, picture FROM references_table"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                reference_data = [
                    {
                        "name": row[0],
                        "email": row[1],
                        "company": row[2],
                        "role": row[3],
                        "picture": row[4],
    
                    }
                    for row in cursor.fetchall()
                ]
        except Exception as e:
            # Log the error and provide fallback data
            logger.error(f"Database query failed: {e}")
            reference_data = []
        #print(reference_data, flush=True)


        return render(request, 'reference.html', {
            'reference_data': json.dumps(reference_data)  # Serialize JSON properly
        })
    




from django.utils.timezone import now, timedelta

class BugReportsView(View):
    template_name = 'bug_reports.html'

    def get(self, request):
        # Filter parameter from the GET request
        date_filter = request.GET.get('date_filter')
        filter_date = None

        # Determine the date range
        if date_filter == 'today':
            filter_date = now().date()
        elif date_filter == 'week':
            filter_date = now() - timedelta(days=7)
        elif date_filter == 'month':
            filter_date = now() - timedelta(days=30)
        elif date_filter == 'year':
            filter_date = now() - timedelta(days=365)

        # Raw SQL query with optional filtering
        raw_query = """
            SELECT 
                u.id AS user_id, 
                u.name AS user_name, 
                u.email AS user_email, 
                br.id AS report_id, 
                br.bug_type, 
                br.report,
                br.solution,
                br.posted_date
            FROM "user" u
            LEFT JOIN bug_report br ON u.id = br.user_id
        """
        if filter_date:
            raw_query += " WHERE br.posted_date >= %s"
            query_params = [filter_date]
        else:
            query_params = []

        raw_query += " ORDER BY u.id, br.posted_date DESC;"

        # Execute the query
        with connection.cursor() as cursor:
            cursor.execute(raw_query, query_params)
            results = cursor.fetchall()

        # Process results into structured data
        users = {}
        for row in results:
            user_id = row[0]
            user_name = row[1] if row[1] else None
            user_email = row[2]
            report_id = row[3]
            bug_type = row[4]
            report = row[5]
            solution = row[6]
            posted_date = row[7]

            if user_id not in users:
                users[user_id] = {
                    'display_name': user_name if user_name else user_email,
                    'bug_reports': []
                }

            if report_id:  # Only add the report if it exists
                comments = Comment.objects.filter(bug_report_id=report_id)
                users[user_id]['bug_reports'].append({
                    'id': report_id,
                    'bug_type': bug_type,
                    'report': report,
                    'solution': solution,
                    'posted_date': posted_date,
                    'comments': comments
                })

        # Convert the dictionary to a list for rendering
        user_list = list(users.values())
        form = CommentForm()

        return render(request, self.template_name, {'users': user_list, 'form': form})


    #@method_decorator(login_required)
    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            bug_report_id = request.POST.get('bug_report_id')
            bug_report = get_object_or_404(BugReport, id=bug_report_id)
            comment = form.save(commit=False)
            # Assign user only if authenticated, else set to None
            comment.user = request.user if request.user.is_authenticated else None
            comment.bug_report = bug_report
            comment.save()
        return redirect('bug_reports')


class PostBug(View):
    template_name = 'Report-bug.html'

    def get(self, request):
        # Render the form for GET requests
        return render(request, self.template_name)
    

    def post(self, request):
        # Extract form data from POST request
        email = request.POST.get('email')
        name = request.POST.get('name', '').strip()
        bug_type = request.POST.get('bug_type')
        report = request.POST.get('report')
        solution = request.POST.get('solution', '')

        # Validate required fields
        if not email or not bug_type or not report:
            return JsonResponse({"error": "Email, Bug Type, and Report fields are required."}, status=400)

        # Validate or create user by email
        user, created = User.objects.get_or_create(email=email)
        if created and name:  # Set the name for a new user
            user.name = name
            user.save()

        # Create and save the BugReport instance
        BugReport.objects.create(
            user=user,
            bug_type=bug_type,
            report=report,
            solution=solution if solution else None,
            posted_date=now()
        )

        return redirect(reverse('bug_reports'))
    
from django.http import FileResponse, Http404

class DownloadCVView(View):
    def get(self, request):
        try:
            # Absolute path to the CV file in the static folder
            file_path = os.path.join(
                "PortfolioApp/static/PDF", "2025_CV.pdf"
            )

            # Fixed download filename
            custom_filename = "Isaac-Obi-Arum-Cv.pdf"

            # Open the file and serve it as a downloadable response
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=custom_filename)
        except FileNotFoundError:
            raise Http404("CV not found")
