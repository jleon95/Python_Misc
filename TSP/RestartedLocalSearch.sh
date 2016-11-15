#!/bin/bash

for filename in data/*.tsp; do

    python src/TSPRestartedLocalSearch.py "$filename" 3 10000 10 > solutions/RestartedLocalSearch/"${filename#data/}"

done 