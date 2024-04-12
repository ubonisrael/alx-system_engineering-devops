# Fixes bug in wordpress website

exec { 'fix bug':
provider => shell,
command  => "sed -i 's/phpp/php/' var/www/html/wp-settings.php"
}
