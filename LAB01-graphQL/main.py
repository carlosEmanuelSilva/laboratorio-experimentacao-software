import requests

url = "https://api.github.com/graphql"
token = "token"
headers = {"Authorization" : f"token {token}"}
body = """
query {
  search(query: "topic:Open Source sort:stars-desc", type: REPOSITORY, first: 10) {
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

response = requests.post(url=url, headers=headers, json={"query" : body})
print(response.status_code)
if response.status_code == 200:
    print("reponse : ", response.content)
else:
    raise Exception(f"Falha na requisição para o repositório: {response.status_code}")
