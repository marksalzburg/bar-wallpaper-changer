import logging
import requests

import web_core
import file_core
import image_core
import display_core


def main(args):

    # test internet connection
    logging.info("Testing internet connection")
    try:
        response = requests.get(args["testurl"], timeout=5)
        if response.status_code == 200:
            logging.info("testurl could be reached")
            response.raise_for_status()
    except requests.exceptions.RequestException as err:
        logging.error("OOps: Something Else", err)
    except requests.exceptions.HTTPError as errh:
        logging.error("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        logging.error("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        logging.error("Timeout Error:", errt)

    # remove old pictures
    # get website pictures
    # get NAS pictures
    # start main loop
    return 0


if __name__ == '__main__':
    args = {"testurl": "https://marksalzburg.at"}
    main(args)


###############################################################################
#    events = web_core.get_website_info()
#    new_pics = web_core.download_images(events, PIC_DIR)
#    return 0
###############################################################################
#    old_pics = os.listdir(PIC_DIR)
#    events = get_website_info()
#    new_pics = download_images(events, PIC_DIR)
#    remove_old_pics(old_pics, new_pics)
#    main(new_pics, PIC_DIR)
#    try:
#        while True:
#            number_of_pics = len(new_pics)
#            for n, element in enumerate(new_pics):
#                if n + 1 == number_of_pics:
#                    break
#                else:
#                    try:
#                        set_wallpaper(PIC_DIR, element)
#                    except Exception as err:
#                        logging.error(err)
#    except Exception as err:
#        logging.error(err)
#    finally:
#        logging.critical('Shutting down')
#        sys.exit()
###############################################################################
