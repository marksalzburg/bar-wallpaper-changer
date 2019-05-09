from . import web_core
from . import file_core
from . import image_core
from . import display_core


def main(PIC_DIR):

    print('here')
    return 0







    old_pics = os.listdir(PIC_DIR)
    events = get_website_info()
    new_pics = download_images(events, PIC_DIR)
    remove_old_pics(old_pics, new_pics)
    main(new_pics, PIC_DIR)
    try:
        while True:
            number_of_pics = len(new_pics)
            for n, element in enumerate(new_pics):
                if n + 1 == number_of_pics:
                    break
                else:
                    try:
                        set_wallpaper(PIC_DIR, element)
                    except Exception as err:
                        logging.error(err)
    except Exception as err:
        logging.error(err)
    finally:
        logging.critical('Shutting down')
        sys.exit()


if __name__ == '__main__':
    pass
