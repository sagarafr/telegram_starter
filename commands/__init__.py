from telegram.ext import Updater
from telegram.ext import CommandHandler
from copy import deepcopy
import pkgutil
import inspect


class Command(object):
    _functions = dict()
    _tmp = dict()

    def __init__(self, pass_args=False, pass_update_queue=False,
                 pass_job_queue=False, pass_user_data=False,
                 pass_chat_data=False):
        self._tmp = {"pass_args": pass_args,
                     "pass_update_queue": pass_update_queue,
                     "pass_job_queue": pass_job_queue,
                     "pass_user_data": pass_user_data,
                     "pass_chat_data": pass_chat_data}
        print(self._tmp)

    def __call__(self, f, *args, **kwargs):
        self._functions[f.__name__] = (f, deepcopy(self._tmp))
        print(self._functions[f.__name__])

        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper

    def init_dispatcher(self, updater: Updater):
        dispatcher = updater.dispatcher
        for cmd in self._functions:
            tuple_function = self._functions[cmd]
            command_function = tuple_function[0]
            command_args = tuple_function[1]
            dispatcher.add_handler(CommandHandler(cmd, command_function, pass_args=command_args["pass_args"],
                                                  pass_update_queue=command_args["pass_update_queue"],
                                                  pass_job_queue=command_args["pass_job_queue"],
                                                  pass_user_data=command_args["pass_user_data"],
                                                  pass_chat_data=command_args["pass_chat_data"]))

__all__ = []

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)

    for name, value in inspect.getmembers(module):
        if name.startswith('__'):
            continue

        globals()[name] = value
        __all__.append(name)
