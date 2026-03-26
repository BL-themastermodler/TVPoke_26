from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (48, 0, 181))

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]

    def elementsToDisplay(self):
        self.elements = [] #new Image with a background (center 50 50 height/width 100/100)

        poke = self.trainers[0].pokemon[0]
        x = 25
        y = 15
        self.elements.append(Image((x, y), 20, 20, poke.img))
        poke = self.trainers[0].pokemon[1]
        x = 50
        y = 15
        self.elements.append(Image((x, y), 20, 20, poke.img))
        poke = self.trainers[0].pokemon[2]
        x = 75
        y = 15
        self.elements.append(Image((x, y), 20, 20, poke.img))
        poke = self.trainers[1].pokemon[0]
        x = 25
        y = 85
        self.elements.append(Image((x, y), 20, 20, poke.img))
        poke = self.trainers[1].pokemon[1]
        x = 50
        y = 85
        self.elements.append(Image((x, y), 20, 20, poke.img))
        poke = self.trainers[1].pokemon[2]
        x = 75
        y = 85
        self.elements.append(Image((x, y), 20, 20, poke.img))






