from os.path import join as path_join
from os.path import exists
from os.path import isfile
from utils.get_env import get_env_config_file


def get_config_file(path: str, file_rescue: list):
    file_to_check = [path_join(path, get_env_config_file()), get_env_config_file()]
    for f in file_rescue:
        file_to_check.append(path_join(path, f))
        file_to_check.append(f)
    for file in file_to_check:
        if isfile(file) and exists(file):
            return file
    raise FileNotFoundError("Configuration file not found. Please create an environment variable TELEGRAM_CONFIG_FILE with the path file or put an argument to this file")
