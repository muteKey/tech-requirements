from base_grabber import BaseGrabber
import requests
from bs4 import BeautifulSoup

class DjinniGrabber(BaseGrabber):

    def __init__(self, in_file_name, out_file_name, delimeter, keyword, number_of_pages):
        super().__init__(in_file_name, out_file_name, delimeter)
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        self.keyword = keyword
        self.number_of_pages = number_of_pages

    def __get_all_links(self):
        links = []
        for page in range(1, self.number_of_pages + 1):
            result = self.__get_detail_links(page)
            links.extend(result)
        return links
        
    def __get_detail_links(self, page):
        seed_url = f"https://djinni.co/jobs/?primary_keyword={self.keyword}" if page == 1 else f"https://djinni.co/jobs/?primary_keyword={self.keyword}&page={page}"
        response = requests.get(seed_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        profile_links = []
        
        for path in soup.body.find_all('a', attrs={'class':'profile'}):
            if path.get('href') is not None:
                link = "https://djinni.co" + path.get('href')
                profile_links.append(link)
        return profile_links
    
    def process(self):
        links = self.__get_all_links()
        descriptions = []

        for link in links:
            response = requests.get(link, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.body.find('div', attrs={'class':'profile-page-section'}).get_text('\n', strip=True)
            description = self.cleanup_text(content)
            descriptions.append(description)
            descriptions.append(self.delimeter)

        return descriptions
