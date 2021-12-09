readarray -t a < input.txt

count=0

for n in `seq 1 ${#a[@]}`; do
    if [ ${a[$(($n-1))]} -le ${a[$n]} ]; then
        ((count=count+1))
    fi
done

echo $count