from os import getcwd
from configuration.configuration import Configuration
from admin.admin import admin

config_file = Configuration(getcwd())
admin_grp = admin(config_file.admins)


def main():
    from app import App
    app = App(config_file.token)
    app.run()


if __name__ == '__main__':
    main()
