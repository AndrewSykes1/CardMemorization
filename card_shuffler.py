from os import listdir
from os.path import isfile, join
import os
import random
from pathlib import Path
import shutil

deck_of_cards = r'C:\Users\drews\SZvsWorkspace\PersonalProjects\MessingAbout\card_memorization\deck_of_cards'

[f.unlink() for f in Path(deck_of_cards).glob("*") if f.is_file()] 


cards = [f for f in listdir(deck_of_cards) if isfile(join(deck_of_cards, f))]
random.shuffle(cards)

os.chdir(deck_of_cards)

ticker = 0
for filename in os.listdir(deck_of_cards):
    ticker += 1
    os.rename(filename, f'{ticker}.png')

# Does not work yet

