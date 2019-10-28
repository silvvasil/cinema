"""
core].py
"""

import requests as re
from bs4 import BeautifulSoup


class CinemaParser:
    """
    Cinema parser
    """
    def __init__(self, city='msk'):
        """

        :param city:town
        """
        self.city = city
        self.url = "http" \
                   "s://" + city + ".subscity.ru"
        self.content = ""

    def extract_raw_content(self):
        """

        :return:html
        """
        response = re.get(url=self.url)
        self.content = response.text

    def print_raw_content(self):
        """

        :return:print html
        """
        soup = BeautifulSoup(self.content, 'html.parser')
        print(soup.prettify())

    def get_film_list(self):
        """

        :return: film list
        """
        soup = BeautifulSoup(self.content, 'html.parser')
        found_teg = soup.find_all('a', {"class": "underdashed"})[6:-30]
        film_list = []
        for i, element in enumerate(found_teg):
            element = str(element)
            if i % 5 == 0:
                film_list.append(str(str(element.split('>')[1])[:-3]))
        return film_list


CINEMA = CinemaParser('msk')
CINEMA.extract_raw_content()
CINEMA.print_raw_content()
print(CINEMA.get_film_list())
