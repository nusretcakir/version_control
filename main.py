import requests
from bs4 import BeautifulSoup
import time

def version_test():

    #programin yerel surumu
    with open("v.txt","r") as f:
        version = int(f.read())  
    
    #programin net surumu
    url = "https://raw.githubusercontent.com/nusretcakir/version_control/master/v.txt"
    new_version = int(str((BeautifulSoup(requests.get(url).content,"html.parser"))))
    
    if version != new_version:
        print("program guncel değil") 
        exit()

def ana():

    version_test()

    while True:
        print("Programın v1 sürümünü kullanmaktasınız.")
        time.sleep(2)
ana()





