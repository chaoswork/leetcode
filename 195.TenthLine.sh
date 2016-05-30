#!/usr/bin/env bash

# How would you print just the 10th line of a file?
# 
# For example, assume that file.txt has the following content:
# 
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10
# Your script should output the tenth line, which is:
# Line 10

awk 'FNR==10' file.txt

# Correct Solution
# 
# Solution 1 (sed)
# 
# sed -n '10p' file.txt
# 1
# 1
# Solution 2(awk)
# 
# awk 'if(NR==10){print $0}' file.txt
# 1
# 1
# Solution 3
# 
# tail -n+10 file.txt | head -n 1
# 1
# 1
# tail -n
# 
# -n, –lines=K Output the last K lines, instead of the default of the last 10; alternatively, use “-n +K” to output lines starting with the Kth.
# Keep in mind that -n+K, output lines starting with Kth
# 
# take-home message
# 
# awk, sed, tail can all solve this problem. These three commands are able to deal with txt editor.
# 
