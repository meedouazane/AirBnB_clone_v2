#!/usr/bin/python3
''' distributes an archive to your web servers '''
from fabric.api import env, run, put
from os.path import exists

env.hosts = ['54.167.181.186', '35.153.194.155']


def do_deploy(archive_path):
    """ Deploy archive! """
    if exists(archive_path) is True:
        try:
            put(archive_path, '/tmp/')
            file_name_ext = archive_path.split('/')[1]
            file_name = file_name_ext.split('.')[0]
            run(f"mkdir -p /data/web_static/releases/{file_name}/")
            run(f" tar -xzf /tmp/{file_name_ext} -C "
                f"/data/web_static/releases/{file_name}/")
            run(f"mv /data/web_static/releases/{file_name}/web_static/* "
                f"/data/web_static/releases/{file_name}/")
            run(f"rm -rf /tmp/{file_name_ext}")
            run("rm -rf /data/web_static/current")
            run(f"ln -s /data/web_static/releases/{file_name}/"
                f" /data/web_static/current")
            return True
        except Exception:
            return False
    else:
        return False