import pandas as pd
import requests
from bs4 import BeautifulSoup

#URL
page = requests.get('https://tbinternet.ohchr.org/_layouts/15/treatybodyexternal/SessionDetails1.aspx?SessionID=1380&Lang=en')
#soup is the object that is a module picked up in Beautiful soup#
soup = BeautifulSoup(page.content, 'html.parser')
#finding the id in the source code to pick up and look at#
treatyName = soup.find(id='DeltaPlaceHolderMain')
#print(treatyName)

#items = treatyName.find_all(class_='rgRow InnerItemStyle    rgSelectedRow')

#items = treatyName.find_all(class_='country')
#country = [item.find(class_='country').get_text() for item in items]


#brings it in hyref from the top panels of the un page
items = treatyName.find_all(class_='rgRow InnerItemStyle')

print(items[0])
#print(items[0].find(class_='country').get_text())

#print(items[2].find(class_='country').get_text())

#creates a table of data
#unitedNations_stuff = pd.DataFrame(
#{
#    'country': country,
#    'short_descriptions': short_descriptions
#    'temperatures': temperatures,
 #   })
#print(unitedNations_stuff)

#unitedNations_stuff.to_csv()

#ms-belltown-anonspacer
#ms-belltown-anonspacer
#class="rgRow InnerItemStyle    rgSelectedRow"

#treatyName = soup.find(id='DeltaPlaceHolderMain')


#Finds all the a tags in the source code#
#print(soup.find_all ('a'))

#Ids from the download documents from the website#
#<a id="ctl00_PlaceHolderMain_dgGenDocs_ctl00_ctl04_MoreDocs" title="View document" href="https://tbinternet.ohchr.org/_layouts/15/treatybodyexternal/Download.aspx?symbolno=CEDAW%2fC%2f75%2f1&amp;Lang=en" target="_blank" style="text-decoration:underline;">View document</a>
#<a id="ctl00_PlaceHolderMain_dgGenDocs_ctl00_ctl06_MoreDocs" title="View document" href="https://tbinternet.ohchr.org/_layouts/15/treatybodyexternal/Download.aspx?symbolno=INT%2fCEDAW%2fPOW%2f75%2f29095&amp;Lang=en" target="_blank" style="text-decoration:underline;">View document</a>
#<span id="ctl00_PlaceHolderMain_tdTreatyName" class="SessionSubtitle">CEDAW - Convention on the Elimination of All Forms of Discrimination against Women</span>