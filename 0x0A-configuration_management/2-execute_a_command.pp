# A manifest that executes a command
exec { 'kill process':
command => '/usr/bin/pkill killmenow'
}
