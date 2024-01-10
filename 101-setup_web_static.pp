#!/usr/bin/env bash
# Puppet for setup
file { /data:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu'
}
file { /data/'web_static':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu'
}
file { /data/web_static/'releases':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu'
}
file { /data/web_static/releases/test/:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu'
}
file { /data/web_static/shared/:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu'
}
file {'/data/web_static/releases/test/index.html':
  ensure  => file,
  content => 'Hello World! this is from Airbnb',
}
exec { 'create_alias':
  command => 'ln -sfT /data/web_static/releases/test/ /data/web_static/current',
  path    => ['/bin', '/usr/bin'],
}
# update ubuntu server
exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}

#install nginx
-> package {'nginx':
  ensure   => 'installed',
  provider => apt,
}

# editing config file
-> file {'/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
        listen 80 ;
        listen [::]:80;
        root /var/www/html;
        index index.html;
        server_name _;
        location /hbnb_static {
                alias /data/web_static/current;
        }
        location / {
                try_files $uri $uri/ =404;
        }
}',
  notify  => Service['nginx'],
}

# starting service
-> service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
