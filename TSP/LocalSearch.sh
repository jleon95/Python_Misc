#!/bin/bash

for filename in data/*.tsp; do

    python src/TSPLocalSearch.py "$filename" 3 10000 > solutions/LocalSearch/"${filename#data/}"

done 