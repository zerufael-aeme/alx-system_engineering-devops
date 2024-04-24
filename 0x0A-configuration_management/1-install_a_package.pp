#Install flask / Version must be 2.1.0
exec { 'install_flask_2.1.0':
 command => 'pip3 install Flask==2.1.0',
 path    => ['/usr/bin/'],
 unless => 'pip3 show Flask | grep "Version: 2.1.0"',
}
  
