import requests
import json
import csv
import os
import sys
from dotenv import load_dotenv

#Carregando Token de .env
load_dotenv()

BASE_URL = "https://api.github.com/graphql"
ACCESS_TOKEN = os.getenv("TOKEN") 
REQUEST_HEADERS = {"Authorization" : f"token {ACCESS_TOKEN}"}
QUERY_STRING = """
query($query: String!, $num: Int) {
  search(query: $query, type: REPOSITORY, first: $num) {
    edges {
      node {
        ... on Repository {
          name
          createdAt
          pullRequests(states: MERGED) {
            totalCount
          }
          releases {
            totalCount
          }
          defaultBranchRef {
            target {
              ... on Commit {
                committedDate
              }
            }
          }
          primaryLanguage {
            name
          }
          issues(states: CLOSED) {
            totalCount
          }
          stargazerCount
          repositoryTopics(first: 10) {
            edges {
              node {
                topic {
                  name
                }
              }
            }
          }
        }
      }
    }
  }
}
"""

def get_repos(query, num):
    variables = {'query': f'{query} sort:stars-desc', 'num': num}
    response = requests.post(url=BASE_URL, headers=REQUEST_HEADERS, json={"query" : QUERY_STRING, "variables" : variables})
    if response.status_code == 200:
        json_response = json.loads(response.content.decode('utf-8'))
        return json_response
    else:
        raise Exception(f"Falha na requisição para o repositório: {response.status_code}")

def create_dict(json_response):
    list_repo = json_response["data"]["search"]["edges"]
    list_of_dict = []

    for repo in list_repo:
        node = repo["node"]
        this_repo = {'name': {node["name"]}, 
                     'create_date': {node["createdAt"]}, 
                     'total_pull_requests': {node["pullRequests"]["totalCount"]},
                     'total_releases': {node["releases"]["totalCount"]}, 
                     'last_commit_date': {node["defaultBranchRef"]["target"]["committedDate"]},
                     'main_language': {'N/A' if node["primaryLanguage"] == None else node["primaryLanguage"]["name"]}, 
                     'total_issues': {node["issues"]["totalCount"]}, 
                     'total_stars': {node["stargazerCount"]}}

        list_of_dict.append(this_repo)

    return list_of_dict

def save_to_csv(repos_info):
    filename = "repos.csv"
    fields = ['name', 'create_date', 'total_pull_requests', 'total_releases', 'last_commit_date', 'main_language', 'total_issues', 'total_stars']

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(repos_info)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Too few arguments")
    elif len(sys.argv) > 3:
        print("Too many arguments")
    else:
        response = get_repos(sys.argv[1], int(sys.argv[2]))
        repos_info = create_dict(response)
        save_to_csv(repos_info)
