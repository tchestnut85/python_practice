import requests


def create_query(langs, min_stars=50000):
    """Accept a list of languages and generate a query string."""
    query = f"stars:>{min_stars} "

    for lang in langs:
        query += f"language:{lang} "

    return query


def search_repos(langs, sort="stars", order="desc"):
    """Search for Github repos with the given query parameters."""
    github_repo_search_url = "https://api.github.com/search/repositories"
    query = create_query(langs)
    parameters = {
        "q": query,
        "sort": sort,
        "order": order,
    }
    response = requests.get(github_repo_search_url, params=parameters)
    status_code = response.status_code

    if status_code != 200:
        raise RuntimeError(
            f"Server error status code: {status_code}")
    else:
        response_json = response.json()["items"]
        return response_json


if __name__ == "__main__":
    languages = ["Python", "JavaScript", "Ruby"]
    results = search_repos(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars")
