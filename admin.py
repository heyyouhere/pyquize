from tkinter import *
from question import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image


root = Tk()
WIDTH = '1080'
HIGHT = '540'
root.geometry(WIDTH + 'x' + HIGHT)
resize_factor = 0.3

def getCanvas(parent, image):
        canvas = Canvas(
                parent,
                width = resize_factor * image.width(),
                height = resize_factor *image.height(),
                )
        canvas.create_image(
                image.width()/2, image.height()/2,
                anchor=CENTER,
                image= image
                )
        return canvas


ipadding = {'ipadx': 10, 'ipady': 10}
def createQuestion(menu):
    question_button = Button(menu, text='New Question')
    question_button.pack(ipady= 10)
    
    ...

def getPictureFromFile(parent):
    file_path = filedialog.askopenfilename()
    image = PhotoImage(file = file_path)
    canvas = getCanvas(parent, image)
    canvas.pack()
       

def openQuestionMenu(text):
        print(text)

def set_list_packing(list, bool):
        if bool:
                for l in list:
                        l.pack()
        else:
                for l in list:
                        l.pack_forget()
                
                

quize_menu = []
question_menu = []
scrolling_menu = []


def main():
        objects_frame = Frame(root)
        objects_frame.pack(side = LEFT, ipadx= int(WIDTH)/4, expand=True)

        quize_frame = Frame(root)
        quize_frame.pack(side = RIGHT, ipadx= int(WIDTH)/4, expand=True)


        #Quize menu
        quize_name = Label(quize_frame, text = 'Input quize name')
        quize_menu.append(quize_name)
        quize_name_entry = Entry(quize_frame)
        quize_menu.append(quize_name_entry)


        sensor_label = Label(quize_frame, text = 'Allow sensor input')
        quize_menu.append(sensor_label)
        sensorInput = Checkbutton(sensor_label)
        quize_menu.append(sensorInput)


        add_logo_button = Button(quize_frame, text = 'Add logo', command = lambda:getPictureFromFile(quize_frame))
        quize_menu.append(add_logo_button)


        for item in quize_menu:
                item.pack(ipadding) 


        quize_settings_button = Button(objects_frame, text = 'Quize', command = lambda:openQuestionMenu(quize_name_entry.get()))
        scrolling_menu.append(quize_settings_button)
        add_question_button = Button(objects_frame, text = 'Hide menu', command = lambda:set_list_packing(quize_menu, False))
        scrolling_menu.append(add_question_button)
        
        set_list_packing(scrolling_menu, True)
        root.mainloop()



if __name__ == "__main__":
    main()