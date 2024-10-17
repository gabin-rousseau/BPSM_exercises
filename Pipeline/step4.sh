#!/usr/bin/bash
rm step4.log
touch step4.log

wc -l bedfiles/TriTrypDB-46_TcongolenseIL3000_2019.bed >> step4.log

cat bedfiles/TriTrypDB-46_TcongolenseIL3000_2019.bed | cut -f1 -s | uniq -c | wc -l >> step4.log
cat bedfiles/TriTrypDB-46_TcongolenseIL3000_2019.bed | cut -f4 -s | uniq -c | wc -l >> step4.log

cat bedfiles/TriTrypDB-46_TcongolenseIL3000_2019.bed | cut -f5 -s | uniq -c | sort -rn | head -n10 >> step4.log
