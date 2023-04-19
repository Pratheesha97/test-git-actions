# Import required modules
import os
import requests
import datetime

# Get the GitHub repository owner and name from the environment
repo = os.environ['GITHUB_REPOSITORY']
owner, name = repo.split('/')

# Construct the API URL for retrieving issues
api_url = f'https://api.github.com/repos/{owner}/{name}/issues'

# Set the authentication token if provided
auth_token = os.environ.get('GITHUB_TOKEN')
headers = {}
if auth_token:
    headers['Authorization'] = f'token {auth_token}'
    
# Send the API request and get the JSON response
response = requests.get(api_url, headers=headers)
response.raise_for_status()
issues = response.json()

# Print the issue titles and URLs
for issue in issues:
    print(f'{issue["title"]}: {issue["html_url"]}')
