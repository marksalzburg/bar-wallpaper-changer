#!/usr/bin/env python3

import os
import logging
import bwc_methods.core


__version__ = "0.1.0"
__author__ = "arxel-sc"


LOG_DIR = os.path.join(os.getcwd(), "logs")
PIC_DIR = os.path.join(os.getcwd(), "pics")
LOG_FILE = os.path.join(LOG_DIR, "bar-wallpaper-changer.log")


if __name__ == "__main__":

    formatting = "%(asctime)s: %(levelname)s: in %(module)s: %(message)s"
    logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG,
                        format=formatting)
    logging.debug(LOG_FILE)
    logging.info(f"Starting version {__version__}")

    # parse arguments
    # read config

    bwc_methods.core.main(PIC_DIR)

