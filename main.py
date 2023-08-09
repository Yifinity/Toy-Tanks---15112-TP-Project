''' 
* Toy Tanks
* CMU 15112 Term Project
* Author: Yifan Jiang
* Date: 10 August 2023
'''


from Scenes.Startup import *
from Scenes.Instructions import *
from Scenes.RunGame import *
from Scenes.GameOver import *


def onAppStart(app): 
    app.runningAnimation = True
    app.runScenes = [
         Startup(),
         Instructions(),
         None,
         RunGame(app),
         GameOver() 
    ]
    # Use 60 sets per second for easy conversion factor
    app.stepsPerSecond = 60

    # Starting scene is our start up animation. 
    app.currentScene = app.runScenes[0]

def redrawAll(app):
    app.currentScene.redraw(app)    

def onStep(app):
    app.currentScene.onStep()

def onMousePress(app, mouseX, mouseY):
    app.currentScene.mousePress(mouseX, mouseY)

def onMouseMove(app, mouseX, mouseY):
    app.currentScene.mouseMove(mouseX, mouseY)


def onKeyPress(app, key):
    app.currentScene.keyPress(key)

def onKeyHold(app, keys):
    app.currentScene.keyHold(keys)

    
def main():
    runApp(width = 800, height = 600)

main()