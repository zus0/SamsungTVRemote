import os
import json
import ssl
import time
import base64
import websocket
from .shortcuts import Shortcuts
from .actions import Actions

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class SamsungTVRemote:
    def __init__(self, ip, name) -> None:
        self.name = self._encode_name(name)
        self.token = self._get_token()
        self.connection = False

        self.ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
        self.url = f'wss://{ip}:8002/api/v2/channels/samsung.remote.control?name={self.name}&token={self.token}'

    def connect(self):
        self.ws.connect(self.url)
        response = self.read_response()
        if response['event'] != "ms.channel.connect":
            self.close()
            exit("Unable to connect!")
        print("Connected!")
        
        if response.get('data'):
            self.connection = True
            if response.get('data').get('token') != None:
                self._store_token(response.get('data').get('token'))
    
    def close(self):
        self.ws.close()
        self.connection = False
        print("Connection closed.")


    def start_app(self, app_id):
        return self.send({
            'method': 'ms.channel.emit',
            'params': {
                'event': 'ed.apps.launch',
                'to': 'host',
                'data': {
                    # 'action_type': 'NATIVE_LAUNCH' or 'DEEP_LINK'
                    'action_type': 'DEEP_LINK',
                    'appId': app_id,
                    'metaTag': ''
                }
            }
        })
    
    def send_key(self, key, keypress_delay = 0.1): #TODO keypress delay
        self.send({
            "method": "ms.remote.control",
            "params": {
                "Cmd": "Click",
                "DataOfCmd": key,
                "Option": "false",
                "TypeOfRemote": "SendRemoteKey"
            }
        })
        time.sleep(keypress_delay)
    
    def get_apps(self):
        self.send({
            'method': 'ms.channel.emit',
            'params': {
                'event': 'ed.installedApp.get',
                'to': 'host'
            }
        })

    def send(self, command):
        self.ws.send(json.dumps(command))
    

    def shortcuts(self):
        return Shortcuts(self)
    
    def actions(self):
        return Actions(self)

    def read_response(self):
        resp = self.ws.recv()
        resp = json.loads(resp)

        ignored_events = ['ms.remote.touchDisable', 'ed.edenTV.update', 'ms.remote.touchEnable']

        if resp['event'] in ignored_events:
            resp = self.read_response()
        return resp
    
    def _store_token(self, token):
        with open(__location__ + '/token.txt', 'w') as token_file:
            token_file.write(token)

    def _get_token(self):
        try:
            with open(__location__ + '/token.txt') as token_file:
                return token_file.readline()
        except:
            return ""

    @staticmethod
    def _encode_name(string):
        return base64.b64encode(string.encode()).decode("utf-8")
