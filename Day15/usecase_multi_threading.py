'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping 
Web scraping often involves making numerous network requests to 
fetch web pages. These are I/O-bound because they spend a lot of 
time waiting for responses from servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently.
'''

'''
https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/
'''

import threading
import requests
from bs4 import BeautifulSoup

urls=[
'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")
    
threads=[]

for url in urls:
    thred=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thred)
    thred.start()
    
for thread in threads:
    thred.join() 
    
print("All web pages fetched")