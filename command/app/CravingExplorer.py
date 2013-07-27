#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class CravingExplorer(Base):

	category = 'app'

	commandName = 'ce'
	description = 'CravingExplorer'

	appName  = 'CravingExplorer.exe'
	appPath  = r'C:\Program Files (x86)\CravingExplorer\CravingExplorer.exe'
	winClass = 'Craving Explorer'

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self, isNew = None):
		scriptName = 'active' if isNew is None else 'new'
		script = self.createScriptPath(scriptName)

		self.executeAppScript(script)
