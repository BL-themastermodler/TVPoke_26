from TVPoke.BaseClasses.PokeTypes import Dark
from TVPoke.BaseClasses.Move import Move

yes = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

class Umbreon(Dark):
    def __init__(self):
        moves = [
            Move("Quick attack", "NORMAL", 40),
            Move("Swift", "NORMAL", 60),
            Move("Snarl", "DARK", 55),
            Move("ark pulse", "DARK", 80)
        ]
        super().__init__("Umbreon", yes, moves, "./TVPoke/Pokemon/imgs/Umbreon.png")