#!/usr/bin/env bash

# Given a text file file.txt, transpose its content.
# 
# You may assume that each row has the same number of columns and each field is separated by the ' ' character.
# 
# For example, if file.txt has the following content:
# 
# name age
# alice 21
# ryan 30
# Output the following:
# 
# name alice ryan
# age 21 30
# 
awk '{for(i=1;i<=NF;++i){if(i in a){a[i] = a[i]" "$i}else{a[i]=$i}};b=NF}END{for(i=1;i<=b;++i){print a[i]}}' file.txt

# It is easy to use arry in awk for this problem.
# 
# awk ‘{ if(NR==1){for(i=1;i<=NF;i++){arr[i]=$i}}
# 	  else{for(i=1;i<=NF;i++){arr[i]=arr[i]” “$i}} }
# END{for(i=1;i<=NF;i++){print arr[i]} }’ file.txt
# {} : concatenate each $i with corresponding arr[i]
# END{} : print arr
# 
