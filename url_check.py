#!/usr/bin/python
import requests,sys

def request(url):
   header={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.bing.com/",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0"}
   session = requests.Session()
   try:
      resp = session.get(url, headers=header, verify=False, timeout=5)
      if resp.url == url:
         print "==>"+resp.url 
   except Exception as e:
      pass



if  __name__ =='__main__':
   print "[*] Starting ..."
   links=open(sys.argv[1]).readlines()
   for link in links:
      url=link.strip()
      request(url)
