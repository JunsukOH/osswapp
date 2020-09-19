from bangtal import *

scene1 = Scene("룸1", "Images/배경-1.png")

door1 = Object("Images/문-오른쪽-닫힘.png")
door1.locate(scene1, 800, 270)
door1.show()
door1.closed = True

key = Object("Images/열쇠.png")
key.setScale(1)
key.locate(scene1, 600, 150)
key.show()

flowerpot = Object("Images/화분.png")
flowerpot.setScale(1)
flowerpot.locate(scene1, 550, 150)
flowerpot.show()

scene2 = Scene("룸2", "Images/배경-2.png")

door2 = Object("Images/문-왼쪽-열림.png")
door2.locate(scene2, 320, 270)
door2.show()

door3 = Object('Images/문-안보임.png')
door3.locate(scene2, 910, 270)
door3.show()
door3.closed = True


def onMouseAction_door1(x, y, action):
    global door1, key, scene2
    if door1.closed == True:
        if key.inHand():
            door1.setImage("Images/문-오른쪽-열림.png")
            door1.closed = False
        else:
            showMessage("문이 잠겨있다. 열쇠가 필요한 것 같다.")
    else:
        scene2.enter()

door1.onMouseAction = onMouseAction_door1

def onMouseAction_key(x, y, action):
    global key
    key.pick()

key.onMouseAction = onMouseAction_key

flowerpot.moved = False
def onMouseAction_flowerpot(x, y, action):
    global flowerpot
    if flowerpot.moved == False:
        if action == MouseAction.DRAG_LEFT:
            flowerpot.locate(scene1, 450, 150)
            flowerpot.moved = True
        elif action == MouseAction.DRAG_RIGHT:
            flowerpot.locate(scene1, 650, 150)
            flowerpot.moved = True

flowerpot.onMouseAction = onMouseAction_flowerpot

def onMouseAction_door2(x, y, action):
    global scene1
    scene1.enter()
door2.onMouseAction = onMouseAction_door2

def onMouseAction_door3(x, y, action):
    global door3
    if door3.closed == True:
        door3.setImage("Images/문-오른쪽-열림.png")
        door3.closed = False
    else:
        endGame()
door3.onMouseAction = onMouseAction_door3

startGame(scene1)
