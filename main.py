import requests
from bs4 import BeautifulSoup

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

    for i in range(5):
        print("v2")

ana()





