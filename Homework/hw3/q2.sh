mkdir -p Male
mkdir -p Female

target_dir="../../Datasets/babynames"
# target_dir="/home/meyers/DataScienceTools/pydata-book-2nd-edition/datasets/babynames"

for file in ${target_dir}/*
do
    if grep -q ',M,' ${file}
    then
        grep ',M,' ${file} > Male/$(basename ${file})
    fi
    if grep -q ',F,' ${file}
    then
        grep ',F,' ${file} > Female/$(basename ${file})
    fi
done