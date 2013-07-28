#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class New(Base):

	category = 'other'

	commandName = 'new'
	description = 'アプリを新規で起動する'

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']
