gitfabweb
=========

a Fabfile to deploy a project hosted on github to an apache installation

Configuration
-------------

Which users are required on which host is determined by the ssh_config file (usually stored in ~/.ssh/config)

Speecify the user for each host like this:

    Host linux
    User root

You can also specify and alias e.g. from complicated.hostname.com to host2:

    Host host2
    HostName complicated.hostname.com
    User anotheruser@hostname.com

Then passwordless logins can be enabled with ssh-keygen and ssh-copy-id.



