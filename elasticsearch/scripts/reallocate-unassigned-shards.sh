#!/bin/bash

set -e

NODE_ID="ax1rxXI"

indices=$(curl -s localhost:9200/_cat/shards?h=index,shard,prirep,state,unassigned.reason | grep UNASSIGNED | cut -f1 -d ' ' | sort | uniq)

for index in $indices; do
  curl -XPOST -H 'Content-Type: application/json' 'localhost:9200/_cluster/reroute' -d @- << _EOF_
{
  "commands" : [{ 
    "allocate_stale_primary" : { 
      "index" : "$index", 
      "shard" : 0, 
      "node" : "$NODE_ID",
      "accept_data_loss" : true
    } 
  }
]}
_EOF_

done
