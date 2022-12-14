from tkinter import *
from question import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image


root = Tk()





def setCanvas(parent, image):
        canvas = Canvas(
                parent,
                width = image.width(),
                height = image.height(),
                )
        canvas.create_image(
                image.width()/2, image.height()/2,
                anchor=CENTER,
                image= image
                )
        return canvas



def main():
    file_path = filedialog.askopenfilename()

    image = PhotoImage(file = file_path)
    ttk.Label(root, image = image).pack()
    root.mainloop()


if __name__ == "__main__":
    main()