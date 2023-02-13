#!\bin\bash
wc -w $1 $2
grep -o '\w*' $1 $2 | sort | uniq -c | sort -nr | head
grep -o '\w*' $1 $2 | sort | uniq -c | sort -nr | head -n $3
