import remote
import time

rm = remote.SamsungTVRemote('192.168.1.206', "Python Remote")
actions = rm.actions()
rm.connect()

# rm.send_key("KEY_SOURCE")
rm.start_app("2ulZzjRf8f.SmartTV")
time.sleep(5)
actions.hdmi(1)