from stat import filemode
from bs4 import BeautifulSoup
import requests
import json
import re
from pwn import *
from multiprocessing import Pool
import wikipedia

# find actors in IMDB
def getACTORS(html):
    actors = re.findall(r'> (.*)\n</a>.*</td>\n.*ellipsis', html.decode())
    return actors
	
def getHTML(url):
	
	response = requests.get(url)
	return BeautifulSoup(response.content,'html.parser')	
	
def getURL(input):
    if input[0] == 't' and input[1] == 't':
        html = getHTML('https://www.imdb.com/title/'+input+'/')
        
    else:
        html = getHTML('https://www.google.co.in/search?q='+input+'IMDB')
        # print(html)
        cite = re.findall(r'(https://www.imdb.com/title/tt\d*/)', html.decode())[0]
        print(cite)

        html = getHTML(cite+'fullcredits')
    return getACTORS(html)


# find actors in wikipedia
def find_actors(film):
    wiki_name = wikipedia.search(film)[0]
    content = wikipedia.WikipediaPage(wiki_name).html()
    names = re.findall(r'title="(.*)">(.*)</a> as', content)
    # print(names[0][0])
    record = []
    for i in range(len(names)):
        if names[i][0] == names[i][1]:
            record.append(names[i][0])

    return record

def attack():
    conn = remote('challenge.ctf.games', 31260)
    for i in range(100):
        print('time: ',i)
        try:
            sen = conn.recvuntil(b'*')
            print(sen)
            if i != 0:
                sen = sen_file
            film_name = re.findall(r'> (.*)\n', sen.decode())[0]
            print(film_name)
            actors1 = getURL(film_name)
            film_name_no_date = re.findall(r'(.*) \(', film_name)[0]
            print(film_name_no_date+ ' film')
            actors2 = find_actors(film_name_no_date+ ' film')
            actors = []
            for a in actors1:
                if a in actors2:
                    actors.append(a)
                if len(actors) == 5:
                    break
            if len(actors) != 5:
                actors = actors1[:5]

            str_actors = '; '.join(actors)
            print(str_actors)
            conn.send(str_actors.encode())

            sen = conn.recvline()
            print(sen)
            sen_file = conn.recvline()
            print(sen_file)
        except EOFError as e:
            print(e)
            break
    while 1:
        try:
            print("break")
            sen = conn.recvline()
            print(sen)
        except EOFError as e:
            print(e)
            break


if __name__ == '__main__':
    attack()
