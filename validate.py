from tkinter import Label, Toplevel, filedialog, messagebox, ttk
from tkinter import *

try:
    from PIL import Image
except ImportError:
    print("no")
from PIL import ImageTk, Image
import preproc
import get_info
from functools import partial
import crop
import cv2

img = 0
photoimg_ok1 = 0
photoimg_nok1 = 0
informatii = {}


def show_file_chooser(main):
    global img, photoimg_ok1, photoimg_nok1
    img_ok1 = Image.open("icons/id_ok.png")
    img_ok1 = img_ok1.resize((img_ok1.size[0] // 2, img_ok1.size[1] // 2), Image.ANTIALIAS)
    photoimg_ok1 = ImageTk.PhotoImage(img_ok1)
    img_nok1 = Image.open("icons/id_nok.png")
    img_nok1 = img_nok1.resize((img_nok1.size[0] // 2, img_nok1.size[1] // 2), Image.ANTIALIAS)
    photoimg_nok1 = ImageTk.PhotoImage(img_nok1)
    filename = filedialog.askopenfilename()
    if not filename:
        messagebox.showwarning(title="Fisier neselectat", message="Nu ati selectat fiserul!")
    else:
        validate_info(main, filename)


def validate_info(main, filename):
    global img, photoimg_ok1, photoimg_nok1, informatii
    img_frame = Toplevel(main)
    img_frame.title("Verifica informatiile")
    imgf = ttk.Frame(img_frame)
    canvas = Canvas(imgf, width=688, height=488)
    canvas.pack()
    imgf.grid(column=0, row=0, rowspan=10)
    imgr = Image.open(filename)
    imgr = imgr.resize((688, 488), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(imgr)
    canvas.create_image(0, 0, anchor=NW, image=img)
    img_copy = ImageTk.PhotoImage(imgr)
    informatii = {
        "Nume": StringVar(img_frame),
        "Prenume": StringVar(img_frame),
        "CNP": StringVar(img_frame),
        "Cetatenie": StringVar(img_frame),
        "Loc Nastere": StringVar(img_frame),
        "Domiciliu": StringVar(img_frame),
        "Seria": StringVar(img_frame),
        "Nr": StringVar(img_frame),
        "Data nastere": StringVar(img_frame),
    }
    mng_img = preproc.preprocesare(filename)
    informatii = get_info.get_informatii(mng_img, informatii)
    lung_min = {
        "Nume": 30,
        "Prenume": 35,
        "CNP": 13,
        "Cetatenie": 15,
        "Loc Nastere": 25,
        "Domiciliu": 45,
        "Seria": 3,
        "Nr": 6,
        "Data nastere": 10,
    }
    current_row = 0
    for key, value in informatii.items():
        b = ttk.Button(img_frame, text=key,
                       command=partial(crop.decupeaza, canvas, img_copy, filename, key, informatii))
        b.grid(column=1, row=current_row)
        b_valid = ttk.Entry(img_frame, width=lung_min[key], justify='center', font=('calibre', 10, 'normal'),
                            textvariable=informatii[key])
        b_valid.grid(column=2, row=current_row)
        current_row += 1

    valid_button = ttk.Button(img_frame, text="Informatii valide", image=photoimg_ok1, compound=LEFT,
                              command=partial(ok_validate, img_frame, informatii))
    valid_button.grid(column=1, row=9)
    cancel_button = ttk.Button(img_frame, text="Inchide", image=photoimg_nok1, compound=LEFT,
                               command=partial(nok_validate, img_frame))
    cancel_button.grid(column=2, row=9)


def ok_validate(img_frame, informatii):
    ok = messagebox.askokcancel(title="Informatii validate",
                                message="S-au salvat informatiile.\nApasati pe Ok pentru a continua")
    if ok:
        img_frame.destroy()
        img_frame.update()
    else:
        pass


def nok_validate(img_frame):
    global informatii
    retry = messagebox.askretrycancel(title="Informatii nevalidate",
                                      message="Nu veti putea completa documentele.\nApasati pe Retry pentru a va intoarce")
    if retry:
        pass
    else:
        informatii.clear()
        img_frame.destroy()
        img_frame.update()
