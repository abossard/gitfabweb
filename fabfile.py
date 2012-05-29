from fabric.api import *

env.use_ssh_config = True

def host_type():
    run('uname -s')

def install_web():
    run('apt-get -s install libapache2-mod-php5 php5-cgi php5 php5-mysql php5-mcrypt apache2 php5-gd mysql-client')

def install_db():
    run('apt-get -s install mysql-server')

