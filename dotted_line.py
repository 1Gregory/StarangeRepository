from PIL import Image
width = int(input("Width: "))
height = int(input("Height: "))

img = Image.new("RGB", (width * 10, height * 10), "black")
canvas = img.load()

cursor = [0, 0]
show = True
step = 10
vector = "d-r"  # d-r  d-l  t-r  t-l


while not(cursor == [width*10-1, 0] or cursor == [0, height*10-1] or cursor == [width*10-1, height*10-1]):
    if step == 0:
        show = not (show)
        step = 10
    if show:
        canvas[cursor[0], cursor[1]] = (255, 255, 255)
    if vector == "d-r":
        if cursor[1] == height*10-1:
            vector = "t-r"
            cursor[0] += 1
        elif cursor[0] == width*10-1:
            vector = "d-l"
            cursor[1] += 1
        else:
            cursor[0] += 1
            cursor[1] += 1
    elif vector == "d-l":
        if cursor[1] == height*10-1:
            vector = "t-l"
            cursor[0] -= 1
        elif cursor[0] == 0:
            vector = "d-r"
            cursor[1] += 1
        else:
            cursor[0] -= 1
            cursor[1] += 1
    elif vector == "t-r":
        if cursor[0] == width*10-1:
            vector = "t-l"
            cursor[1] -= 1
        elif cursor[1] == 0:
            vector = "d-r"
            cursor[0] += 1
        else:
            cursor[0] += 1
            cursor[1] -= 1
    elif vector == "t-l":
        if cursor[0] == 0:
            vector = "t-r"
            cursor[1] -= 1
        elif cursor[1] == 0:
            vector = "d-l"
            cursor[0] -= 1
        else:
            cursor[0] -= 1
            cursor[1] -= 1

    step -= 1

img.show()