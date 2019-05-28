import os
from configparser import ConfigParser

_current_file_path = os.path.abspath(__file__)

_utils_package_path = os.path.dirname(_current_file_path)
project_path = os.path.normpath(os.path.join(_utils_package_path, os.pardir))
_default_config_folder_path = os.path.join(project_path, 'cfg/')


def load_configuration(name, section='DEFAULT', config_folder_path=_default_config_folder_path):
    config = ConfigParser()
    config_file_path = os.path.join(config_folder_path, name)
    config.read(config_file_path)
    section = config[section]

    return section
