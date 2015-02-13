#!/usr/bin/env ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "precise32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"
  config.vm.network :forwarded_port, guest: 8000, host: 8050
  config.ssh.forward_agent = true
  config.vm.synced_folder './devops', '/vagrant/devops', 
      :mount_options => ['fmode=666']
  
  #config.vm.provision :shell, :path => "devops/boot.sh"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "devops/start.yml"
    ansible.inventory_path = "devops/inventory/development"
    ansible.limit = "localhost"
    #ansible.verbose = "v"
  end

  # Cache apt-get package downloads to speed things up
  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
    config.cache.enable :generic, { :cache_dir => "/var/cache/pip" }
  end

end