# Raises ulimit

exec { 'raise limit' :
provider => shell,
command  => "sed -i 's/15/4096/' /etc/default/nginx"
}

exec { 'restart nginx' :
provider => shell,
command  => 'sudo service nginx restart',
require  => Exec['raise limit']
}
