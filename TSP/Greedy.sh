#!/bin/bash

for filename in data/*.tsp; do

    python src/TSPGreedy.py "$filename" > solutions/Greedy/"${filename#data/}"

done 