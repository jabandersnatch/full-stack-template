#!/bin/sh
grep -o '\w*' $1 | sort | uniq -c | sort -nr
