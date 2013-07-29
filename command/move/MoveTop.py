#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class MoveTop(Base):

	category = 'move'

	commandName = 'top'
	description = '最前面トグル'

	env = 'ryowin'

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self):
		scriptName = 'top'
		script = self.createScriptPath(scriptName)

		self.executeNoArgScript(script)
