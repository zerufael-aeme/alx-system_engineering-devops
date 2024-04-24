# Kills a process named killmenow

exec { 'pkill -f killmenow':
  command => 'pkill -f killmenow',
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}
