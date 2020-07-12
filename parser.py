from bs4 import BeautifulSoup as BS
import requests
from time import sleep

url = 'https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

while True:
    response = requests.get(url, headers = header)
    soup = BS(response.content, 'html.parser')

    par = open('parser.txt', 'a')

    for el in soup:
        par.write(str(el))

    par.close()

    par = open('parser.txt', 'r')

    file = par.readlines()
    line = file[11]

    for i in range(len(line)):
        if line[i] == 'w':
            l = i;
            url_photo = 'https://'
            while (line[l] != '>'):
                url_photo = url_photo + line[l]
                l = l + 1
                if (line[l-1] == 'p') and (line[l] == 'g'):
                    break
            url_photo = url_photo + line[l]
            break

    par.close()

    url_file = open('url.txt', 'w')

    url_file.write(url_photo)

    url_file.close()

    sleep(3600)
