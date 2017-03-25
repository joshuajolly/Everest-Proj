print("Hello, World!")

from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

latitude = 27.988
longitude = 86.925

doc.asis(r'<?xml version="1.0" encoding="UTF-8"?>')
doc.asis(r'<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">')
inarr=(
	r'	<Style id="sn_ltblu-pushpin">',
	'		<IconStyle>',
	'		<scale>1.1</scale>',
	'		<Icon>',
	'			<href>http://maps.google.com/mapfiles/kml/pushpin/ltblu-pushpin.png</href>',
	'		</Icon>',
	'		<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>'
	'	</IconStyle>',
	'	<ListStyle>',
	'	</ListStyle>',
	'</Style>',
	'<StyleMap id="msn_ltblu-pushpin">',
	'	<Pair>',
	'		<key>normal</key>',
	'		<styleUrl>#sn_ltblu-pushpin</styleUrl>',
	'	</Pair>',
	'	<Pair>',
	'		<key>highlight</key>',
	'		<styleUrl>#sh_ltblu-pushpin</styleUrl>',
	'	</Pair>',
	'</StyleMap>',
	'<Style id="sh_ltblu-pushpin">',
	'	<IconStyle>',
	'		<scale>1.3</scale>',
	'		<Icon>',
	'			<href>http://maps.google.com/mapfiles/kml/pushpin/ltblu-pushpin.png</href>',
	'	</Icon>',
	'		<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>'
	'	</IconStyle>',
	'	<ListStyle>',
	'	</ListStyle>',
	'</Style>')

with tag("Document"):
	with tag("name"):
		text("North Col Lower.kmz")
	doc.asis(
	r'	<Style id="sn_ltblu-pushpin">',
	'		<IconStyle>',
	'		<scale>1.1</scale>',
	'		<Icon>',
	'			<href>http://maps.google.com/mapfiles/kml/pushpin/ltblu-pushpin.png</href>',
	'		</Icon>',
	'		<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>'
	'	</IconStyle>',
	'	<ListStyle>',
	'	</ListStyle>',
	'</Style>',
	'<StyleMap id="msn_ltblu-pushpin">',
	'	<Pair>',
	'		<key>normal</key>',
	'		<styleUrl>#sn_ltblu-pushpin</styleUrl>',
	'	</Pair>',
	'	<Pair>',
	'		<key>highlight</key>',
	'		<styleUrl>#sh_ltblu-pushpin</styleUrl>',
	'	</Pair>',
	'</StyleMap>',
	'<Style id="sh_ltblu-pushpin">',
	'	<IconStyle>',
	'		<scale>1.3</scale>',
	'		<Icon>',
	'			<href>http://maps.google.com/mapfiles/kml/pushpin/ltblu-pushpin.png</href>',
	'	</Icon>',
	'		<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>'
	'	</IconStyle>',
	'	<ListStyle>',
	'	</ListStyle>',
	'</Style>')
	with tag("Folder"):
		with tag("name"):
			text("North Col Lower")
		with tag("open"):
			text(1)
		for i in range(-5,6):
			for j in range(-5,6):
				with tag("Placemark"):
					with tag("name"):
						text(str(i) + ", " + str(j))
					with tag("LookAt"):
						with tag("gx:TimeSpan"):
							with tag("begin"):
								text("2016-10-29T19:23:47.753756031Z")
							with tag("end"):
								text("2016-10-29T19:23:47.953758597Z")
						with tag("gx:ViewerOptions"):
							with tag("gx:option", name = "historicalimagery"):
								pass
							with tag("gx:option", name = "sunlight"):
								pass
							with tag("gx:option", enabled = "0", name = "streetview"):
								pass
						with tag("longitude"): # important!
							text(str(longitude + (i * 0.0166666666666667)))
							#text("86.93668923957243")
						with tag("latitude"):
							text(str(latitude + (j * 0.0166666666666667)))
							#text("28.02133532907021")
						with tag("altitude"):
							text("0")
						with tag("heading"):
							text("-135.7661521779345")
						with tag("tilt"):
							text("62.20153741388337")
						with tag("range"):
							text("3715.435957350113")
						with tag("gx:altitudeMode"):
							text("relativeToSeaFloor")
					with tag("styleUrl"):
						text("#msn_ltblu-pushpin")
					with tag("Point"):
						with tag("gx:drawOrder"):
							text("1")
						with tag("coordinates"): # not entirely sure what this does
							text(str(longitude + (i * 0.0166666666666667)) + "," + str(latitude + (j * 0.0166666666666667)) + ",0")
doc.asis("</kml>")

result = indent(
	doc.getvalue(),
	indentation = ' '*4,
	newline = '\r'
)

f=open('doc.kml','w+')
f.write(result)
f.close()