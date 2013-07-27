#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Move4(Base):

	category = 'move'

	commandName = '4'
	description = '画面１ 左半分'

	left = 0
	top = 0

	env = 'ryowin'

	if env ==  'ryowin':
		width = 960
		height = 1080

	elif env ==  'nebigwin':
		width = 960
		height = 1080

	elif env ==  'nebigmac':
		width = 960
		height = 1080

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self):
		scriptName = 'move'
		script = self.createScriptPath(scriptName)

		self.executeMoveScript(script)
