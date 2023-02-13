#!\bin\bash
wc -w $1 $2 $3
grep -o '\w*' $1 $2 $3 | sort | uniq -c | sort -nr | head
grep -o '\w*' $1 $2 $3 | sort | uniq -c | sort -nr | head -n $4
