# using puppet to create a file /tmp/school with content "I love Puppet"
file={ '/tmp/school':
  ensure  => file,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => www-data,
  group   => www-data
}

