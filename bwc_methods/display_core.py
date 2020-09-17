import os
import time
import logging

def set_wallpaper(PIC_DIR, element, rotation_time=30):
    os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{PIC_DIR}/{element}")
    os.system("gesettings set org.gnome.desktop.background picture-options 'scaled'")
    logging.debug(f'Set new Wallpaper: {element}')
    time.sleep(rotation_time)


def display_diashow(PIC_DIR, rotation_time=30):

    for element in pic_list:
        pass
    return 0

