#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Move01(Base):

	category = 'move'

	commandName = '1'
	description = '画面１ 左下'

	env = 'ryowin'

	if env ==  'ryowin':
		left   = 0
		top    = 540 
		width  = 960
		height = 540

	elif env ==  'nebigwin':
		left   = 0
		top    = 540 
		width  = 960
		height = 540

	elif env ==  'nebigmac':
		left   = 0
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
