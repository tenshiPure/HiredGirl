#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Exit(Base):
	category = 'operate'

	commandName = 'exit'
	description = 'アプリケーションを終了'

	env = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self):
		scriptName = 'kill'
		script = self.createScriptPath(scriptName)

		self.executeNoArgScript(script)
