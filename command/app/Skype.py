#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Skype(Base):

	category = 'app'

	commandName = 'skype'
	description = 'Skype'

	appName  = 'Skype.exe'
	appPath  = r'C:\Program Files (x86)\Skype\Phone\Skype.exe'
	winClass = 'tSkMainForm'

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self, isNew = None):
		scriptName = 'active' if isNew is None else 'new'
		script = self.createScriptPath(scriptName)

		self.executeAppScript(script)
