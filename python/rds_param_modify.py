#!/usr/bin/env python3

import boto3
import sys

pg_name = sys.argv[1]

conn = boto3.client('rds')
conn.modify_db_parameter_group(
    DBParameterGroupName=pg_name,
    Parameters=[
        {
            'ParameterName': 'work_mem',
            'ParameterValue': '{DBInstanceClassMemory/204801}',
            'ApplyMethod': 'immediate'
        },
    ]
)
