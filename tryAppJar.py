import sys
from appJar import gui

def press(button):
 if button == 'llama':
  print( 'llama pressed!')
 if button == 'tapir':
  print( 'tapir pressed!')
 

win = gui()
win.addButtons(['llama', 'tapir'], press)
win.addImage('quadImage', 'quad.jpg')
win.go()
