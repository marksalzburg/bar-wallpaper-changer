import os
import logging


def remove_old_pics(old, new):
    '''
    Remove old pictures from the pic-directory to not clutter it.
    '''
    for element in old:
        if element not in new:
            os.remove(os.path.join(PIC_DIR, element))
            logging.info(f'Removed {element} from pics folder!')

