#!/usr/local/bin/python3

"""
Downloads all the XKCD comics - ignores the invalid ones
"""

# requests is needed for importing the content from the webpages, os for OS specific modules and bs4 for parsing the pages
import requests, os, bs4

#starting url
url = 'http://xkcd.com'
#Store comics in ./xkcd_comics
os.makedirs('xkcd_comics', exist_ok=True)

while not url.endswith('#'):
	
	#Download the webpage - the initial page is always the latest comic
	print ('Downloading page %s...' % url )
	XKCDRes = requests.get(url)
	XKCDRes.raise_for_status()

	#Make a soup object from the page
	XKCDSoup = bs4.BeautifulSoup(XKCDRes.text, "html.parser")

	#Find the URL for the comic image
	comicElem = XKCDSoup.select('#comic img')

	#Download only if comic img url exists
	if comicElem == []:
		print('Could not find the comic image.')
	else:
		#For eg: //imgs.xkcd.com/comics/barrel_cropped_(1).jpg
		comicUrl = comicElem[0].get('src').replace('//', 'http://')
		
		#Only download comics from the imgs url
		if 'imgs.xkcd.com' in comicUrl:
			#Download the image
			print('Downloading image %s' % comicUrl)
			res = requests.get(comicUrl)
			res.raise_for_status()

			#Save the image file to ./xkcd_comics if it doesnt already exist
			imageFileName = os.path.join('xkcd_comics', os.path.basename(comicUrl))
			if os.path.isfile(imageFileName):
				print ('Image already exists..Skipping.')
			else:
				imageFile = open(imageFileName, 'wb')
				for chunk in res.iter_content(100000):
					imageFile.write(chunk)
				imageFile.close()
		else:
			print('Not a valid comic.')

	#Get the PREV button's URL
	prevLink = XKCDSoup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')
	print('---')

#All image files have been downloaded.
print('Done.')






