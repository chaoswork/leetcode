#!/usr/bin/env bash

# Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.

# You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)
# 
# You may also assume each line in the text file must not contain leading or trailing white spaces.
# 
# For example, assume that file.txt has the following content:
# 
# 987-123-4567
# 123 456 7890
# (123) 456-7890
# Your script should output the following valid phone numbers:
# 987-123-4567
# (123) 456-7890

grep -P "^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$" file.txt

# Correct Solution

# Solution 1 (sed)
# 
# sed -nr ‘/^([0-9]{3}-){2}[0-9]{4}$|^([0-9]{3}) [0-9]{3}-[0-9]{4}$/p’ file.txt
# sed does not support \d in regular expression
# It is necessary to use “sed -r (support extended regular expression)” so that we can use {n}.
# 
# Solution 2 (grep)
# 
# cat file.txt | grep -E ‘^([0-9]{3}-){2}[0-9]{4}$|^([0-9]{3}) [0-9]{3}-[0-9]{4}$’
# grep should be used along with -E to support extended regular expression
# 
# Solution 3 (awk)
# 
# awk –posix ‘/^([0-9]{3}-){2}[0-9]{4}|\([0−9]3\)[0−9]3−[0−9]4/{print $0}’ file.txt
# –posix is added to support

# When using regular expression, take care about whether it (awk, sed or grep) supports extended regular expression. It is safe to enable it once we want to use regular expresion
# 
# sed -r ‘/pattern/p’ filename
# awk –posix ‘/pattern/{action}’ filename
# cat filename | grep -E ‘pattern
