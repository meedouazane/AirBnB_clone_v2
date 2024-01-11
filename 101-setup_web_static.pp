# Puppet for setup
file { '/data':
  ensure  => 'directory'
} ->
file { '/data/web_static':
  ensure => 'directory'
} ->
file { '/data/web_static/releases':
  ensure => 'directory'
} ->
file { '/data/web_static/releases/test':
  ensure => 'directory'
} ->

file { '/data/web_static/shared':
  ensure => 'directory'
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "Hello World! this is from Airbnb\n\n"
} ->

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
} ->

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/var/www':
  ensure => 'directory'
} ->

file { '/var/www/html':
  ensure => 'directory'
} ->

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School Nginx\n\n"
} ->

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n"
} ->
package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->
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
