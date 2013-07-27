#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class iTunes(Base):

	category = 'app'

	commandName = 'itunes'
	description = 'iTunes'

	appName  = 'iTunes.exe'
	appPath  = r'C:\Program Files (x86)\iTunes\iTunes.exe'
	winClass = 'iTunes'

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self, isNew = None):
		scriptName = 'active' if isNew is None else 'new'
		script = self.createScriptPath(scriptName)

		self.executeAppScript(script)
