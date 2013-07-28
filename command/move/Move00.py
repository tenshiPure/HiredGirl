#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Move00(Base):

	category = 'move'

	commandName = '0'
	description = '最小化'

	env = 'ryowin'

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self):
		scriptName = 'minimize'
		script = self.createScriptPath(scriptName)

		self.executeMinimizeScript(script)
