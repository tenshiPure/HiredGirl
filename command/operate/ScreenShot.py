#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class ScreenShot(Base):
	category = 'operate'

	commandName = 'ss'
	description = 'スクリーンショット'

	env = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self, fileName):
		scriptName = 'screenshot'
		script = self.createScriptPath(scriptName)

		path = os.path.dirname(os.path.abspath(__file__)) + '/../app'
		sys.path.append(os.path.abspath(path))
		from Paint import Paint

		self.executeScreenShotScript(script, Paint(), fileName)
