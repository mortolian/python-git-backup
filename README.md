# GIT Backup

This is a GIT backup program created in Python to backup repos to an on premises
location. Although we put everything in the cloud and a total loss of data is not too likely,
I was not willing to take that chance. At the very least I will feel better and maybe even avoid
some lost work hours if something did go wrong.

## How it works

### Step 1
The backup program will collect all the repo config data from the config file. A config can either 
automatically collect all repo data from the cloud vendor it supports (or you can extend) or you can specify a single 
repo backup item from any repo.

The configuration file `config.example.json` is in the root of the application source. 
To configure the application rename the example file to `config.json`.

### Step 2
You will have to set up access to every private repo you would like to back-up.
The way to do this is to setup SSH keys for every repo or die vendor account and 
lock this down with a privilage limited backup user created for this task.

### Step 3
You can now run the backup program manually or add it into a cron or other 
task management program.

Example of excuting a back-up from shell:
```commandline
python3 git-backup/main.py
```

Example of cron:
```commandline
0 4 * * *   /usr/bin/python3 /home/{username}/git-backup/main.py > /home/{username}}/logs/gitbackup.log 2>&1
```

### The file structure generated

```
--+
   - {Specified Backup dir}
       - {prefix}
          - backups
             - {prefix}_yyyymmddHHSS.zip
          - temp (temporary storage while process is running)

```

### Days backups are kept
You can configure the number of days backups are kept in the `config.json` by setting `days_to_keep_backups`.
Keep in mind that this will work on time in seconds from the time the file was created.

There is no backup file rotation at the moment (daily, monthly, weekly.).

## Requirements
- Docker 20.x.x
- Python 3.9.9
- Python Lib : requests [Documentation](https://docs.python-requests.org/en/latest/#)
- Python Lib : shutil, os

## Roadmap
- Create an alert hook of some kind when a backup fails, alerts to a chat application or something.
- Dockerise the application.
- Make the 

## Contribution
Anyone is welcome to fork the project and evolve it or can create a pull request with improvements.

## References

### BitBucket Documentation and Useful Links
- URL to get app passwords: https://bitbucket.org/account/settings/app-passwords/
- Documentation: https://developer.atlassian.com/
- Documentation: https://developer.atlassian.com/cloud/bitbucket/getting-started/
- Documentation: https://developer.atlassian.com/cloud/bitbucket/rest/intro/

### GitHub Documentation and Useful Links

- Documentation: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-token
- Documentation: https://docs.github.com/en/rest/overview/other-authentication-methods#basic-authentication
- Documentation: https://docs.github.com/en/rest
- Create a token: https://github.com/settings/developers