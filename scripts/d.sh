#!\bin\bash
grep -H -o '\w*' $1 | sort | uniq -c | sort -nr | head -n $2
