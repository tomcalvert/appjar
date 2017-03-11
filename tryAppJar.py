import sys
from appJar import gui

def press(button):
	if button == 'llama':
		print( 'llama pressed!')
	if button == 'tapir':
		print( 'tapir pressed!')
	if button == 'zebra':
		print( 'zebra pressed!')
 

win = gui()
win.addButtons(['llama', 'tapir', 'zebra'], press)
win.addImage('quadImage', 'quad.jpg')
win.go()
