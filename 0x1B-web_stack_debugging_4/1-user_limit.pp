# raises the file limit for user holberton

exec { 'raise hard limit' :
provider => shell,
command  => "sed -i 's/holberton hard nofile 5/holberton hard nofile 500/' /etc/security/limits.conf"
}

exec { 'raise soft limit' :
provider => shell,
command  => "sed -i 's/holberton soft nofile 4/holberton soft nofile 400/' /etc/security/limits.conf",
require  => Exec['raise hard limit']
}
