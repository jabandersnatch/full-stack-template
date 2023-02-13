#!/bin/bash
grep -o '\w*' reut2-000.sgm | sort | uniq -c | sort -nr | head -n $1
