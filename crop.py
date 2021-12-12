from tkinter import *

try:
    from PIL import Image
except ImportError:
    print("no")
from functools import partial
import preproc
import get_info


def decupeaza(canvas, img_copy, filename, key, informatii):
    canvas.bind('<Button-1>', partial(incepe_decupare, canvas))
    canvas.bind('<B1-Motion>', partial(trage, canvas, img_copy))
    canvas.bind('<ButtonRelease-1>', partial(sfarsit_decupare, canvas, filename, key, informatii, img_copy))


x, y, x_, y_ = 0, 0, 0, 0
text = ""


def incepe_decupare(canvas, event):
    global x, y
    x, y = event.x, event.y
    return


def trage(canvas, img, event):
    canvas.create_image(0, 0, anchor=NW, image=img)
    global x, y, x_, y_
    x_, y_ = event.x, event.y
    canvas.create_rectangle(x, y, x_, y_)


def sfarsit_decupare(canvas, filename, key, informatii, img, event):
    global text
    canvas.unbind('<Button-1>')
    canvas.unbind('<B1-Motion>')
    canvas.unbind('<ButtonRelease-1>')
    introd_text(filename, key, informatii)
    canvas.create_image(0, 0, anchor=NW, image=img)


def introd_text(filename, key, informatii):
    global x, y, x_, y_
    img = preproc.preprocesare(filename)
    h, w = img.shape
    rapy = round(h / 488)
    rapx = round(w / 688)
    y *= rapy
    y_ *= rapy
    x *= rapx
    x_ *= rapx
    img = img[y:y_, x:x_]
    text = get_info.get_text(img)
    informatii[key].set(text)
