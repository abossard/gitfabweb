How to install a wordpress based app on padogabox


1. Go to https://dashboard.pagodabox.com/ and create a new app
1. Choose wordpress as app type
1. Rename it in the Admin part of the apps Dashboard to your liking
1. Remember the git url it has now. E.g. git@git.pagodabox.com:abossard-mystory.git
1. add your publish ssh key, to the registerd ssh keys: https://dashboard.pagodabox.com/account/edit
1. clone the directory to an empty directory

    git clone git@git.pagodabox.com:abossard-mystory.git

1. clone your source directory as well 

    git clone git@github.com:psoluch/mystory.jesus.net.git

1. move to your working branch

    git checkout dev

1. copy over the files from your source directory to the target

    cp -vr mystory.jesus.net/* abossard-mystory/
  (don't forget the * as it prevents .git form being copied)

1. copy over the .htaccess file

    cp -v mystory.jesus.net/.htaccess abossard-mystory/

1. add everything to the git repo

    git add .; git commit -am "init"

1. push it

    git push

Database setup

1. install the pagoda utility form here: http://help.pagodabox.com/customer/portal/articles/175474

more to come 