#kills a process

exec { 'kill_process':
  command => '/usr/bin/pkill -f killmenow',
  path    => '/usr/bin:/usr/sbin:/bin',
}
