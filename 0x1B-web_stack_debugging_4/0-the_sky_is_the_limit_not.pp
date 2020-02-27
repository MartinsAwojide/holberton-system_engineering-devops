# Script that fix the limits for the request of nginx
exec { 'Debugging4':
  command  => "echo 'ULIMIT=\"-n 4096\"' > /etc/default/nginx",
  provider => shell,
}

-> exec { 'restart':
  command  => 'service nginx restart',
  provider => shell,
}
