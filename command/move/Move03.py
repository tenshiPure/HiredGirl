#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Move03(Base):

	category = 'move'

	commandName = '3'
	description = '画面１ 右下'

	env = 'ryowin'

	if env ==  'ryowin':
		left   = 960
		top    = 540 
		width  = 960
		height = 540

	elif env ==  'nebigwin':
		left   = 960
		top    = 540 
		width  = 960
		height = 540

	elif env ==  'nebigmac':
		left   = 960
		top    = 540 
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
