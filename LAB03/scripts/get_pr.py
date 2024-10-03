import pandas as pd
import requests
import csv
import json
import os
from datetime import datetime
from dateutil import parser
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.github.com/graphql"
ACCESS_TOKEN = os.getenv("TOKEN")
REQUEST_HEADERS = {"Authorization" : f"token {ACCESS_TOKEN}"}

QUERY = """

query($cursor: String, $name: String!, $owner: String!) {
  repository(owner: $owner, name: $name) {
    pullRequests(states: [MERGED, CLOSED], first: 10, after: $cursor) {
      pageInfo{
        endCursor
      }
      nodes{
      	number
        changedFiles
        additions
        deletions
        createdAt
        closedAt
        mergedAt
        body
        participants{
          totalCount
        }
        totalCommentsCount
      }
    }
  }
}

"""

def get_repos():
    # Abrindo .csv como dataframe
    df = pd.read_csv("../results/repos.csv");
    # Atribuindo à variaveis 'name' e 'owner' suas respectivas 'series'
    name = df[df.columns[0]]
    owner = df[df.columns[1]]
    
    list_of_repos = []
    
    # Iterando sobre todas as linhas do .csv e construindo um dicionário com 'name' e 'owner' o qual é, posteriormente adicionado a uma lista
    for i in range(0, len(df.axes[0])):
        this_repo = {'name': name[i], 'owner': owner[i]}
        list_of_repos.append(this_repo)

    return list_of_repos

def get_pr():
    list_of_repos = get_repos()
    for repo in list_of_repos:
        print(f"Nome: {repo['name']}, Owner: {repo['owner']}")
        construct_info(repo['name'], repo['owner'])

def make_request(cursor, name, owner):
    variables = {'cursor': cursor, 'name': name, 'owner': owner}
    response = requests.post(url=BASE_URL, headers=REQUEST_HEADERS, json={"query" : QUERY, "variables" : variables})
    if response.status_code == 200:
        json_response = json.loads(response.content.decode('utf-8'))
        return json_response
    else:
        raise Exception(f"Falha na requisição para o repositório: {response.status_code}")


def construct_info(name, owner):
    list_pr = []
    cursor = ""

    while len(list_pr) < 100:
        json_response = make_request(cursor, name, owner)
        print("-"*100)
        print(json_response)
        print("-"*100)
        pull_requests = json_response["data"]["repository"]["pullRequests"]["nodes"]
        
        for pr in pull_requests:    
            
            datetime_1 = parser.parse(pr['createdAt'])

            if pr['mergedAt'] != None:
                datetime_2 = parser.parse(pr['mergedAt'])
            elif pr['createdAt'] != None:
                datetime_2 = parser.parse(pr['closedAt'])
            else:
                continue;

            diferenca = datetime_2 - datetime_1

            if(diferenca.total_seconds() / 3600 >= 1):

                this_pr = {'number': pr['number'],
                        'changedFiles': pr['changedFiles'],
                        'additions': pr['additions'],
                        'deletions': pr['deletions'],
                        'createdAt': pr['createdAt'],
                        'closedAt': pr['closedAt'],
                        'mergedAt': pr['mergedAt'],
                        'body': pr['body'],
                        'participants': pr['participants']['totalCount'],
                        'comments': pr['totalCommentsCount']}
                list_pr.append(this_pr)
            
        cursor = json_response["data"]["repository"]["pullRequests"]["pageInfo"]["endCursor"]

    save_to_csv(list_pr)

            
def save_to_csv(list_of_pr):
    filename = "../results/pr.csv"
    fields = ["number", "changedFiles", "additions", "deletions", "createdAt", "closedAt", "mergedAt", "body", "participants", "comments"]

    if os.path.exists(filename):
        with open(filename, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(list_of_pr)
    else:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(list_of_pr)
if __name__ == "__main__":
    get_pr()
