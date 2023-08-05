#!/usr/bin/env ruby

phone_number = ARGV[0]
pattern = /^\d{10}$/

if phone_number =~ pattern
  puts phone_number
end
