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
from .models import AboutMe, Project



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

            return render(request, "project.html", {"projects": data})
        except Exception as e:
            return HttpResponse(f"Database error: {str(e)}", status=500)