import datetime
import os
import time
import shutil


class GitCloudBackup:
    def __init__(self, repo_dict_array, backup_directory, directory_prefix):
        self.repo_dict_array = repo_dict_array
        self.backup_directory = backup_directory
        self.directory_prefix = directory_prefix

    def compress(self):
        src = os.path.join(self.backup_directory, self.directory_prefix, 'temp')
        dest = os.path.join(self.backup_directory, self.directory_prefix, 'backups')
        filename = self.directory_prefix + '_' + time.strftime('%Y%m%d%-H%M')

        # Compress
        shutil.make_archive(os.path.join(dest, filename), 'zip', src)

        # Wipe the temporary files
        shutil.rmtree(src)

        return True

    def rotate(self, number):
        if type(number) == int:
            backup_directory = os.path.join(self.backup_directory, self.directory_prefix, 'backups')
            now = time.time()

            # Collect list of files
            for file in os.listdir(backup_directory):
                file_path = os.path.join(backup_directory, file)
                if (now - os.stat(file_path).st_ctime) > number * 86400:
                    print('Delete Old Backup: ', file_path)
                    os.remove(file_path)

    def backup(self):
        if len(self.repo_dict_array):
            for repo in self.repo_dict_array:
                repo_name = repo['name'].replace(' ', '-')
                backup_directory = os.path.join(self.backup_directory, self.directory_prefix, 'temp', repo_name)
                output = '________________ BACKUP ________________\n'
                output += 'Backup Dir: ' + backup_directory + '\n'
                output += 'Backup: ' + repo['git_ssh_url'] + '\n'
                print(output)
                os.system('git clone --mirror ' + repo['git_ssh_url'] + ' ' + backup_directory)

            return True
        else:
            print('Nothing to backup for this backup request.')

        return False
