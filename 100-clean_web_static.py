#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives, using the function do_clean.
"""

from fabric.api import env, run, local
from datetime import datetime
from os.path import exists
from fabric.operations import put

# Set the username and hosts to connect to
env.user = 'ubuntu'
env.hosts = ['54.162.83.217', '3.85.168.57']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    try:
        # Convert number to integer
        number = int(number)

        # Get a list of all archives in the versions folder
        archives_local = local('ls -t versions', capture=True).split()

        # Keep only the most recent 'number' of archives
        archives_to_keep = archives_local[:number]

        # Delete all unnecessary archives in the versions folder
        for archive in archives_local:
            if archive not in archives_to_keep:
                local('rm versions/{}'.format(archive))

        # Get a list of all archives in the /data/web_static/releases folder
        archives_remote = run('ls -t /data/web_static/releases').split()

        # Keep only the most recent 'number' of archives
        archives_to_keep_remote = archives_remote[:number]

        # Delete all unnecessary archives in the /data/web_static/releases folder
        for archive_remote in archives_remote:
            if archive_remote not in archives_to_keep_remote:
                run('rm -rf /data/web_static/releases/{}'.format(archive_remote))

        print('Cleaning completed!')
        return True
    except Exception as e:
        print('Error:', e)
        return False
