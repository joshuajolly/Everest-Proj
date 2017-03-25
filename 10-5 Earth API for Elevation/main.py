print("Hello, World!")

#just 9 values to start with

import simplejson

#0,0 is 27.988,86.925
longitude = 86.925
latitude = 27.988

import googlemaps as g

client = g.Client(key="AIzaSyA2Y1ipBGS_cmokDXrSDB_sMOljMHbsdxw")

import time

req_vals = []



for i in range(-50,51):
	#print(longitude + (-50 * 0.001), ",", (latitude + (i * 0.001)), "and",
	#	longitude + (50 * 0.001), ",", (latitude + (i * 0.001)))
	req_vals.append([(latitude + (50 * 0.001), longitude + (i * 0.001)),
		(latitude + (-50 * 0.001), (longitude + (i * 0.001)))])

#print(req_vals)

result = []

for ans in req_vals:
	result.append(g.elevation.elevation_along_path(client,ans, 100))
	

print("finished")

#for i in req_vals:
#result.append(g.elevation.elevation(client, (2,2)))

print(dir(g.elevation.elevation_along_path))

#result.append(g.elevation.elevation_along_path(client,[(1,1),(2,2)], 100))

#	print(i)
#	time.sleep(10)

f = open("output.csv", "w+")

i=0
for answer in result:
	#print(int(round((req_vals[i][0] - latitude) * 1000, 5)), "\t", int(round((req_vals[i][1] - longitude) * 1000, 5)), "\t",answer['elevation'])
	for responses in answer:
		outstr = str(responses['location']['lat']) + "," + str(responses['location']['lng']) + "," + str(responses['elevation'])
		print(outstr)
		f.write(outstr + "\n")
f.close()
