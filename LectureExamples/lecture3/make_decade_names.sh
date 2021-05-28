#! /bin/bash

for dec in {188..201}
do
    mkdir ${dec}0s
    cp babynames/yob${dec}* ${dec}0s/
done
