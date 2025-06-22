# imports
import os
import random

# class hangman
class hangman:

	def _welcome_screen():


		os.system("clear")
		print("\n\n    welcome to the hang-man\n\n")
		_list_of_word=["Liopa","aparpale"]
		return random.choice(_list_of_word)


	def _world_underscore_(string:str):


		_under_scoreWorld=[]
		for i in range(len(string)):
			_under_scoreWorld.append("_")
		_under_scoreWorld_str="".join(_under_scoreWorld)
		return _under_scoreWorld_str


	def _validate_is_onechar():
			
			while True:

				_gess_char=input("dame un caracter para adivinar\nR:")
				if len(_gess_char) != 1:
					print("no puedes poner valores incorrecto, esto solo detecta un caracter\n solo uno.... intenta de nuevo")
					
				else:
					return _gess_char

	
	def replace_char_with_slicing(original_string, index, new_char):
		return original_string[:index] + new_char + original_string[index+1:]



	def _game_():


		#var
		_gess_world=hangman._welcome_screen()
		_under_scoreWorld=hangman._world_underscore_(_gess_world)
		_cnt_=len(_gess_world)
		_lives_= 3
		strikes=0
		print(f"valor a adivinar\n '{_gess_world}'\n     ","estos son los undesrcores...    \n     ",_under_scoreWorld)
		while True:
			print(f"tines {_lives_} vidas")
			_gess_char=hangman._validate_is_onechar()
			for i in range(len(_under_scoreWorld)):
				if _gess_world[i] == _gess_char:
					#_under_scoreWorld[i] =_gess_char
					_under_scoreWorld=hangman.replace_char_with_slicing(_under_scoreWorld,i,_gess_char)
					_cnt_ -=1
					print(_under_scoreWorld)	
				else:
					strikes += 1
					if strikes == len(_gess_world):
						strikes=0
						_lives_ -=0
				
				if _cnt_ == 0:
					print("....ACABOO...")
					return 0
				if _lives_ == 0:
					print("....ACABOO...")
					return 0
			



		
##test 
os.system("cls")
hangman._game_()
