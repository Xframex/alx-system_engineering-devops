#!/usr/bin/env ruby
log_entry = ARGV[0]

# Regular expression pattern to extract the desired values
pattern = /\[from:([^\]]+)\] \[to:([^\]]+)\] \[flags:([^\]]+)\]/
# Use the pattern to extract values from the log entry
data_pattern = log_entry.match(pattern)

if data_pattern
  sender = data_pattern[1]
  receiver = data_pattern[2]
  flags = data_pattern[3]
  
  # Print the extracted values
  puts "#{sender},#{receiver},#{flags}"
else
  puts "No match found in the log entry."
end
