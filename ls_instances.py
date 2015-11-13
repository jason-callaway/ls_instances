#!/usr/bin/env python

import json
import sys

data = json.load(sys.stdin)

for reservation in data['Reservations']:
	for instance in reservation['Instances']:
		id = instance['InstanceId']
		state = instance['State']['Name']
		tags = {}
		if instance.get('Tags'):
			for tag in instance['Tags']:
				tags[tag['Key']] = tag['Value']
		print id + ' ' + state + ' ' + ', '.join(['%s=%s' % (k, str(v)) for (k, v) in tags.items()])

