import time

class Shortcuts:
    def __init__(self, remote):
        self.remote = remote

    # power
    def power(self):
        self.remote.send_key('KEY_POWER')

    # menu
    def home(self):
        self.remote.send_key('KEY_HOME')

    def menu(self):
        self.remote.send_key('KEY_MENU')

    def source(self):
        self.remote.send_key('KEY_SOURCE')

    def guide(self):
        self.remote.send_key('KEY_GUIDE')

    def tools(self):
        self.remote.send_key('KEY_TOOLS')

    def info(self):
        self.remote.send_key('KEY_INFO')

    # navigation
    def up(self, delay=None):
        self.remote.send_key('KEY_UP', delay)

    def down(self, delay=None):
        self.remote.send_key('KEY_DOWN', delay)

    def left(self, delay=None):
        self.remote.send_key('KEY_LEFT', delay)

    def right(self, delay=None):
        self.remote.send_key('KEY_RIGHT', delay)

    def enter(self, delay=None):
        self.remote.send_key('KEY_ENTER', delay)

    def back(self, delay=None):
        self.remote.send_key('KEY_RETURN', delay)

    # channel
    def channel_list(self):
        self.remote.send_key('KEY_CH_LIST')

    def digit(self, d):
        self.remote.send_key('KEY_' + d)

    def channel_up(self):
        self.remote.send_key('KEY_CHUP')

    def channel_down(self):
        self.remote.send_key('KEY_CHDOWN')

    # volume
    def volume_up(self, amount=1):
        for _ in range(amount):
            self.remote.send_key('KEY_VOLUP', 0.30)

    def volume_down(self, amount=1):
        for _ in range(amount):
            self.remote.send_key('KEY_VOLDOWN', 0.30)

    def mute(self):
        self.remote.send_key('KEY_MUTE')

    # extra
    def red(self):
        self.remote.send_key('KEY_RED')

    def green(self):
        self.remote.send_key('KEY_GREEN')

    def yellow(self):
        self.remote.send_key('KEY_YELLOW')

    def blue(self):
        self.remote.send_key('KEY_BLUE')
    
    # apps
    def youtube(self):
        self.remote.start_app("111299001912")

    def plex(self):
        self.remote.start_app("3201512006963")

    def emanual(self):
        self.remote.start_app("20182100010")

    def gallery(self):
        self.remote.start_app("3201710015037")

    def apple_tv(self):
        self.remote.start_app("3201807016597")

    def televizor(self):
        self.remote.start_app("3201412000606")

    def media_station_x(self):
        self.remote.start_app("3201801015538")

    def internet(self):
        self.remote.start_app("org.tizen.browser")

    def netflix(self):
        self.remote.start_app("11101200001")

    def facebook_watch(self):
        self.remote.start_app("11091000000")

    def google_play_movies(self):
        self.remote.start_app("3201601007250")

    def prime_video(self):
        self.remote.start_app("3201512006785")

    def kinopoisk(self):
        self.remote.start_app("111399000037")

    def ivi(self):
        self.remote.start_app("111199000746")

    def tvzavr(self):
        self.remote.start_app("3201506003168")

    def amediateka(self):
        self.remote.start_app("111399002017")

    def start_movies(self):
        self.remote.start_app("3201611011182")

    def megogo(self):
        self.remote.start_app("3201505002589")

    def more_tv(self):
        self.remote.start_app("111299002103")

    def okko(self):
        self.remote.start_app("3201506002941")

    def privacychoices(self):
        self.remote.start_app("3201909019271")

    def yandex(self):
        self.remote.start_app("3201802015794")

    def samsung_club(self):
        self.remote.start_app("3201805016309")

    def kion(self):
        self.remote.start_app("3201908018954")

    def wink(self):
        self.remote.start_app("3201710014965")

    def spotify(self):
        self.remote.start_app("3201606009684")

    def twitch(self):
        self.remote.start_app("2ulZzjRf8f.SmartTV")