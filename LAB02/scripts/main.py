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
query($cursor: String) {
  search(query: "language:java stars:>1 sort:stars-desc", type: REPOSITORY, first: 20, after: $cursor) {
    pageInfo {
      endCursor
    }
    edges {
      node {
        ... on Repository {
          name
          createdAt
          url
          releases {
            totalCount
          }
          stargazerCount
        }
      }
    }
  }
}
"""
list_of_dict = []

def get_repos(cursor):
    variable = {'cursor': cursor}
    response = requests.post(url=BASE_URL, headers=REQUEST_HEADERS, json={"query" : QUERY_STRING, "variables": variable})
    if response.status_code == 200:
        json_response = json.loads(response.content.decode('utf-8'))
        return json_response
    else:
        raise Exception(f"Falha na requisição para o repositório: {response.status_code}")

def get_info():
    cursor = ""
    while len(list_of_dict) < 1000:

        json_response = get_repos(cursor)
        list_repo = json_response["data"]["search"]["edges"]

        for repo in list_repo:
            node = repo["node"]
            this_repo = {'name': {node["name"]}, 
                        'create_date': {node["createdAt"][:10]}, 
                        'total_releases': {node["releases"]["totalCount"]}, 
                        'total_stars': {node["stargazerCount"]},
                        'url': {node['url']}}
                        
            
            list_of_dict.append(this_repo)

        cursor = json_response["data"]["search"]["pageInfo"]["endCursor"]

def save_to_csv():
    filename = "repos.csv"
    fields = ['name', 'create_date', 'total_releases', 'total_stars', 'url']

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(list_of_dict)

if __name__ == "__main__":
    repos_info = get_info()
    save_to_csv()
