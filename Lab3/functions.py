import random

insults=['payaso', 'impresentable', 'ignorante', 'desgraciado']

def add_insult(insult):
    insults.append(insult)
    return ' '

def get_insults():
    return list(insults)

def insultme():
    return random.choice(insults)
