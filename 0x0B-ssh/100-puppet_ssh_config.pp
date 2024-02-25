# ssh(1) obtains configuration data from the following sources in the following order:
#   1.   command-line options
#   2.   user's configuration file (~/.ssh/config)
#   3.   system-wide configuration file (/etc/ssh/ssh_config)

$file_content = "Host *
\tIdentityFile ~/.ssh/school
\tPasswordAuthentication no
\tSendEnv LANG LC_*
\tHashKnownHosts yes
\tGSSAPIAuthentication yes
"

file { 'create ssh config file':
path    => '/etc/ssh/ssh_config',
ensure  => present,
content => $file_content,
require => File['/etc/ssh']
}
