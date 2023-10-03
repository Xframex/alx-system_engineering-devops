#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit(1)
end

pattern = /hbt{2,5}n/
input_string = ARGV[0]
matches = input_string.scan(pattern)
puts matches.join
