#!/usr/bin/python3
''' creates and distributes an archive to your web servers '''
from fabric.api import env, run, put, local
from os.path import exists
from datetime import datetime
do_deploy = __import__('2-do_deploy_web_static').do_deploy


env.hosts = ['54.167.181.186', '35.153.194.155']
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

def deploy():
    ''' Full deployment '''
    archive = do_pack()
    if exists(archive) is False:
        return False
    deploy = do_deploy(archive)
    return deploy
