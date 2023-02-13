#!/bin/sh 
wc -w $1
grep -o '\w*' $1 | sort | uniq -c | sort -nr | head 
echo 'Ingrese el numero N de palaras'
read number
grep -o '\w*' $names | sort | uniq -c | sort -nr | head -n $number

