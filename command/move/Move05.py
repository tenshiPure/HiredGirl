#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Move05(Base):

	category = 'move'

	commandName = '5'
	description = '画面１ 全画面'

	env = 'ryowin'

	if env ==  'ryowin':
		left   = 0
		top    = 0 
		width  = 1920
		height = 1080

	elif env ==  'nebigwin':
		left   = 0
		top    = 0 
		width  = 1920
		height = 1080

	elif env ==  'nebigmac':
		left   = 0
		top    = 0 
		width  = 1920
		height = 1080

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self):
		scriptName = 'move'
		script = self.createScriptPath(scriptName)

		self.executeMoveScript(script)
