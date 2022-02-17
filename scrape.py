import requests

html_text = requests.get('https://www.mit.edu/~ecprice/wordlist.10000').text
with open("words.txt", "w") as f:
    f.write(html_text)
