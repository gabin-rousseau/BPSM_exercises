##There are 100 people. 
wc -l people.txt 
##106 (-1 because of the header) // 100, the condition if(NF==7 && $1 != "" && $1 != "name")

#Question 2
##People around 30 y.o. or older satisfy the condition: 2024 - [birth_year] >= 30
## the year column is field $6
awk '(2024 - $6 >= 30)' people.txt | wc -l
#awk 'if(typeof($6)== number)(2024 - $6 >= 30)' people.txt | wc -l
##returned 99 
tail -n +2 people.txt | awk 'BEGIN{FS="\t";}{if(NF ==7 && 2024 - $6 >= 30){print $0;}}' | wc -l
#FIXED by removing the first line and forcing tab FS, result is 95 (easier to get by checking <= 1994 //90

#Question 3
#Starting with pattern Jan
perl -ne 'print if m/^Jan/g' people.txt
#Containing word Jan
perl -wlne 'print if/\bJan\b/' people.txt | wc -l

#Question 4
#get most frequent coutnries, Mozambique first ( and 5 empty fields? maybe counted elsewhere in the exercise)
awk -F '\t' '{if(NF == 7 && $1 != "name"){print $7;}}' people.txt | sort | uniq -c | sort -nr | head -1
awk -F '\t' '{if(NF ==7 && $7 == "Mozambique" && 2024 - $6 >= 50){x+=1}}END{print"There are",x,"people aged around 50 or older born in Mozambique."}' people.txt
#works to tell there is 1 person from Mozambique fitting the criteria, but this is overly verbose as it prints again for every line -fixed with END rule

#Question 5
#awk -F '\t' '/edu/ {print $2}' people.txt
cat people.txt | sort -t$'\t' -rk1 | sort -t$'\t' -rk7 | awk -F '\t' 'BEGIN{OFS="\t#####\t"} /\.edu/ {print $1,$7}'
