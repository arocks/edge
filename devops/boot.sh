#!/usr/bin/env bash
#
# Set up Ansible on a Vagrant Ubuntu Precise box, then run the
# development playbook.

echo "provisioning...."

if [[ ! $(ansible --version 2> /dev/null) =~ 1\.6 ]]; then
    sudo rm -rf /var/lib/apt/lists/* && \
    sudo apt-get update && \
    sudo apt-get -y install python-software-properties && \
    sudo add-apt-repository -y ppa:rquillo/ansible && \
    sudo apt-get update && \
    sudo apt-get -y install ansible
fi

PYTHONUNBUFFERED=1 ansible-playbook /vagrant/devops/start.yml \
    --inventory-file=/vagrant/devops/inventory/development \
    --connection=local