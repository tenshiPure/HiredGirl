#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Move44(Base):

	category = 'move'

	commandName = '44'
	description = '画面２ 左半分'

	env = 'ryowin'

	if env ==  'ryowin':
		left   = 1920
		top    = 0 
		width  = 960
		height = 1080

	elif env ==  'nebigwin':
		left   = 1920
		top    = 0 
		width  = 960
		height = 1080

	elif env ==  'nebigmac':
		left   = 1920
		top    = 0 
		width  = 960
		height = 1080

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self):
		scriptName = 'move'
		script = self.createScriptPath(scriptName)

		self.executeMoveScript(script)
