from fabric.api import *
from fabric.contrib import files

env.use_ssh_config = True
env.sync_dir = '~/sync/'
env.source_git = 'git@github.com:psoluch/mystory.jesus.net.git'
env.source_name = 'mystory.jesus.net'
env.source_branch = 'dev'

env.target_git = 'git@git.pagodabox.com:abossard-mystory.git'
env.target_name = 'abossard-mystory'

def deploy():
    print files.exists(env.sync_dir)
    if not files.exists(env.sync_dir):
        run('mkdir %s'%env.sync_dir)
    with cd(env.sync_dir):
        refresh_git(env.source_git, env.source_name, env.source_branch);
        refresh_git(env.target_git, env.target_git);

def undeploy():
    run('rm -rf %s'%env.sync_dir)

def refresh_git(gitsrc, target_dir, branch=None):
    if files.exists(target_dir):
        with cd(target_dir):
            run('git pull')
    else:
        run('git clone %s %s' %(gitsrc, target_dir ))
        if branch:
            run('git checkout %s' % branch)
