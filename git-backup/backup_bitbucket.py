import requests
from git_cloud_backup import GitCloudBackup
from requests.auth import HTTPBasicAuth


class BitBucketBackup(GitCloudBackup):
    """
    Bitbucket Cloud Backup Class
    """

    base_api_url = "https://api.bitbucket.org/2.0/"

    def __init__(self, backup_directory, directory_prefix, username, password):
        self.username = username
        self.password = password
        repo_dict_array = self.get_repo_data()

        super().__init__(
            repo_dict_array,
            backup_directory,
            directory_prefix
        )

    def get_repo_data(self):
        workspace_response = requests.get(
            self.base_api_url + "workspaces",
            auth=HTTPBasicAuth(
                self.username,
                self.password
            )
        )

        if workspace_response.status_code == 200:
            json_workspace_response = workspace_response.json()

            response_array = []

            for workspace in json_workspace_response['values']:
                repo_response = requests.get(
                    self.base_api_url + "repositories/" + workspace['slug'],
                    auth=HTTPBasicAuth(
                        self.username,
                        self.password
                    )
                )

                if repo_response.status_code == 200:
                    json_repo_response = repo_response.json()

                    repo_dict = {}

                    for repo in json_repo_response['values']:
                        repo_dict['name'] = repo['name']

                        for clone in repo['links']['clone']:
                            if clone['name'] == 'ssh':
                                repo_dict['git_ssh_url'] = clone['href']

                    response_array.append(repo_dict)

            return response_array

        return False
