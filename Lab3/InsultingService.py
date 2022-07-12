import random

class InsultingService:
    def __init__(self):
        self.insults = set()
    
    def add_insult(self, insult):
        self.insults.add(insult)
        return ' '

    def get_insults(self):
        return list(self.insults)

    def insultme(self):
        return list(self.insults)[random.randrange(0, len(self.insults))]

insultingService = InsultingService()