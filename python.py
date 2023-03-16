import random

class exo1:
    def __init__(self):
        self.citations = ["“Cris de mouette, signe de tempête.”", "“Mieux vaut sagesse que richesse.”", "“À la Saint-Gaston, surveille tes bourgeons.”"]
    
    def phraseRandom(self):
        print(random.choice(self.citations))

phrase = exo1()
phrase.phraseRandom()
