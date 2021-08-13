from threading import Thread

from consoles.sports import Basketball
from consoles.sports import Football
from consoles.sports import Volleyball
from consoles.sports import WaterPolo
from consoles.sports import WaterPoloDaktronics

from consoles import SerialConnection

import socketio

from ports import get_com_port

class ScoreKeeper:
    def __init__(self, sport: str) -> None:
        port = get_com_port()
        self.score = None # type: SerialConnection
        if sport == 'basketball':
            self.score = Basketball(port)
        elif sport == 'football':
            self.score = Football(port)
        elif sport == 'volleyball':
            self.score = Volleyball(port)
        elif sport == 'waterpolo':
            self.score = WaterPolo(port)
        elif sport == 'daktronicswaterpolo':
            self.score = WaterPoloDaktronics(port)

        self.score.on_update = self.updater
    
        self.client = socketio.Client()
        self.client_thread = Thread(target=self.socket_client)
        self.client_thread.start()
    
    def updater(self, game_state):
        if self.client.connected:
            self.client.emit('update', game_state)
            self.game_state = game_state
    
    def socket_client(self):
        self.client.connect('http://localhost:9876')
        self.client.wait()