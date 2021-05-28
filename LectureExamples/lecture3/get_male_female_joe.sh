cat /home/meyers/DataScienceTools/pydata-book-2nd-edition/datasets/babynames/*txt | sort > all_baby_lines.csv
grep -i Joe, all_baby_lines.csv > all_joe_lines.csv
grep ',F,' all_joe_lines.csv | cut -d, -f1,3 > female_joe.csv
grep -v ',F,' all_joe_lines.csv | cut -d, -f1,3 > male_joe.csv
