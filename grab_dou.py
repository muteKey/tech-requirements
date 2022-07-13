from bs4 import BeautifulSoup
import requests
from base_grabber import BaseGrabber

class DouGrabber(BaseGrabber):
    def __get_vacation_links(self):
        with open(self.in_file) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            links = soup.body.find_all('a', attrs={'class':'vt'})

            results = []
            
            for link in links:
                href = link["href"]
                results.append(href)

            return results

    def __get_job_descriptions(self, links):
        results = []
        for link in links:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.body.find('div', attrs={'class':'text b-typo vacancy-section'}).get_text('\n', strip=True)
            if text is not None:
                text = self.__cleanup_text(text)
                results.append(text)
                results.append(self.delimeter)
        return results


    def __cleanup_text(self, text):
        return text.strip().replace("● ", "").replace(" "," ").replace(" "," ").replace(" "," ").replace("• ", " ").replace(" ", "").replace("• ", "").replace("​", "")

    
    def process(self):
        links = self.__get_vacation_links()
        descriptions = self.__get_job_descriptions(links)
        self.write_results(descriptions)
