#!/usr/bin/python3
'''a Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy:'''

from fabric.api import run, put, env
import os
from os.path import exists


# Define the list of web servers
env.hosts = ['54.162.83.217', '3.85.168.57']
env.user = 'ubuntu'
def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.
    """
    if not exists(archive_path):
        print("Error: Archive file does not exist.")
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to the folder /data/web_static/releases/<archive filename without extension>
        filename = archive_path.split('/')[-1]
        folder_name = '/data/web_static/releases/{}'.format(filename[:-4])
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {} --strip-components=1'.format(filename, folder_name))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(filename))

        # Delete the existing symbolic link /data/web_static/current
        run('rm /data/web_static/current')

        # Create a new symbolic link linked to the new version of the code
        run('ln -s {} /data/web_static/current'.format(folder_name))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Error:", e)
        return False
