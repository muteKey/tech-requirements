from bs4 import BeautifulSoup
import sys

def get_description(seed_file_name):
    with open(seed_file_name) as fp:
        print(seed_file_name)
        soup = BeautifulSoup(fp, 'html.parser')
        links = soup.body.find_all('span', attrs={'data-test':'job-description-text'})
        results = []
        for link in links:
            text = link.get_text('', strip=True) + "\n--------------------"
            results.append(text)
        return "\n".join(results)

def main_func(seed_file_name, out_file_name):
    text = get_description(seed_file_name)
    results = open(out_file_name, "w")

    results.write(text)
    results.close()

main_func(sys.argv[1], sys.argv[2])
