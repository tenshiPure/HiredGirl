#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class VisualBoyAdvance(Base):

	category = 'app'

	commandName = 'vba'
	description = 'VisualBoyAdvance'

	appName  = 'VisualBoyAdvance.exe'
	appPath  = r'D:\Game\emulator\GBA\VisualBoyAdvanceLink\VisualBoyAdvance.exe'
	winClass = 'Afx:400000:0:0:1900011:3a6d0763'

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self, isNew = None):
		scriptName = 'active' if isNew is None else 'new'
		script = self.createScriptPath(scriptName)

		self.executeAppScript(script)
