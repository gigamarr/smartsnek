import os
import urllib.request
from bs4 import BeautifulSoup
from utils import catch_404, get_attr_or_empty

class Dictionary:
    base_url = "https://www.dictionary.com/browse/"

    @catch_404
    def get_and_soupify(self, word):
        response = urllib.request.urlopen(self.base_url + word).read()
        soup = BeautifulSoup(response, 'html.parser')
        return soup

class Word(Dictionary):
    write_path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, word, count=None):
        self.soup = super().get_and_soupify(word)
        self.count = count

    @property
    @get_attr_or_empty
    def word(self):
        return self.soup.find('h1').text

    @property
    @get_attr_or_empty
    def pronunciation(self):
        return self.soup.find('span', class_='pron-spell-content').text

    @property
    @get_attr_or_empty
    def word_type(self):
        return self.soup.find('span', class_='luna-pos').text.replace(',', '')

    @property
    @get_attr_or_empty
    def definitions(self):
        return ["{}. {}\n".format(index, value.get_text(strip=True)) for index, value in enumerate(self.soup.find_all('div', class_='e1q3nk1v3'), start=1)]

    def write(self, data):
        with open(self.write_path+'/output', 'a+') as f:
            f.write(data)
    @property
    def representation(self):
        return "{} -- {} - {} \n\n{}".format(self.word, self.pronunciation, self.word_type, "".join(self.definitions[0:self.count]))

    def __str__(self):
        return self.word
