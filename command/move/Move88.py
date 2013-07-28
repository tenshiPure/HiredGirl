#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Move88(Base):

	category = 'move'

	commandName = '88'
	description = '画面２ 上半分'

	env = 'ryowin'

	if env ==  'ryowin':
		left   = 1920
		top    = 0 
		width  = 1920
		height = 540

	elif env ==  'nebigwin':
		left   = 1920
		top    = 0 
		width  = 1920
		height = 540

	elif env ==  'nebigmac':
		left   = 1920
		top    = 0 
		width  = 1920
		height = 540

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self):
		scriptName = 'move'
		script = self.createScriptPath(scriptName)

		self.executeMoveScript(script)
