import pygame, constants, util, gen

class Player:

	def __init__(self, num, playing):
	
		self.num = num
		self.score = 0
		self.playing = playing
		
		# state variables
		self.active = False
		self.buzzed = False
		
		# betting variables
		self.cur_bet = 0
		self.is_betting = False
		self.bet_set = False
		
		# check variables
		self.check_set = False
		
		# initialize surfaces
		self.blank_char_surface = gen.char_surface(num)
		self.char_surface = gen.char_surface(num)
		
		# load sound clips
		self.correct_sound = None
		self.incorrect_sound = constants.WRONG_SOUNDS[self.num - 1]
		
		# blit initial score
		self.add_to_score(0)
		
	def play_wrong(self): self.incorrect_sound.play()
	
	def play_right(self): self.correct_sound.play()
		
	def get_max_bet(self):
	
		# determine maximum bet from player score
		if self.score <= 1000: return 1000
		else: return self.score
		
	def setup_bet(self, final = False):
	
		if not final:
			self.cur_bet = self.get_max_bet
			self.is_betting = True
		else:
			self.cur_bet = self.score
			if self.score > 0: self.is_betting = True
			else: self.bet_set = True
			
		self.__update_char_surface(self.cur_bet)
	
	# ADD TO PLAYER BET, UPDATE SURFACE
	def add_to_bet(self):
	
		if (self.cur_bet + 100) <= self.score: self.cur_bet += 100	
		self.__update_char_surface(self.cur_bet)
	
	# SUB FROM PLAYER SCORE, UPDATE SURFACE
	def sub_from_bet(self):
	
		if (self.cur_bet - 100) >= 0: self.cur_bet -= 100
		self.__update_char_surface(self.cur_bet)
	
	# NEGATES POINTS AND CALLS add_to_score
	def sub_from_score(self, points):
	
		self.add_to_score(points * -1)
	
	# ADD TO PLAYER SCORE, UPDATE SURFACE
	def add_to_score(self, points):
	
		# add points to scores
		self.score += points
		
		self.__update_char_surface(self.score)
	
	def __update_char_surface(self, value):
	
		# determine display color
		if self.score >= 0: color = constants.WHITE
		else: color = constants.RED
	
		# update player surface
		self.char_surface.fill(constants.DARK_BLUE)
		self.char_surface.blit(self.blank_char_surface, (0,0))
		self.char_surface.blit(gen.text_surface(value, self.char_surface.get_width(), self.char_surface.get_height(), 30, color, "digital", constants.BLUE), (0, 70))
