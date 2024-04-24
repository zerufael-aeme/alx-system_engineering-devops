#Install flask / Version must be 2.1.0
exec { 'pip3 install flask':
  command => 'pip3 install Flask==2.1.0',
}
  
