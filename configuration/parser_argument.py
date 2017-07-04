import argparse


class ParserArgument:
    def __init__(self):
        self._arg_parse = argparse.ArgumentParser(description="Bot Telegram",
                                                  epilog="Starter to create a bot Telegram with the less code possible")
        self._arg_parse.add_argument("--token", nargs=1, type=str, help="Token give by the Bot Father", dest='token')
        self._arg_parse.add_argument("--config_file", nargs=1, type=str, help="Configuration file for the bot", dest='config_file')
        self._arg_parse.add_argument("--version", "-v", action="version", version="0.0.0")
        self._args = self._arg_parse.parse_args()

    @property
    def token(self):
        return self._args.token if self._args.token is not None else ""

    @property
    def config_file(self):
        return self._args.config_file if self._args.config_file is not None else ""
