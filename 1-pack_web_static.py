#!/usr/bin/python3
''' Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.'''
from fabric.api import local
from datetime import datetime

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
