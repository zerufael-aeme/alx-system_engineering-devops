# Using Puppet, install flask from pip3.

package { 'install_flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}
