import csv
import sys
from bs4 import BeautifulSoup
import sys
import os
from os import listdir


maxInt = sys.maxsize

while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/2)
with open("media_resource.tab", "r", encoding="utf8") as f:
    reader = csv.reader(f, delimiter="\t")
    next(reader)
    ctr =0
    for level,row in enumerate(reader):
        (identifier, taxon_ID, type, format, CVterm,\
            title,description,furtherInformationURL,language,\
                UsageTerms, Owner) = row
        
        if not "Brief Summary" in title:
            continue
        
        soup = BeautifulSoup(description, features="html.parser")
        for script in soup(["script", "style"]):
            script.extract() 
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        with open(f"extracted\\{title.split(':')[0]}.txt", 'w', encoding="utf8") as ext:
            ext.write(text)
        
