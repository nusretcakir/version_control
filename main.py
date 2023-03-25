import requests

def version_test():
    pass


def ana():
    with open("v.txt","r") as f:
        version = f.read()


    for i in range(5):
        print(version)

version_test()
ana()