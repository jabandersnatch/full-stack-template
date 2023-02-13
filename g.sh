#!/bin/sh
for f in $@; do
    grep -H -o '\w*' $f | sort | uniq -c | sort -nr | head -n 1
done
