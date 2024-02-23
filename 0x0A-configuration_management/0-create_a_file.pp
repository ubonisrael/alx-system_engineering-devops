# This manifest creates a file /tmp/school
file { '/tmp/school':
path    => '/tmp/school',
content => 'I love Puppet',
group   => 'www-data',
owner   => 'www-data',
mode    => '0744'
}
