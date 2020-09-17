import os
import logging
import requests
from bs4 import BeautifulSoup


def get_website_info():
    requests.packages.urllib3.disable_warnings()
    sitecontent = requests.get("https://www.marksalzburg.at", verify=False)
    soup = BeautifulSoup(sitecontent.text, "html.parser")
    events = soup.find_all("div", "event-content")
    return events


def download_images(events, PIC_DIR):
    new_pics = []
    for event in events:
        image_url = event.find('img')['src']
        image_name = image_url.split('/')[-1]
        new_pics.append(image_name)
        if image_name not in old_pics:
            with open(os.path.join(PIC_DIR, image_name), 'wb') as pic:
                r = requests.get(image_url, allow_redirects=True, verify=False)
                pic.write(r.content)
                logging.info(f'Downloaded {image_name} to pics folder!')
    return new_pics


if __name__ == '__main__':
    pass

