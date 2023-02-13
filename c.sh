#!/bin/sh
echo "Ingrese el numero N de palabras"
read number
grep -o '\w*' reut2-000.sgm | sort | uniq -c | sort -nr | head -n $number
