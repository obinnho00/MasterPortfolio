from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .models import *
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import base64
import requests
import sys
import os
import re
import markdown2
from  django.utils.text import slugify
from PortfolioApp.gitconfig.gitconfig import GITHUB_API_URL, USERNAME, TOKEN


from django.views import View
from .models import AboutMe, Project, TechnicalSkill



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

        context = {
            'skills': skills
        }
        return render(request, self.template_name, context)



class Technical_Skills(View):
    def get(self, request):
        query = "SELECT category, name, description, skill_level FROM technical_skill"
        with connection.cursor() as cursor:
            cursor.execute(query)
            skills = [
                {
                    'category': row[0],
                    'name': row[1],
                    'description': row[2],
                    'skill_level':row[3]
                }
                for row in cursor.fetchall()
            ]

        data = {
            'skills': skills
        }
        return render(request, 'technical_skill.html', data)


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



class ReferenceView(View):
    def get(self, request):
        query = "SELECT name, email, company, role, picture FROM reference_table"
        with connection.cursor() as cursor:
            cursor.execute(query)
            reference_data = [
                {
                    "name": row[0],
                    "email": row[1],
                    "company": row[2],
                    "role": row[3],
                    "picture": row[4],  # Ensure this stores the correct file path
                }
                for row in cursor.fetchall()
            ]
        return render(request, "reference.html", {'reference_data': reference_data, 'MEDIA_URL': settings.MEDIA_URL})
