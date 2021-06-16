import remote

rm = remote.SamsungTVRemote('192.168.1.206', "Python Remote")
rm.connect()

shortcuts = rm.shortcuts()
actions = rm.actions()
# setup finished

shortcuts.twitch()
actions.pic_mode("light")

# run twitch and switch to bright mode (made for personal use obv)