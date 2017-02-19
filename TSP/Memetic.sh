#!/bin/bash

for filename in data/*.tsp; do

    python src/TSPMemetic.py "$filename" 3 250 40 > solutions/Memetic/"${filename#data/}"

done 