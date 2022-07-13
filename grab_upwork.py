from bs4 import BeautifulSoup
from base_grabber import BaseGrabber

class UpworkGrabber(BaseGrabber):
    def process(self):
        text = self.__get_description()
        self.write_results(text)


    def __get_description(self):
        with open(self.in_file) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            links = soup.body.find_all('span', attrs={'data-test':'job-description-text'})
            results = []
            for link in links:
                text = link.get_text('\n', strip=True) + self.delimeter
                results.append(text)
            return "\n".join(results)


