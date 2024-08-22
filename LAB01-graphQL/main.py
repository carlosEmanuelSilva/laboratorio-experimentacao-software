import requests
import json

url = "https://api.github.com/graphql"
token = "token"
headers = {"Authorization" : f"token {token}"}
body = """
query {
  search(query: "Open Source sort:stars-desc", type: REPOSITORY, first: 10) {
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

def get_repos():
    response = requests.post(url=url, headers=headers, json={"query" : body})
    if response.status_code == 200:
        json_response = json.loads(response.content.decode('utf-8'))
        return json_response
    else:
        raise Exception(f"Falha na requisição para o repositório: {response.status_code}")

def create_dict(json_response):
    list_repo = json_response["data"]["search"]["edges"]
    for repo in list_repo:
        print(repo["node"]["name"])

if __name__ == "__main__":
    response = get_repos()
    create_dict(response)
