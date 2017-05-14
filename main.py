from app import App


def main():
    app = App('./resources/configuration.ini')
    app.run()


if __name__ == '__main__':
    main()
