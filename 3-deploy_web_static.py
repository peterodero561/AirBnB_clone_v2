#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers,
using the function deploy.
"""
from fabric.api import env, run
from fabric.operations import local
from os.path import exists
from datetime import datetime
from fabric.operations import put


env.user = 'ubuntu'
env.hosts = ['3.85.168.57', '54.162.83.217']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        # Create the versions directory if it doesn't exist
        local("mkdir -p versions")

        # Create the name for the archive
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second
        )

        # Compress the contents of the web_static folder
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path if generated successfully
        return "versions/{}".format(archive_name)
    except Exception as e:
        print("Error:", e)
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        filename = archive_path.split('/')[-1]
        folder_name = '/data/web_static/releases/{}'.format(filename[:-4])
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {} --strip-components=1'.format(
            filename, folder_name))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(filename))

        # Delete the existing symbolic link /data/web_static/current
        run('rm /data/web_static/current')

        # Create a new symbolic link linked to the new version of the code
        run('ln -s {} /data/web_static/current'.format(folder_name))

        print('New version deployed!')
        return True
    except Exception as e:
        print('Error:', e)
        return False


def deploy():
    """
    Creates and distributes an archive to the web servers
    """
    # Create the archive
    archive_path = do_pack()
    if not archive_path:
        return False

    # Deploy the archive
    return do_deploy(archive_path)
