#!/usr/bin/env python3
from ServerObj import Server
import random, argparse,json

# Parse script arguments
parser = argparse.ArgumentParser()
parser.add_argument("--servernum", help="Number (int) of servers to be generated")
args = parser.parse_args()

# Set default number of servers to be genarated
serverNum = 10

# Use script named params to assign URL passed by --url named param(arg)
if args.servernum:
    serverNum = int(args.servernum)


# Empty servers dictionary
serversDictionary = { }

# Populate servers dictionary
for i in range(serverNum):
    cpuUsage = random.randint(0, 100)
    currServer = Server("server" + str(i), cpuUsage)
    
    serversDictionary[currServer.getName()]  = currServer.getCpuUsage()

# Dictionary as JSON output
js = json.dumps(serversDictionary)

with open('/var/www/html/data.json', 'w') as outfile:
    outfile.write(js)