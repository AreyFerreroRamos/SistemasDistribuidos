import random

insults=[]

def add_insult(insult):
    insults.append(insult)
    return ' '

def get_insults():
    return list(insults)

def insultme():
    random.choice(insults)
