from array import array
from email.mime import base
from multiprocessing.dummy import Array
from typing import final
import pyautogui
screenWidth =pyautogui.size().width
screenHeight = pyautogui.size().height
lines = "No instructions"
pyautogui.moveTo(screenWidth/2, screenHeight/2, duration = 1)
try:
    with open('automom_instructions.auto') as f:
        lines = f.readlines()
except:
    print("Not instructions file found")
def purifyInstruction(command):
    keys="No keys loaded"
    command = command.strip()
    command = command.split("(")
    baseInstruction = command[0]
    params = command[1].replace(")","").split(",")
    try:
        with open('automom_battery.auto') as f:
            keys = f.readlines()
    except:
        print("Not Battery file found")
        return 
    finalKeys = []
    for key in keys:
        key = key.strip()
        finalKeys.append(key.split("=")[0])
        finalKeys.append( key.split("=")[1])
    # keys = keys.split("=")
    finalParams = []
    finalCommand = []
    for param in params:
        if param.isnumeric():
            finalParams.append(param)
        else:
            if param in finalKeys:
                finalParams.append(finalKeys[finalKeys.index(param)+1])
            else:
              finalParams.append(param)
        
    finalCommand.append(command[0])
    finalCommand.append(finalParams)
    return finalCommand
def executeInstruction(instruction):
    baseInstruction = instruction[0]
    params = instruction[1]
    match baseInstruction:
        case "move":
            print("se debe mover a X:"+params[0]+"|Y:"+params[1]+"|Tiempo:"+params[2]+"s")
            pyautogui.moveTo(int(params[0]),int(params[1]),int(params[2]))
        case "find":
            while 1==1:
                position = pyautogui.position()
                print(position)
        case "rightClick":
            pyautogui.rightClick()
        case "leftClick":
            pyautogui.leftClick()
        case "write":
            pyautogui.write(params[0])
        case "press":
            pyautogui.press(params[0])
        # If an exact match is not confirmed, this last case will be used if provided
        case _:
            return "Something's wrong with the internet"
        
for instruction in lines:
    instruction = purifyInstruction(instruction)
    executeInstruction(instruction)
    

