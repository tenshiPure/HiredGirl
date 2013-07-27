#-*- coding: utf-8 -*-
import os
import os.path

class Base:

	category = 'base'

	#
	# スクリプトのパスを組み立てる
	#
	def createScriptPath(self, scriptName):
		scriptHead = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../script')
		scriptPath = os.path.join(scriptHead, self.category)
		exeName = 'win.exe' if os.name == 'nt' else 'mac'

		script = '"%s/%s/%s"' % (scriptPath, scriptName, exeName)

		return script

	#
	# app系スクリプトを実行する
	#
	def executeAppScript(self, script):
		os.system('%s %s %s %s' % (script, self.appName, self.appPath, self.winClass))

	#
	# moveスクリプトを実行する
	#
	def executeMoveScript(self, script):
		os.system('%s %s %s %s %s' % (script, self.left, self.top, self.width, self.height))
