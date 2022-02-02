import requests
from git_cloud_backup import GitCloudBackup
from requests.auth import HTTPBasicAuth


class GitHubBackup(GitCloudBackup):
    """
    GitHub Cloud Backup Class
    """

    base_api_url = 'https://api.github.com/user/repos?visibility=all'

    def __init__(self, backup_directory, directory_prefix, username, token, organization):
        self.username = username
        self.token = token
        self.organization = organization
        repo_dict_array = self.get_repo_data()

        super().__init__(
            repo_dict_array,
            backup_directory,
            directory_prefix
        )

    def get_repo_data(self):
        response = requests.get(
            self.base_api_url,
            auth=HTTPBasicAuth(
                self.username,
                self.token
            )
        )

        if response.status_code == 200:
            response_json_data = response.json()

            response_array = []

            for repo in response_json_data:
                dict = {'name': repo['name'], 'git_ssh_url': repo['ssh_url']}
                response_array.append(dict)

            return response_array

        return False
