from backup_bitbucket import BitBucketBackup
from backup_github import GitHubBackup
from backup_single import SingleGitBackup
from backup_get_config import GetJsonConfig
import os


if __name__ == "__main__":
    # Read the configuration from the JSON configuration file
    json_backup_config = GetJsonConfig(os.path.dirname(os.path.realpath(__file__)) + "/config.json").get_content()

    backup_directory = json_backup_config['backup_directory']

    for backup_config in json_backup_config['backup_jobs']:
        if backup_config['vendor'] == 'bitbucket':
            backup = BitBucketBackup(
                backup_directory,
                "bitbucket",
                backup_config['bitbucket_username'],
                backup_config['bitbucket_app_password']
            )

        if backup_config['vendor'] == 'github':
            backup = GitHubBackup(
                backup_directory,
                "github",
                backup_config['github_username'],
                backup_config['github_token'],
                backup_config['github_organization']
            )

        if backup_config['vendor'] == 'single':
            backup = SingleGitBackup(
                backup_directory,
                "single",
                backup_config['git_repo_name'],
                backup_config['git_ssh_url']
            )

        if backup:
            backup.backup()
            backup.compress()
            backup.rotate(3)
            backup = None
