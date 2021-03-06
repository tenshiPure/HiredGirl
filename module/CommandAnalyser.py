#-*- coding: utf-8 -*-
import os
import os.path
import sys

class CommandAnalyser:

	#
	# コンストラクタ
	#
	def __init__(self):
		pass

	#
	# 入力値を分割して返す
	#
	def splitInput(self, input):
		splited = input.split('_', 2)

		try:
			input1 = splited[0]
		except:
			input1 = ''

		try:
			input2 = splited[1]
		except:
			input2 = ''

		try:
			input3 = splited[2]
		except:
			input3 = ''

		return (input1, input2, input3)

	#
	# 入力値からコマンドを生成する
	#
	def createCommand(self, input1, input2, input3):
		command1 = self._searchModule(input1)
		command2 = self._searchModule(input2)
		command3 = self._searchModule(input3)

		return (command1, command2, command3)

	#
	# 入力値に適したコマンドクラスを探す
	#
	def _searchModule(self, input):
		pathApp = os.path.dirname(os.path.abspath(__file__)) + '/../command/app/'
		command = self._walkCompare(pathApp, input)

		if command is None:
			pathDir = os.path.dirname(os.path.abspath(__file__)) + '/../command/dir/'
			command = self._walkCompare(pathDir, input)

		if command is None:
			pathOperate = os.path.dirname(os.path.abspath(__file__)) + '/../command/operate/'
			command = self._walkCompare(pathOperate, input)

		if command is None:
			pathMove = os.path.dirname(os.path.abspath(__file__)) + '/../command/move/'
			command = self._walkCompare(pathMove, input)

		if command is None:
			pathOption = os.path.dirname(os.path.abspath(__file__)) + '/../command/other/'
			command = self._walkCompare(pathOption, input)

		return command

	#
	# 入力値と各コマンドクラスのコマンドを比較する
	#
	def _walkCompare(self, path, input):
		sys.path.append(os.path.abspath(path))

		for fileName in os.listdir(path):
			if fileName.find('pyc') != -1:
				continue

			moduleName = fileName.split('.', 1)[0]

			instance = getattr(__import__(moduleName), moduleName)()

			if instance.commandName == input:
				return instance

		return None

	#
	# 実行可能な入力値か判定する
	#
	def isExecutableInput(self, command1, command2, command3):
		if command1.category == 'none':
			return False

		if command1.category == 'process':
			if command2.category == 'none' or command2.commandName == 'new':
				if command3.category != 'none':
					return False
			else:
				if command2.category != 'move' and command2.commandName != 'kill' and command2.commandName != 'exit' and command2.commandName != 'new':
					return False
				if command2.category != 'move' and command3.commandName != 'new':
					return False

		if command1.commandName == 'ss':
			if command3.category != 'none':
				return False

		if command1.commandName == 'sleep':
			if command2.category != 'none':
				return False
			if command3.category != 'none':
				return False

		if command1.commandName == 'kill' or command1.commandName == 'exit':
			if command2.category != 'none':
				return False
			if command3.category != 'none':
				return False

		if command1.commandName == 'desc':
			if command2.commandName != 'env' and command2.commandName != 'all':
				return False
			if command3.category != 'none':
				return False

		if command1.category == 'move':
			if command2.category != 'none':
				return False
			if command3.category != 'none':
				return False

		return True
