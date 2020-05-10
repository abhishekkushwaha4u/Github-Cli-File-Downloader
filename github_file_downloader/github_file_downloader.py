#!/usr/bin/python
import wget
import sys

try:
    url = sys.argv[1]
    url = url.replace('https://github.com/', "https://raw.githubusercontent.com/")
    url = url.replace("blob/", '')
    url = url.replace("%20", " ")

    print(url)
    try:
        file = wget.download(url)
    except Exception as e:
        print(e)

except Exception:
    print("Need a url to run")
