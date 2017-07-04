import os


def get_env(key: str):
    try:
        return os.environ[key]
    except KeyError:
        return ""


def get_env_config_file():
    return get_env("TELEGRAM_CONFIG_FILE")
