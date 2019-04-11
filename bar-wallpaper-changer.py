#!/usr/bin/env python3

"""
Usage: bwc-cli.py [-h] [-v | -q] (--config FILE | --path PATH)

This program uses either a configuration file or a specified path to display a
set of pictures on a screen. Can easily be used to display ads using feh as the
program to display. Using a YAML configuration file is the preferred way.

Arguments:
  -c --config FILE  Use this file as configuration written in YAML.
  -p --path PATH    Use this path for pictures with default or specifies
                    options
Options:
  -h --help     Display the help message.
  -v --verbose  Show debug output.
  -q --quite    Show no output.
"""

import yaml
import docopt
import subprocess


def read_config(config_file):
    with open(config_file) as config:
        cfg = yaml.safe_load(config)
    print(cfg)
    return 0


if __name__ == "__main__":
    args = docopt.docopt(__doc__)
    if args["--config"] != None:
        print("yes")
    print("auch yes")
