# autoupdate.py

import requests

def get_latest_release_version(repo_owner, repo_name, access_token):
    # url = f"https://api.github.com/repos/vinaynmcci/autoupdate/releases/latest"
    url = f"https://api.github.com/repos/vinaynmcci/Cricket/releases/latest"
    headers = {"Authorization": f"token {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["tag_name"]
    else:
        return None

def check_for_update(repo_owner, repo_name, access_token):
    latest_version = get_latest_release_version(repo_owner, repo_name, access_token)
    print(latest_version)
    return latest_version

if __name__ == "__main__":
    repo_owner = "vinaynmcci"
    repo_name = "Cricket"
    access_token = "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"
    latest_version = check_for_update(repo_owner, repo_name, access_token)
    print(latest_version)
