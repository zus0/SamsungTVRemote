import remote

rm = remote.SamsungTVRemote('192.168.1.206', "Python Remote")
rm.connect()

shortcuts = rm.shortcuts()
actions = rm.actions()
# setup finished

actions.pic_mode("light")
# actions.hdmi(1)