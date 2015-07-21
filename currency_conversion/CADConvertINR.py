#!/usr/local/bin/python3

"""
Script to get the current conversion from CAD to INR from xe.com
"""

# requests is needed for importing the content from the webpage and bs4 for parsing it
import requests, bs4

# Import the converter object from the XE website
XERes = requests.get('http://www.xe.com/currencyconverter/convert.cgi?template=pca-new&Amount=1&From=CAD&To=INR')
XERes.raise_for_status()

# Make a soup object out of the Response object received from above, so we can parse it.
XESoup = bs4.BeautifulSoup(XERes.text, "html.parser")
ConvStr = XESoup.select('table span h2')[2].getText()
print(ConvStr)
