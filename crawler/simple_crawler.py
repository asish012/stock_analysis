import bs4 as bs
import requests
import re


class SimpleCrawler:

    def __init__(self, ticker):
        url = self._get_msn_url(ticker) #'https://www.msn.com/en-us/money/stockdetails/financials/nys-v/fi-a256cw'
        # self.soup = self._get_soup(url)

    @staticmethod
    def _get_soup(url):
        sauce = requests.get(url)
        return bs.BeautifulSoup(sauce.content, 'lxml')

    def _get_msn_url(self, ticker):
        url = 'https://www.google.com/search?q=msn+money+stock:{}'.format(ticker)
        soup = self._get_soup(url)

        regex = r"https://www.msn.com/en-us/money/stockdetails/.*-" + re.escape(ticker) + r"/fi-[a-zA-Z0-9]{6}"
        msn_url = soup.find_all('a', attrs={'href': re.compile(regex)})
        print(msn_url)
        return ''

    def get_eps(self):
        # all_financial_columns = soup.find_all('li', {'class': 'left-align column0 financials-columns'})
        eps_anchor = self.soup.find_all('p', text='Diluted EPS from Continuing Operations')
        eps_segment = eps_anchor[0].parent.parent

        for p in eps_segment.find_all('p', {'class': 'truncated-string'}):
            print(p.get_text())


        # print(eps_segment)


if __name__ == '__main__':

    crawler = SimpleCrawler('googl')
    # crawler.get_eps()
