#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Move99(Base):

	category = 'move'

	commandName = '99'
	description = '画面２ 右上'

	env = 'ryowin'

	if env ==  'ryowin':
		left   = 2880
		top    = 0 
		width  = 960
		height = 540

	elif env ==  'nebigwin':
		left   = 2880
		top    = 0 
		width  = 960
		height = 540

	elif env ==  'nebigmac':
		left   = 2880
		top    = 0 
		width  = 960
		height = 540

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self):
		scriptName = 'move'
		script = self.createScriptPath(scriptName)

		self.executeMoveScript(script)
