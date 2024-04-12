# Fixes bug in wordpress website

exec { 'fix bug':
provider => shell,
command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
path     => '/usr/local/bin/:/bin/'
}
