#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class GoogleChrome(Base):

	category = 'app'

	commandName = 'chrome'
	description = 'GoogleChrome'

	appName  = 'chrome.exe'
	appPath  = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
	winClass = 'Chrome_WidgetWin_1'

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self, isNew = None):
		scriptName = 'active' if isNew is None else 'new'
		script = self.createScriptPath(scriptName)

		self.executeAppScript(script)
