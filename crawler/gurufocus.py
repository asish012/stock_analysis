from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from bs4 import BeautifulSoup

class GuruFocus:
    custom_search_url = 'https://www.gurufocus.com/industry_overview.php?industry=Medical-Devices'

    def __init__(self):

        # Start a WebDriver and load the page
        wd = webdriver.Firefox(executable_path='../driver/geckodriver/wires')
        wd.get(self.custom_search_url)

        # Wait for the dynamically loaded elements to show up And grab the page HTML source
        WebDriverWait(wd, 10)
        html_page = wd.page_source

        wd.quit()

        soup = BeautifulSoup(html_page, 'html.parser')

        print(soup.prettify())


if __name__ == '__main__':
    mobile_crawler = GuruFocus()
