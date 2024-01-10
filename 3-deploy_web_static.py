#!/usr/bin/python3
''' creates and distributes an archive to your web servers '''
from fabric.api import env, run, put
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


env.hosts = ['54.167.181.186', '35.153.194.155']


def deploy():
    ''' Full deployment '''
    archive = do_pack()
    if not archive:
        return False
    deploy = do_deploy(archive)
    return deploy
