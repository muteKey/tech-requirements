from bs4 import BeautifulSoup
import requests

def get_vacation_links():
    with open("seed.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        links = soup.body.find_all('a', attrs={'class':'vt'})

        results = []
        
        for link in links:
            href = link["href"]
            results.append(href)

        return results


def get_job_descriptions(links):
    results = []
    for link in links:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.body.find('div', attrs={'class':'text b-typo vacancy-section'}).get_text('\n', strip=True)
        if text is not None:
            text = cleanup_text(text)
            results.append(text)
            results.append("\n-----------------------")
    return results


def cleanup_text(text):
    return text.strip().replace("● ", "").replace(" "," ").replace(" "," ").replace(" "," ").replace("• ", " ").replace(" ", "").replace("• ", "").replace("​", "")


links = get_vacation_links()
descriptions = get_job_descriptions(links)

results = open("results-android.txt", "w")
text = "\n".join(descriptions)

results.write(text)
results.close()
