import guiController, listChecker, logicClass
import easygui
import os, re

def main():
	x = guiController.startup()
	logicClass.errorHandler(x)
	if x == 'error':
		return None 
	y = guiController.selectList()
	z = listChecker.listLength(y)
	c = logicClass.listSelecter(y, z + 2)
	g = logicClass.EorS_return(x)
	