import requests
import webbrowser


class Films:
    def __init__(self, menu='https://kinogo.biz', fentezi='https://kinogo.biz/fentezi', vestern='https://kinogo.biz/vestern/', triller='https://kinogo.biz/triller/', horror='https://kinogo.biz/uzhasy/', action='https://kinogo.biz/boevik/', comedy='https://kinogo.biz/komedia/'):
        self.menu = menu
        self.fentezi = fentezi
        self.vestern = vestern
        self.triller = triller
        self.horror = horror
        self.action = action
        self.comedy = comedy

    def start_fentezi(self):
        return webbrowser.open(self.fentezi)

    def start_vestern(self):
        webbrowser.open(self.vestern)

    def start_triller(self):
        webbrowser.open(self.triller)

    def start_horror(self):
        webbrowser.open(self.horror)

    def start_action(self):
        webbrowser.open(self.action)

    def start_comedy(self):
        webbrowser.open(self.comedy)


def get_film_menu(self):
    return webbrowser.open(self.menu)


def set_film_menu(self, value):
    self.menu = value
    res = requests.get(value)
    print(res)
    if res.status_code == requests.codes.ok:
        with open('kinogo.biz', 'wb') as value:
            value.write(res.content)


class Fentezi(Films):
    def __init__(self):
        super().__init__()

    def get_film_fentezi(self):
        return webbrowser.open(self.fentezi)

    def set_film_fentezi(self, value):
        self.menu = value
        res = requests.get(value)
        print(res)
        if res.status_code == requests.codes.ok:
            with open('kinogo.biz/fentezi', 'wb') as value:
                value.write(res.content)


class Vestern(Films):
    def __init__(self):
        super().__init__()

    def get_film_vestern(self):
        return webbrowser.open(self.vestern)

    def set_film_vestern(self, value):
        self.menu = value
        res = requests.get(value)
        print(res)
        if res.status_code == requests.codes.ok:
            with open('kinogo.biz/vestern/', 'wb') as value:
                value.write(res.content)


class Triller(Films):
    def __init__(self):
        super().__init__()

    def get_film_triller(self):
        return webbrowser.open(self.triller)

    def set_film_triller(self, value):
        self.menu = value
        res = requests.get(value)
        print(res)
        if res.status_code == requests.codes.ok:
            with open('kinogo.biz/triller/', 'wb') as value:
                value.write(res.content)


class Horror(Films):
    def __init__(self):
        super().__init__()

    def get_film_horror(self):
        return webbrowser.open(self.horror)

    def set_film_horror(self, value):
        self.menu = value
        res = requests.get(value)
        print(res)
        if res.status_code == requests.codes.ok:
            with open('https://kinogo.biz/uzhasy/', 'wb') as value:
                value.write(res.content)


class Action(Films):
    def __init__(self):
        super().__init__()

    def get_film_action(self):
        return webbrowser.open(self.action)

    def set_film_action(self, value):
        self.menu = value
        res = requests.get(value)
        print(res)
        if res.status_code == requests.codes.ok:
            with open('https://kinogo.biz/boevik/', 'wb') as value:
                value.write(res.content)


class Comedy(Films):
    def __init__(self):
        super().__init__()

    def get_film_comedy(self):
        return webbrowser.open(self.comedy)

    def set_film_comedy(self, value):
        self.menu = value
        res = requests.get(value)
        print(res)
        if res.status_code == requests.codes.ok:
            with open('https://kinogo.biz/komedia/', 'wb') as value:
                value.write(res.content)














