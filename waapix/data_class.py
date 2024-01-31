from enum import Enum


class TransportObject:
    default_game_obj = 18446744073709551614

    def __init__(self, w_obj: str, game_obj: int = -1, transport_id: int = -1):
        self.w_obj = w_obj
        self.game_obj = game_obj if game_obj != -1 else self.default_game_obj
        self.id = transport_id

    def __str__(self):
        return {
            'object': self.w_obj,
            'gameObject': self.game_obj,
            'transport': self.id
        }

    def as_args(self):
        return {
            'object': self.w_obj,
            'gameObject': self.game_obj,
        }


class TransportAction(Enum):
    Play = 'play'
    Stop = 'stop'
    Pause = 'pause'
    PlayStop = 'playStop'
    PlayDirectly = 'playDirectly'


class TransportState(Enum):
    Playing = 'playing'
    Stopped = 'stopped'
    Paused = 'paused'

