=============
Pybay website
=============


Infrastructure
==============

Steps to configure the production infrastucture on linode::

    PYBAY_PATH=/data/pybay

    sudo su
    mkdir -p /data
    apt-get install nginx
    mkdir /var/log/nginx

    # Deploy pybay
    git clone http://github.com/mzdaniel/pybay_front_end $PYBAY_PATH
    cd $PYBAY_PATH
    chown -R www-data.www-data $PYBAY_PATH
    rm /etc/nginx/sites-enabled/default
    ln -s $PYBAY_PATH/infrastructure/pybay_nginx.conf /etc/nginx/sites-enabled
    /etc/init.d/nginx start

    cd $PYBAY_PATH
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    pip install -U /data/uWSGI-2.0.15-cp35-cp35m-linux_x86_64.whl

    # Create project, app and consolidate cfg with django-admin and mv commands
    ./manage.py migrate
    ./manage.py loaddata fixtures/*
    ./manage.py runserver

    /data/pybay/venv/bin/uwsgi --ini /data/pybay/infrastructure/pybay_uwsgi.ini --daemonize /var/log/uwsgi.log

    # Launch uwsgi on reboot
    sed -Ei 's/exit 0//' /etc/rc.local
    echo -e "/data/pybay/venv/bin/uwsgi --ini /data/pybay/infrastructure/pybay_uwsgi.ini --daemonize /var/log/uwsgi.log\nexit 0" >> /etc/rc.local



Developer site
==============

::

    git clone
    cd pybay_front_end
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    # Create project, app and consolidate cfg with django-admin and mv commands
    ./manage.py migrate
    ./manage.py loaddata fixtures/*
    ./manage.py runserver

    # For testing purposes use the admin interface with user: test and password: test
