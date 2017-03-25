print("Hello, World!")

f = open("output.txt", "r")

inp = f.readlines()

f.close()

print(len(inp))

f = open("finished.obj", "w+")

f.write(
		"# Blender v2.77 (sub 0) OBJ File: ''\n"+
		"# www.blender.org\n"+
		"mtllib untitled1.mtl\n"+
		"o LevMesh\n"
	)

import re



for elem in inp:
	if (len(elem) < 3):
		break
	tmp = elem.strip().replace("   "," ").replace("  "," ")
	tmp = tmp.split(" ")
	print(tmp)
	f.write("v " + tmp[0] + " " + tmp[1] + " " + tmp[2] + "\n")

f.write(
		"vn 0.0000 -1.0000 0.0000\n"+
		"usemtl Material\n"+
		"s off"
	)

f.close()
