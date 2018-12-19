#!/usr/bin/env python3.7

import yaml
import logging


def get_config(file_path):
    """
    Loads all the required configuration from a file
    :return: dict to use as configuration, empty if unable to load configuration
    """
    config = {}

    with open(file_path, 'r') as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError:
            logging.getLogger(__name__).critical("Unable to access configuration file.")

    return config
