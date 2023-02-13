#!/bin/bash
grep -o '\w*' $1 | sort | uniq -c | sort -nr | head
