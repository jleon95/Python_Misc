#!/bin/bash

for filename in data/*.tsp; do

    python src/TSPGenetic.py "$filename" 3 250 40 > solutions/Genetic/"${filename#data/}"

done 