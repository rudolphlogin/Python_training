'''Provides random greetings'''
import random
sayings = ('Hello','Hi','Hey','Alo','Aloha')

def greet():
	return random.choice(sayings)