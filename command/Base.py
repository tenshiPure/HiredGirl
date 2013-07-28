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
		appName = self.appName.replace(' ', '_space_')
		appPath = self.appPath.replace(' ', '_space_')
		winClass = self.winClass.replace(' ', '_space_')
		os.system('%s %s %s %s' % (script, appName, appPath, winClass))

	#
	# dir系スクリプトを実行する
	#
	def executeDirScript(self, script):
		dirPath = self.dirPath.replace(' ', '_space_')
		os.system('%s %s %s %s' % (script, 'blah', dirPath, 'CabinetWClass'))

	#
	# move系スクリプトを実行する
	#
	def executeMoveScript(self, script):
		os.system('%s %s %s %s %s' % (script, self.left, self.top, self.width, self.height))

	#
	# 引数がないスクリプトを実行する
	#
	def executeNoArgScript(self, script):
		os.system('%s' % (script))
