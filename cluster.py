#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import combinations
import csv
import hierarchical
import os
import time

def importData(filename):
    duplicate_pairs = []

    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            duplicate_pairs.append(((cleanId(row['id1']), cleanId(row['id2'])), float(row['level'])))

    return duplicate_pairs

def cleanId(id_string):
    return int(id_string.replace('CC', ''))

def print_csv(output_file, clustered_dupes) :
  with open(output_file,"w") as f :
    writer = csv.writer(f)
    writer.writerow(["cluster_id", "id"])
    
    for group_id, cluster in enumerate(clustered_dupes, 1) :
      for candidate in sorted(cluster) :
        print group_id, candidate
        # row = orig_data[candidate]
        row = [group_id, candidate]
        writer.writerow(row)

t0 = time.time()

input_file = 'data/northwestern_match_examples.csv'
output_file = 'data/northwestern_clusters.csv'
cluster_threshold = 0.3

duplicates = importData(input_file)
#print duplicates

clusters = hierarchical.cluster(duplicates, cluster_threshold)
#print clusters

print '# duplicate sets'
print len(clusters)
print_csv(output_file, clusters)

print 'ran in ', time.time() - t0, 'seconds'
