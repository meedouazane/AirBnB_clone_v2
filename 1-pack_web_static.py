#!/usr/bin/python3
''' generates a .tgz archive from the contents of the web_static folder '''
from fabric.api import env, local
from datetime import datetime


env.hosts = ['localhost']


def do_pack():
    ''' Compress Files '''

    local("mkdir -p versions")
    currtime = datetime.now().strftime('%Y%m%d%H%M%S')
    path = f"versions/'web_static_{currtime}.tgz'"
    generate = local(f"tar -czvf {path} -C web_static .")
    if generate:
        return path
    else:
        return None
