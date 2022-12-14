from asyncio.windows_events import NULL
import time
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 
from question import *
import serial
import serial.tools.list_ports

import pyautogui



"""
install Python3
install pip
pip install python3-tk
pip install pillow
pip install serial

"""

root = Tk()
#----------tkinter settings-------------#
logo_resize_factor = 1.5
question_resize_factor = 0.5
answers_resize_factor = 0.3



title = "Quize"



#window_size = {"width" : 394, "height" :701}
window_size = {"width" :  root.winfo_screenwidth() , "height" : root.winfo_screenheight()}

button_style = ttk.Style()
button_style.configure ('W.TButton', font =
               ('calibri', 25),
               activecolor = 'none',
               # background=[('pressed', '#e8372a'), ('active', 'blue')],
               height=15, 
               width=round(window_size["width"] * 0.05))

button_style.map('W.TButton', 
                foreground=[('active', '#e8372a'),
                            ('pressed', '#000000')])



#________quize settings________________#
quize_folder = "quize"
quize = loadQuize(quize_folder)
logo = ImageTk.PhotoImage(Image.open("quize/assets/company_logo.png"))

picks = [Image.open("quize/assets/test1.png"), 
        Image.open("quize/assets/test2.png"),
        Image.open("quize/assets/test3.png"),
        Image.open("quize/assets/test4.png"),
        Image.open("quize/assets/test5.png")]
quest_picks = []
for image in picks:
        a =  ImageTk.PhotoImage(image)
        quest_picks.append(a)




#____________COM PORT SETTINGS_________________________#
serialPort = NULL
print('Search...')
ports = serial.tools.list_ports.comports(include_links=False)
# for port in ports :
#         print('Find port '+ port.device)    
#         serialPort = port.device








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
       

def checkAnswer(question_frame, answer, gamestate):
        question_frame.destroy()
        pyautogui.moveTo(0,0)
        if answer == quize[gamestate[0]].correct_answer:
                gamestate[1] = gamestate[1] + 1
        gamestate[0] = gamestate[0] + 1

        if gamestate[1] == 5:
                print("Winner!")
                serialPort.write(1)
                gamestate[1] == 0
        if gamestate[0] == len(quize):
                gamestate[0] = 0
                
        if gamestate[0] % 5 == 0:
                gamestate[1] = 0

        count.configure(text = str(gamestate[1]) + "/5 #" + str(gamestate[0] + 1))
        setQuestionGUI(gamestate)
        


def setQuestionGUI(gamestate):
        question = quize[gamestate[0]]
        question_frame = ttk.Frame(root)
        question_frame.pack(pady= 100)
        question_text = Label(question_frame,
        text = question.text, 
        font = ('calibi', 25))
        question_text.pack()
        if question.image != "":
                question_canvas = setCanvas(question_frame, quest_picks[int(quize[gamestate[0]].image)])
                question_canvas.pack()

        for answer in question.answers:
                # if answer[1] != "":
                #         answerCanvas = setCanvas(question_frame, answer[1], "blue", answers_resize_factor)
                #         answerCanvas.pack(side = LEFT)
                button = ttk.Button(question_frame, 
                                text = answer[0], 
                                style= 'W.TButton',
                                command=lambda f = question_frame, a = answer[0], gs=gamestate
                                :checkAnswer(f, a, gs))
                button.pack(pady = 10, ipady = 30)


if __name__ == '__main__':
        root.title(title)
        #root.geometry(str(window_size["width"]) + "x" + str(window_size["height"]))
        root.attributes("-fullscreen", True)
        root.config()
        huh = time.time()

        
        gamestate = [0, 0]
        logocanvas = setCanvas(root, logo)
        logocanvas.pack(pady=window_size["height"] * 0.05)

        count = Label(root, text = '0/5', font =('calibi', 20, 'italic'))
        count.pack()
        

        setQuestionGUI(gamestate)
        root.mainloop()