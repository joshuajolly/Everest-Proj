print("Hello World")

f = open("input.csv")
_in = f.read()
f.close()

import csv

with open('input.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	
	i = 0
	for row in spamreader:
		#print(row)
		if i == 0:
			i+=1
			continue
		dat = row[0].split(",")
		#print("Name: ",dat[6])
		try:
			name = dat[6]
		except:
			name = ""

		try:
			if len(name) > 0:
				print("Name: ",dat[6])
				print(dat)
				print("X:",dat[17])
				print("Y:",dat[18])
				print("Z:",dat[19])
		except Exception as e:
			print(e)
			#pass
		#if i == 4:
		#	break
		i+=1

#print(dir(reader))

#print(reader.line_num)