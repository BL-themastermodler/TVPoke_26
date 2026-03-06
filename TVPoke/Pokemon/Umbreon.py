from TVPoke.BaseClasses.PokeTypes import Psychic
from TVPoke.BaseClasses.Move import Move

class Espeon(Psychic):
    def __init__(self):
        moves = [
            Move("Quick attack", "NORMAL", 40),
            Move("Swift", "NORMAL", 60),
            Move("Snarl", "DARK", 55),
            Move("ark pulse", "DARK", 80)
        ]
        super().__init__("Umbreon", 95, moves, "./TVPoke/Pokemon/imgs/Umbreon.png")