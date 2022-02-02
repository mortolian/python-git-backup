import requests
from git_cloud_backup import GitCloudBackup


class SingleGitBackup(GitCloudBackup):
    """
    Single Backup of a Git Repo
    """

    def __init__(self, backup_directory, directory_prefix, repo_name, git_ssh_url):
        self.repo_name = repo_name
        self.git_ssh_url = git_ssh_url
        repo_dict_array = self.get_repo_data()

        super().__init__(
            repo_dict_array,
            backup_directory,
            directory_prefix
        )

    def get_repo_data(self):
        response_array = []
        dict = {'name': self.repo_name, 'git_ssh_url': self.git_ssh_url}
        response_array.append(dict)

        return response_array
