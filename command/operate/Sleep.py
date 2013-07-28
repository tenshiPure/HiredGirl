#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Sleep(Base):
	category = 'operate'

	commandName = 'sleep'
	description = 'スリープ状態にする'

	env = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self):
		scriptName = 'sleep'
		script = self.createScriptPath(scriptName)
		print script

		self.executeNoArgScript(script)
