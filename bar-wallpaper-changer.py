#!/usr/bin/python3

################################################################################
# imports                                                                      #
################################################################################

import os
import sys
import time
import json
import logging
import requests
from bs4 import BeautifulSoup


__version__ = '0.0.2'
__author__ = 'arxel-sc'


################################################################################
# init logging                                                                 #
################################################################################

formatting = '%(asctime)s: %(levelname)s: in %(module)s: %(message)s'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format=formatting)
logging.debug(LOG_FILE)
logging.info(f'Starting version {__version__}')


def get_website_info():
    requests.packages.urllib3.disable_warnings()
    sitecontent = requests.get("https://www.marksalzburg.at", verify=False)
    soup = BeautifulSoup(sitecontent.text, "html.parser")
    events = soup.find_all("div", "event-content")
    return events


def download_images():
    for event in events:
        image_url = event.find('img')['src']
        image_name = image_url.split('/')[-1]
        new_pics.append(image_name)
        if image_name not in old_pics:
            with open(os.path.join(PIC_DIR, image_name), 'wb') as pic:
                r = requests.get(image_url, allow_redirects=True, verify=False)
                pic.write(r.content)
                logging.info(f'Downloaded {image_name} to pics folder!')


def remove_old_pics(old, new):
    '''
    Remove old pictures from the pic-directory to not clutter it.
    '''
    for element in old:
        if element not in new:
            os.remove(os.path.join(PIC_DIR, element))
            logging.info(f'Removed {element} from pics folder!')


def set_wallpaper():
    # os.system(f'feh --bg-scale {PIC_DIR}/{element}')
    os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{PIC_DIR}/{element}")
    os.system("gesettings set org.gnome.desktop.background picture-options 'scaled'")
    logging.info(f'Set new Wallpaper: {element}')
    time.sleep(rotation_time)


def main():
    try:
        while True:
            number_of_pics = len(new_pics)
            for n, element in enumerate(new_pics):
                if n + 1 == number_of_pics:
                    break
                else:
                    set_wallpaper()
    except Exception as err:
        logging.error(err)
    finally:
        logging.critical('Shutting down')
        sys.exit()


if __name__ == '__main__':

    HOME_FOLDER = os.path.expanduser('~')
    SHARE_DIR = os.path.join(HOME_FOLDER, '.local', 'share', 'bar-wallpaper-changer')
    LOG_DIR = os.path.join(SHARE_DIR, 'logs')
    PIC_DIR = os.path.join(SHARE_DIR, 'pics')
    LOG_FILE = os.path.join(LOG_DIR, 'bar-wallpaper-changer.log')

    try:
        if not os.path.isdir(SHARE_DIR):
            os.mkdir(SHARE_DIR)
    except Exception as err:
        os.mkdirs(SHARE_DIR)
    if not os.path.isdir(LOG_DIR):
        os.mkdir(LOG_DIR)
    if not os.path.isdir(PIC_DIR):
        os.mkdir(PIC_DIR)

    old_pics = os.listdir(PIC_DIR)
    new_pics = []

    remove_old_pics(old_pics, new_pics)
    main()

