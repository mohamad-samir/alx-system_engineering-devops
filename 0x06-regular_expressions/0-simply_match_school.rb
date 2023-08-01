#!/usr/bin/env ruby
# This script accepts one argument and pass it to a regular expression matching method

# Import the OptionParser class
require 'optparse'

# Initialize a new instance of OptionParser
options = OptionParser.new do |opts|
  # Define the option
  opts.on("-i", "--input INPUT", "Input string") do |input|
    # Perform the regular expression match
    matches = input.scan(/School/)
    # Print the matches
    puts matches.join
  end
end

# Parse the command-line options
options.parse!
