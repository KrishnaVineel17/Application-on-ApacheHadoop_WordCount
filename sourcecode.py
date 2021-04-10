import urllib2
iiitdm = "https://iiitk.ac.in"
page = urllib2.urlopen(iiitdm)

with open('/home/vineel/Desktop/iiitDM', 'a') as f:
	f.writelines(page)
