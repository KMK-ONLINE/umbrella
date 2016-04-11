#!/usr/bin/env bash

set- e

cd /tmp

sudo apt-get update

wget https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.deb

sudo dpkg -i vagrant_1.8.1_x86_64.deb

sudo apt-get install virtualbox nfs-kernel-server python-pip -y

sudo pip install ansible


