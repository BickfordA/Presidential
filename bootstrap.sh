#!/bin/bash

echo "starting update"

apt-get update
apt-get install python-virtualenv -y

echo "moving to presidential dir"
cd /vagrant/presidential/

echo "creating virtual env"
virtualenv flask
. flask/bin/activate

echo "installing mySQL"
#http://www.thisprogrammingthing.com/2013/getting-started-with-vagrant/
#http://www.sitepoint.com/vagrantfile-explained-setting-provisioning-shell/
#http://stackoverflow.com/questions/23959457/connect-to-mysql-on-vagrant-instance-with-sequel-pro
#https://github.com/AlexDisler/mysql-vagrant/blob/master/install.sh

sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'

echo "preparing install"
sudo apt-get -y install mysql-server

# http://stackoverflow.com/questions/24855942/vagrant-ssh-setting-up-and-connecting-to-mysql
# fill in the blanks for root password, db name, username (local), and password
#mysql -uroot -proot -e "
#CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
#CREATE USER 'root'@'%' IDENTIFIED BY 'root';
#GRANT ALL PRIVILEGES ON * . * TO 'root'@'localhost';
#GRANT ALL PRIVILEGES ON * . * TO 'root'@'%';
#FLUSH PRIVILEGES;
#CREATE DATABASE presidential_db;"

#echo "DROP DATABASE IF EXISTS presdb" | mysql -uroot -proot
#echo "CREATE USER 'root'@'localhost' IDENTIFIED BY 'root'" | mysql -uroot -proot
if [ ! -f /var/log/presidentialsetup ];
then
  echo "CREATE DATABASE PRESIDENTIAL" | mysql -uroot -proot
  echo "GRANT ALL ON PRESIDENTIAL.* TO 'root'@'localhost'" | mysql -uroot -proot
  echo "GRANT ALL ON PRESIDENTIAL.* TO 'root'@'%'" | mysql -uroot -proot
  echo "FLUSH PRIVILEGES" | mysql -uroot -proot

  touch /var/log/presidentialsetup

  if [ -f /vagrant/data/PRESIDENTIAL.sql ];
  then
      mysql -uroot -proot PRESIDENTIAL < /vagrant/data/PRESIDENTIAL.sql
  fi
fi

# change bind address to allow connections from anywhere
sed -i "s/bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/my.cnf


echo "restarting mySQL"

sudo service mysql restart

echo "installing libs"

echo
flask/bin/pip install flask
flask/bin/pip install flask-login
flask/bin/pip install flask-openid
flask/bin/pip install flask-mail
flask/bin/pip install flask-sqlalchemy
flask/bin/pip install sqlalchemy-migrate
flask/bin/pip install flask-whooshalchemy
flask/bin/pip install flask-wtf
flask/bin/pip install flask-babel
flask/bin/pip install guess_language
flask/bin/pip install flipflop
flask/bin/pip install coverage
flask/bin/pip install watchdog
