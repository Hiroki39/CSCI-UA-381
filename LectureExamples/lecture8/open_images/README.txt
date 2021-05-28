1) Get the first column of the csv file and remove duplicates
cut -f 1 -d , oidv6-train-annotations-bbox.csv | sed 's/"//g' | sort | uniq > all.ids
2) manually deleted "Image ID"
3)  remove probably ill-formed file names
     grep -v + all.ids > all.ids2 
4) put them in a random order
    sort -R all.ids2 > all.ids3
 5) pick a sample of 500 items
 head -500 all.ids3 > 500.ids
 6) add the prefix "train/" at the front of each filename
      sed 's/^/train\//' 500.ids > 500b.ids
      mv 500b.ids 500.ids
      python downloader.py 500.ids
      1 file could not be found -- `train/345760085172554`
      So there are only 499 .jpg files
 7) I randomly added one file to replace it:
      sort -R all.ids3 | head -1 | sed 's/^/train\//' > 1more.id
 8) I made sure it was not already in the previous list
     grep "041f63d06d538d2f" 500.ids
     yielded no result
 9) I got the remaining jpg file:
     python downloader.py 1more.id
 10) Display a sample of jpg files (from one directory up)
     ls open_images/*jpg |head -5 > 5_open_image.list
     python3 demo_group_for_N_seconds.py 5_open_image.list 10
     
     	     
