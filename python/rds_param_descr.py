#!/usr/bin/env python3

import boto3
import sys
import json

pg_name = sys.argv[1]

conn = boto3.client('rds')
response = conn.describe_db_parameters(
    DBParameterGroupName=pg_name,
    MaxRecords=100,
    Marker='data',
)

print(json.dumps(response, indent=4, sort_keys=True))
