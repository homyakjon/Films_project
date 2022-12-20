import requests
import webbrowser


class Films:
    def __init__(self, menu='https://kinogo.biz', vestern='https://kinogo.biz/vestern/', triller='https://kinogo.biz/triller/', horror='https://kinogo.biz/uzhasy/', action='https://kinogo.biz/boevik/', comedy='https://kinogo.biz/komedia/'):
        self.menu = menu
        self.vestern = vestern
        self.triller = triller
        self.horror = horror
        self.action = action
        self.comedy = comedy

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

class Fentezi:
    def __init__(self, fentezi='https://kinogo.biz/fentezi'):
        self.fentezi = fentezi

    def start_fantasy(self):
        return webbrowser.open(self.fentezi)


class Vestern(Films):
    def __init__(self):
        super().__init__()

    def get_film_vestern(self):
        return webbrowser.open(self.vestern)


class Triller(Films):
    def __init__(self):
        super().__init__()

    def get_film_triller(self):
        return webbrowser.open(self.triller)


class Horror(Films):
    def __init__(self):
        super().__init__()

    def get_film_horror(self):
        return webbrowser.open(self.horror)


class Action(Films):
    def __init__(self):
        super().__init__()

    def get_film_action(self):
        return webbrowser.open(self.action)


class Comedy(Films):
    def __init__(self):
        super().__init__()

    def get_film_comedy(self):
        return webbrowser.open(self.comedy)


