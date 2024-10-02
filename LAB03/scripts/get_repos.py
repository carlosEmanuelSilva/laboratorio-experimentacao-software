import requests
import json
import csv
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.github.com/graphql"

ACCESS_TOKEN = os.getenv("TOKEN")

REQUEST_HEADERS = {"Authorization" : f"token {ACCESS_TOKEN}"}

QUERY_STRING = """
query($cursor: String) {
  repos: search(query: "stars:>1 sort:stars-desc", type: REPOSITORY, first:10, after:$cursor) {
    pageInfo{
        endCursor
    }
    edges {
      node {
        ... on Repository {
            name
            owner{
                login
            }
  		}		
	}
    }
  }
}
"""

list_of_results = []

def get_repos(cursor):
    variable = {'cursor': cursor}
    response = requests.post(url=BASE_URL, headers=REQUEST_HEADERS, json={"query": QUERY_STRING, "variables": variable})
    if response.status_code == 200: 
        json_response = json.loads(response.content.decode('utf-8'))
        return json_response
    else:
        raise Exception(f"Falha na requisição para o repositório: {response.status_code}")

def get_info():
    cursor = ""
    while len(list_of_results) < 200:
        json_response = get_repos(cursor)
        list_repos = json_response["data"]["repos"]["edges"]
        
        for repo in list_repos:
            node = repo["node"]
            this_repo = {'name': {node["name"]},
                        'owner': {node["owner"]["login"]}
                        }
            list_of_results.append(this_repo)

        cursor = json_response["data"]["repos"]["pageInfo"]["endCursor"]

def save_to_csv():
    filename = "../results/repos.csv"
    fields = ["name", "owner"]

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(list_of_results)

if __name__ ==  "__main__":
    repos_info = get_info()
    save_to_csv()


