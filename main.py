from datetime import datetime

from Persoana import Persoana

try:
    from PIL import Image
except ImportError:
    print("no")
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
from functools import partial

try:
    from PIL import Image
except ImportError:
    print("no")
from PIL import ImageTk, Image
import validate
import cereri


def complet():
    informatii = validate.informatii
    var = cereri.var
    no_val = 1
    for i, sel in enumerate(var):
        if sel.get() == 1:
            no_val = 0
    if not bool(informatii):
        messagebox.showerror(title="Nu au fost salvate informatii",
                             message="Alegeti mai intai poza cu buletinul pentru a valida informatiile!")
    elif not bool(var) or no_val:
        messagebox.showerror(title="Nu au fost selectate documentele", message="Selectati mai intai documentele!")
    else:
        cereri.fa_cereri(informatii, var)


def iesi(root):
    root.destroy()


def main():
    root = Tk()
    root.title("DocFiller!")

    content = ttk.Frame(root, padding=(3, 3, 12, 12))
    width = 100
    height = 100
    img_choose = Image.open("icons/add_file.png")
    img_choose = img_choose.resize((width, height), Image.ANTIALIAS)
    photoImg_choose = ImageTk.PhotoImage(img_choose)
    askfilebutton = ttk.Button(root, text="Alege imagine cu buletinul", image=photoImg_choose, compound=LEFT,
                               command=partial(validate.show_file_chooser, root))
    img_template = Image.open("icons/template.png")
    img_template = img_template.resize((width, height), Image.ANTIALIAS)
    photoImg_template = ImageTk.PhotoImage(img_template)
    asktemplate = ttk.Button(root, text="Alege documentul de completat", image=photoImg_template, compound=LEFT,
                             command=partial(cereri.selecteaza_documente, root))
    img_ok = Image.open("icons/checked1.png")
    img_ok = img_ok.resize((img_ok.size[0] // 2, img_ok.size[1] // 2), Image.ANTIALIAS)
    photoimg_ok = ImageTk.PhotoImage(img_ok)
    proceedbutton = ttk.Button(root, text="Completeaza!", image=photoimg_ok, compound=LEFT, command=complet)
    img_nok = Image.open("icons/unchecked.png")
    img_nok = img_nok.resize((img_nok.size[0] // 2, img_nok.size[1] // 2), Image.ANTIALIAS)
    photoimg_nok = ImageTk.PhotoImage(img_nok)
    exitbutton = ttk.Button(root, text="Inchide", image=photoimg_nok, compound=LEFT, command=partial(iesi, root))

    content.grid(column=0, row=0, sticky=(N, S, E, W))
    askfilebutton.grid(column=0, row=0)
    asktemplate.grid(column=1, row=0)
    proceedbutton.grid(column=0, row=1, columnspan=1, rowspan=1)
    exitbutton.grid(column=1, row=1, columnspan=1, rowspan=1)
    root.pack_propagate(False)
    root.resizable(False, False)
    root.mainloop()


def maintr():
    p = Persoana()
    p.nume = "Pop"
    p.prenume = "Brusli"
    p.cetatenie = "Romana / ROU"
    p.loc_nastere.set_localitate("Husi", "Valsui")
    p.domiciliu.set_domiciliu(("Husi", "Valsui"), ("Mihai", 3))
    p.emis = "IDROU"
    p.data_nastere = datetime(2022, 1, 1)
    p.af()


if __name__ == "__main__":
    maintr()
