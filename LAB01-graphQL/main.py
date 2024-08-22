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
    list_of_dict = []

    for repo in list_repo:
        node = repo["node"]

        this_repo = {'name': {node["name"]}, 'create_date': {node["createdAt"]}, 'total_pull_requests': {node["pullRequests"]["totalCount"]},
                     'total_releases': {node["releases"]["totalCount"]}, 'last_commit_date': {node["defaultBranchRef"]["target"]["committedDate"]},
                     'main_language': {node["primaryLanguage"]["name"]}, 'total_issues': {node["issues"]["totalCount"]}, 
                     'total_stars': {node["stargazerCount"]}}

        list_of_dict.append(this_repo)

    return list_of_dict
if __name__ == "__main__":
    response = get_repos()
    repos_info = create_dict(response)
    print(repos_info)
