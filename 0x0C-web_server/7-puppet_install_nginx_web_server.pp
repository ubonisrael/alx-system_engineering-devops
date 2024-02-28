# Installs nginx on a server
$server_config = "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /redirect_me {
        return 301 https://www.goal.com;
    }

    error_page 404 /404.html;
    location = /404.html {
                root /var/www/html;
                internal;
    }
}
"
exec { 'update server':
command => '/usr/bin/sudo /usr/bin/apt-get update'
}

exec { 'change owner /var/www':
command => '/usr/bin/sudo /usr/bin/chown -R "$USER":"$USER" /var/www',
require => Package['nginx']
}

exec { 'change owner /etc/nginx':
command => '/usr/bin/sudo /usr/bin/chown -R "$USER":"$USER" /etc/nginx',
require => Package['nginx']
}

package { 'nginx':
ensure  => installed,
require => Exec['update server']
}

file { '/var/www/html/index.nginx-debian.html':
ensure  => present,
content => 'Hello World!',
require => Exec['change owner /var/www']
}

file { '/var/www/html/404.html':
ensure  => present,
content => "Ceci n'est pas une page",
require => Exec['change owner /var/www']
}

file { '/etc/nginx/sites-available/default':
ensure  => present,
content => $server_config,
require => Exec['change owner /etc/nginx']
}

exec { 'restart nginx':
command => '/usr/bin/sudo /usr/sbin/service /usr/sbin/nginx restart',
require => File['/etc/nginx/sites-available/default']
}
