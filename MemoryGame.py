
# THIS PROJECT IS
# MADE BY DORA ESIN USTA
# COMPUTER ENGINEERING (100% ENGLISH)
# STUDENT NUMBER: 17290126


import tkinter as tk
from tkinter import ttk
import random
from functools import partial  


initial_num = 5
counter = 0
answer = ''
congrats_check = 0
wrong_check = 0
root = tk.Tk()
img = tk.PhotoImage(file = 'icon.png')
root.tk.call('wm','iconphoto',root._w, img)
root.geometry("700x700")
root.title("Memory Game")
root.configure(background='#fee2e9')
button_style = ttk.Style()
button_style.configure('bs.TButton', font=('Century Gothic',14),foreground = "#951747",background = "#f0c1cc", height=50)
label = tk.Label(root, bg = '#fee2e9' )
button = ttk.Button(root, text = 'Ready!', style='bs.TButton', command = lambda: counter_label(label))
# (command waits for a function object. If we call counter_label without using lambda, function will be called before the
#  creation of widget and command will be assigned with the return value.)

button.place(relx = 0.5, rely = 0.5, anchor = 'center')
button_2 = ttk.Button(root)


def counter_label(label):
    global disp
    global initial_num
    counter = initial_num
    button.place_forget()
    button_2.place_forget()

    
        
    def disp(key, entry, button_1):
        global answer
        global initial_num
        global congrats_check
        global wrong_check
        congrats = tk.Label(root, bg = '#fee2e9')
        entry.place_forget()
        button_1.place_forget()
        
        if answer == key.get()+' ':
            
            def print_message():
                global congrats_check
                if congrats_check == 1:
                    congrats_check = 0
                    congrats.place_forget()
                    return 0
                    
                congrats.config(text = "CONGRATS!", font=('Century Gothic',20), width = 25, height = 25)
                congrats.place(relx = 0.5, rely = 0.5, anchor = 'center')
                congrats.after(3000, lambda: print_message())
                congrats_check = 1

            print_message()

            answer = ''
            initial_num += 1
            
            button_2.configure(text = 'Ready!', style='bs.TButton', command = lambda: counter_label(label))
            button_2.place(relx = 0.5, rely = 0.5, anchor = 'center')           
            
        
        else:
            def print_message():
                global wrong_check
                if wrong_check == 1:
                    wrong_check = 0
                    congrats.place_forget()
                    return 0
                    
                congrats.config(text = "Wrong Answer, Try Again!", font=('Century Gothic',20), width = 25, height = 25, fg='#7a7a7a')
                congrats.place(relx = 0.5, rely = 0.5, anchor = 'center')
                congrats.after(3000, lambda: print_message())
                wrong_check = 1

            print_message()
            answer = ''
            button_2.configure(text = 'Ready!', style='bs.TButton', command = lambda: counter_label(label))
            button_2.place(relx = 0.5, rely = 0.5, anchor = 'center')
            
        return


    def entry_box():
        global disp
        key = tk.StringVar()
        entry = tk.Entry(root, textvariable = key, width = 20, bd = 6, relief = "flat",font=('Century Gothic',14) )
        entry.place(relx = 0.35, rely = 0.5, anchor = 'center')
        button_1 = ttk.Button(root)
        disp = partial(disp, key, entry, button_1)
        button_1.configure(text = 'Submit!',style='bs.TButton', command = disp)
        button_1.place(relx = 0.68, rely = 0.5, anchor = 'center')


    def count(counter):
        global answer
        if counter == 0:
            label.place_forget()
            print(answer) #----> to see the answers in the shell
            entry_box()
            return 0
        value = random.randint(1,10)
        answer += str(value) + ' '
        label.config(text = str(value))
        label.config(font=('Century Gothic',20))
        label.place(relx = random.randint(1,90)/100, rely = random.randint(1,90)/100)
        counter -= 1
        label.after(1000,lambda: count(counter))
        

    
    count(counter)
    

root.mainloop()
