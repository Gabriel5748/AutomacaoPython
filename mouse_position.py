import pyautogui as py;

while True:
    x = py.position().x
    y = py.position().y
    print(f'X = {x}, Y = {y}')
