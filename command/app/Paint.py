#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Paint(Base):

	category = 'process'

	commandName = 'paint'
	description = 'Paint'

	appName  = 'mspaint.exe'
	appPath  = r'C:\Windows\System32\mspaint.exe'
	winClass = 'MSPaintApp'

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self, isNew = None):
		scriptName = 'active' if isNew is None else 'new'
		script = self.createScriptPath(scriptName)

		self.executeAppScript(script)
