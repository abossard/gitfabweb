from fabric.api import *
from fabric.contrib import files

env.use_ssh_config = True

env.web_target_path = '/var/www/mystory'
env.git_url = 'git@github.com:psoluch/mystory.jesus.net.git'
env.branch = 'dev'

env.required_web_packages = 'libapache2-mod-php5 php5-cgi php5 php5-mysql php5-mcrypt apache2 php5-gd mysql-client git'
env.required_db_packages = ''


def host_type():
    run('uname -s')

def install_web():
    run('apt-get -y install %s'%env.required_web_packages)

def uninstall_web():
    run('apt-get -y remove %s'%env.required_web_packages)

def install_db():
    run('apt-get -s install mysql-server')

def deploy_web():
    if not files.exists(env.web_target_path):
        run('git clone %s %s' %(env.git_url, env.web_target_path ))
        with cd(env.web_target_path):
            run('git checkout %s' % (env.branch,))
        run('chown -R www-data:www-data %s' %(env.web_target_path, ))
    else:
        with cd(env.web_target_path):
            run('git pull')

def undeploy_web():
    run('rm -rf %s'%env.web_target_path)