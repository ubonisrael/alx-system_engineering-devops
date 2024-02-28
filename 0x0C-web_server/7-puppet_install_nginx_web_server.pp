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

package { 'nginx':
ensure  => installed,
require => Exec['update server']
}

file { '/etc/nginx/sites-available/default':
ensure  => file,
content => $server_config,
notify => Service['nginx']
}

service { 'nginx':
ensure  => running,
enable  => true,
require => Package['nginx']
}

file { '/var/www/html/index.nginx-debian.html':
ensure  => present,
content => 'Hello World!'
}

file { '/var/www/html/404.html':
ensure  => present,
content => "Ceci n'est pas une page"
}
