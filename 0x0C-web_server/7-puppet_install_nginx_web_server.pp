# Installs nginx on a server
exec { 'update server':
command => 'sudo apt-get update'
}

exec { 'change owner /var/www':
command => 'sudo chown -R "$USER":"$USER" /var/www'
}

exec { 'change owner /etc/nginx':
command => 'sudo chown -R "$USER":"$USER" /etc/nginx'
}

package { 'install nginx':
ensure  => installed,
name    => nginx,
require => Exec['update server']
}
