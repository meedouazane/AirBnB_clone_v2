#!/usr/bin/python3
''' generates a .tgz archive from the contents of the web_static folder '''
from fabric import task


def do_pack():
    ''' Compress Files '''
    run("mkdir -p versions")
    run("tar -czvf versions/'web_static_$(date +'%Y%m%d%H%M%S').tgz' -C web_static .")
