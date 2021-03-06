#!/usr/bin/env python3
from re import A
import urllib3, json, sys, argparse

# Parse script arguments
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URL to json file")
args = parser.parse_args()

# Set default url to read JSON data.
url = 'http://34.123.72.107/data.json'

# Use script named params to assign URL passed by --url named param(arg)
if args.url:
    url = args.url


http = urllib3.PoolManager()

# Send GET request to url
resp = http.request('GET', url)

# Het request response status code
respStatus = resp.status

if respStatus != 200:
    print('Error: Invalid response code !')
    sys.exit("Exit")

# Response == 200
jsonData = resp.data.decode('utf-8')

print(jsonData)

data = json.loads(jsonData)


under = 0
over = 0
for server, cpuUsage in data.items():
    if cpuUsage < 50:
        under += 1
    else:
        over += 1

resultDict = {"under": under, "over": over}

print(resultDict)