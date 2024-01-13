#!/usr/bin/python3
''' deletes out-of-date archives '''
from fabric.api import run, env, local


env.hosts = ['54.167.181.186', '35.153.194.155']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_clean(number=0):
    '''
    deletes out-of-date archives
    number is the number of the archives, including the most recent,
    to keep
    '''
    number = int(number)
    int(number)
    if number <= 1:
        local("find versions -type f -printf '%T+ %p\n' "
              "| sort -r | tail -n +2 | cut -d' ' -f2- | xargs rm -f")
        run("cd /data/web_static/releases && find . -mindepth 1 "
            "-type d -printf '%T+ %p\n' | sort -r | tail -n +2 "
            "| cut -d' ' -f2- | cut -d'/' -f2 | xargs rm -rf")
    elif number > 1:
        num = number + 1
        local(f"find versions -type f -printf '%T+ %p\n' | sort -r "
              f"| tail -n +{num} | cut -d' ' -f2- | xargs rm -f")
        run(f"cd /data/web_static/releases && find . -mindepth 1 -type d "
            f"-printf '%T+ %p\n' | sort -r | tail -n +{num} | "
            f"cut -d' ' -f2- | cut -d'/' -f2 | xargs rm -rf")
