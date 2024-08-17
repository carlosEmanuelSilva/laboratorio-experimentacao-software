import requests
from datetime import datetime

token = "token"

#Função para obeter os repositórios mais populares com o termo-chave "open source"
def get_popular_repos(termo_chave, num_repos):
    url = f"https://api.github.com/search/repositories?q={termo_chave}&sort=stars&order=desc&per_page={num_repos}"
    headers = {"Authorization" : f"token {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["items"]
    else:
        raise Exception(f"Falha na requisição para o repositório: {response.status_code}")

#Função para obter detalhes de um repositório
def get_detalhes_repos(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Authorization" : f"token {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Falaha na requisição de detalhes do repositório: {reponse.status_code}")

#Função para obter todas as Pull Requests mescladas
def get_pull_requests(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=closed"
    headers = {"Authorization" : f"token {token}"}
    page = 1
    pull_requests = []

    while True:
        response = requests.get(f"{url}&page={page}&per_page=100", headers=headers)
        if response.status_code == 200:
            page_pull_request = response.json()
            if not page_pull_request:
                break
    
            for pr in page_pull_request:
                if pr.get('merget_at'):
                    pull_requests.append(pr)

            page += 1
        else:
            raise Exception(f"Falha na requisição das pull request: {response.status_code}")
    
    return len(pull_requests)

#Função para obter as releases
def get_releases(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    headers = {"Authorization" : f"token {token}"}
    page = 1
    releases = []

    while True:
        response = requests.get(f"{url}?page={page}&per_page=100", headers=headers)
        if response.status_code == 200:
            page_release = response.json()
            if not page_release:
                break
            release.extend(page_release)
            page += 1
        else:
            raise Exception(f"Falaha na requisição das releases: {response.status_code}")

    return len(releases)

#Função para calcular quanto tempo se passou desde a ultima atualização
def get_ultima_atualizacao(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Authorization" : f"token {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        info_repo = response.json()
        str_ultima_atualizacao = info_repo['pushed_at']
        ultima_atualizacao = datetime_object = datetime.strptime(str_ultima_atualizacao, '%Y-%m-%dT%H:%M:%SZ')

        return datetime.now() - ultima_atualizacao
    
    else:
        raise Exception(f"Falha na requisição da última atualização: {response.status_code}")


#Função para listar a linguagem primária do repositório
def get_linguagem(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    headers = {"Authorization" : f"toke {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        linguagem = response.json()

        linguagem_primaria = max(linguagem, key=linguagem.get)

    return linguagem_primaria

#Função para calcular a quantidade total de issues no repósitório 
def get_issues_totais(owner, repo):
    url= f"https://api.github.com/repos/{owner}/{repo}/issues?state=all"
    headers = {"Authorization" : f"token {token}"}
    page = 1
    all_issues = []

    while True:
        response = requests.get(f"{url}&page={page}&per_page{100}", headers=headers)

        if response.status_code == 200:
            page_issues = response.json()
            if not page_issues:
                break
            all_issues.extend(page_issues)
            page+=1
        else:
            raise Exception("Falaha na requisição de todas as issues: {response.status_code}")
    
    return len(all_issues)

#Função para calacular quantidade de issues fechadas no repositório
def get_issues_fechadas(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=closed"
    headers = {"Authorization" : f"token {token}"}
    page = 1
    closed_issues = []

    while True:
        response = requests.get(f"{url}&page={page}&per_page={100}", headers=headers)

        if response.status_code == 200:
            page_issues = response.json()
            if not page_issues:
                break
            closed_issues.extend(page_issues)
            page+=1
        else:
            raise Exception("Falha na requisição das issues fechadas: {response.status_code}")

    return len(closed_issues)

#Função para calcular a porcentagem de issues fechadas
def get_porcentagem_issues(owner,repo):
    return (get_issues_fechadas(owner, repo)/get_issues_totais(owner,repo)) * 100

#Função para coletar e imprimir dados dos repositórios
def coletar_e_imprimir_dados(repos):
    for repo in repos:
        owner = repo["owner"]["login"]
        repo_name = repo["name"]
        repo_details = get_detalhes_repos(owner, repo_name)
        
        pull_requests = get_pull_requests(owner, repo_name)
        releases = get_releases(owner, repo_name)
        main_language = get_linguagem(owner, repo_name)
        closed_issues = get_porcentagem_issues(owner, repo_name)
        day_since_last_commit =  get_ultima_atualizacao(owner, repo_name)


        print(f"Repository: {repo_name}")
        print(f"Owner: {owner}")
        print(f"URL: {repo_details['html_url']}")
        print(f"Stars: {repo_details['stargazers_count']}")
        print(f"Forks: {repo_details['forks_count']}")
        print(f"Commits: {repo_details['open_issues_count']}")
        print(f"Watchers: {repo_details['watchers_count']}")
        print(f"Pull Requests: {pull_requests if pull_requests is not None else 'N/A'}")
        print(f"Last Commit Date: {repo_details['pushed_at']}")
        print(f"Day since the last commit: {day_since_last_commit}")
        print(f"Main Language: {main_language}")
        print(f"License: {repo_details['license']['name'] if repo_details['license'] else 'No license'}")
        print(f"Contributors: {repo_details['network_count']}")
        print(f"Size: {repo_details['size']} KB")
        print(f"Main Branch: {repo_details['default_branch']}")
        print(f"Releases: {releases if releases is not None else 'N/A'}")
        print(f"Closed Issues (%): {closed_issues if closed_issues is not None else 'N/A'}")
        print(f"Topics: {', '.join(repo_details['topics']) if 'topics' in repo_details else 'No topics'}")
        print("-" * 200)

#Main
if __name__ == "__main__":
    keyword = "open source"
    num_repos = 1
    try:
        popular_repos = get_popular_repos(keyword, num_repos)
        coletar_e_imprimir_dados(popular_repos)
    except Exception as e:
        print(e)
