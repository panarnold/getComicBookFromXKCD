#! python
# downloadxkcd.py - download all cartoons published on XKCD website
# X 2020 Arnold Cytrowski

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):

    print('Downloading the page %s' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    comic_element = soup.select('#comic img')
    if comic_element == []:
        print('There is not any comics')
    else:
        comic_url = 'http:%s' % comic_element[0].get('src')

        print('Downloading comic %s' % comic_url)
        res = requests.get(comic_url)
        res.raise_for_status()

        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('aaand it\'s done')

