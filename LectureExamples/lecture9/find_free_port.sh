#!/usr/bin/bash

while true :; do 
    PORT=$(shuf -i 10000-49151 -n 1)
    if netstat -4tuln | grep LISTEN | grep $PORT; then 
        echo "Port $PORT is already in use. Skipping."
    else
        echo "Port $PORT is available for use."
        break
    fi
done
