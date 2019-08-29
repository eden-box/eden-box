#!/usr/bin/env python3.7

import yaml
import logging


def get_config(resource):
    """
    Loads all the required configuration from a binary string of a yaml file
    :param: binary string resource
    :return: dict to use as configuration, empty if unable to load configuration
    """
    config = {}

    try:
        config = yaml.safe_load(resource)
    except yaml.YAMLError:
        logging.getLogger(__name__).warning("Unable to access configuration file.")

    return config


def save_config(file_path, config):
    """
    Save a configuration to a file
    :param file_path: to configuration file
    :param config: configuration to save
    """

    with open(file_path, 'w') as f:
        try:
            yaml.safe_dump(config, f, default_flow_style=False)
        except yaml.YAMLError:
            logging.getLogger(__name__).critical("Unable to update configuration file.")
