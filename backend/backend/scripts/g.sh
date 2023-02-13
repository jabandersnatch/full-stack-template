#!/bin/sh
grep -H -w -c 'the' $@ | sort -r -t : -k 2,2
wc -w $@ | sort -nr | head -n 1
