import requests
from bs4 import BeautifulSoup       # allows us to use HTML and modify data (clean up)
import pprint

res = requests.get('https://news.ycombinator.com/news')          # basically a website callout
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')      # convers HTML from a string to object
soup2 = BeautifulSoup(res2.text, 'html.parser')

# print(soup.body.contents)       # only takes the body and contents from HTML file
# print(soup.find_all('div'))
# print(soup.title)               # can use any of these keywords to locate data

links = soup.select('.storylink')       # inspect page element to get desired class information
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

all_links = links + links2
all_subtext = subtext + subtext2
# print(votes[0].get('id'))

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)      # cant use sorted on dictionaries, so must give a key
# lambda syntax tells sorted method to sort by the number of votes, reverse makes it highest votes to lowest

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()                    # returns the link titles
        href = item.get('href', None)             # returns the href links
        vote = subtext[idx]. select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))       # convert string to int and replace the word points
            if points > 99:
                hn.append({'title': title, 'link':href, 'votes': points})        # appends the titles and links to a dictionary
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(all_links, all_subtext))