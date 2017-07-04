from configuration.parser_argument import ParserArgument
from configuration.basic_configuration import BasicConfiguration
from utils.get_config_file import get_config_file


class Configuration:
    def __init__(self, path):
        self._parser_arg = ParserArgument()
        # TODO put the parser arg here
        self._basic_configuration = BasicConfiguration(get_config_file(path, ['./resources/configuration.ini']))

    @property
    def token(self):
        return self._parser_arg.token if self._parser_arg.token != "" else self._basic_configuration.token

    @property
    def admins(self):
        return self._basic_configuration.admins

    @property
    def trust_admin_in_chan(self):
        return self._basic_configuration.trust_admin_in_chan
