#!/usr/bin/python3
'''a Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy:'''

from fabric.api import run, put, env
import os
from os.path import exists


# Define the list of web servers
env.hosts = ['54.175.255.107', '3.85.168.57']
env.user = 'ubuntu'
def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.
    """
    if not exists(archive_path):
        print("Error: Archive file does not exist.")
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Get the filename of the archive
        archive_filename = os.path.basename(archive_path)
        # Extract the name without extension
        archive_name = os.path.splitext(archive_filename)[0]

        # Uncompress the archive to /data/web_static/releases/<archive_name> on the web server
        run("mkdir -p /data/web_static/releases/{}".format(archive_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_filename, archive_name))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_filename))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current linked to the new version
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive_name))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Error:", e)
        return False
