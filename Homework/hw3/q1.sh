sed -e 's/, /__/g' P00000001-ALL.csv | cut -d, -f3,10 | grep -e '-[0-9]' > negative_amounts.csv
sed -e 's/, /__/g' P00000001-ALL.csv | cut -d, -f3,10 | grep -v -e '-[0-9]' > positive_amounts.csv