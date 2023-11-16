# fix cuncurrent users number
exec {'fix':
  command => "sed -i 's/worker_processes 4;/worker_processes 7;/g' /etc/nginx/nginx.conf; sudo service nginx restart"
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
