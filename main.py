from os import getcwd
from os.path import join as path_join
from configuration.basic_configuration import BasicConfiguration
from admin.admin import admin

config_file = BasicConfiguration(path_join(getcwd(), './resources/configuration.ini'))
admin_grp = admin(config_file.admins)


def main():
    from app import App
    app = App(config_file.token)
    app.run()


if __name__ == '__main__':
    main()
