# MADE WITH tkinter 

import time
import random
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# from PIL import ImageTk, Image

class Root(Tk):

    def __init__(self):
        super().__init__()

        self.play = 0
        self.player = 'o'
        self.winner = ""
        # self.color = ''
        self.x_score = 0
        self.o_score = 0
        self.ways_to_win = {'win1': [1, 2, 3], 'win2': [6, 5, 4], 'win3': [7, 8, 9],
                            'win4': [1, 6, 7], 'win5': [2, 5, 8], 'win6': [3, 4, 9], 'win7': [1, 5, 9], 'win8': [3, 5, 7]}
        self.wins = {'win1': [], 'win2': [], 'win3': [],
                     'win4': [], 'win5': [], 'win6': [], 'win7': [], 'win8': []}
        self.clicked = []
        self.my_image = ImageTk.PhotoImage(Image.open("brick.jpg"))
        self.image2 = ImageTk.PhotoImage(Image.open("forest.jpg"))

        self.frame = Label(bg="#bde5ff", image=self.my_image)
        self.frame.place(relheight=1, relwidth=1)

        self.label = Label(self.frame, bg="white", text="Xender Game")
        self.label.place(x=0, y=10, relwidth=0.75, relheight=0.09)

        self.label2 = Label(self.frame, bg="white", text="Turn: X")
        self.label2.place(x=186, y=10, relwidth=0.24, relheight=0.09)

        self.label3 = Label(self.frame, bg="pink", text="Easy")
        self.label3.place(x=188, y=135, relwidth=0.24, relheight=0.09)

        self.setmode()

        self.result_label1 = Label(
            self.frame, bg="white", text="x : 0", font=('arial 13 bold'))
        self.result_label1.place(x=188, y=38, relwidth=0.24, relheight=0.09)

        self.result_label2 = Label(
            self.frame, bg="white", text="o : 0", font=('arial 13 bold'))
        self.result_label2.place(x=188, y=62, relwidth=0.24, relheight=0.09)

        self.checkresult()

        #############Buttons for the game###############
        self.but1 = Button(self.frame, fg="black", bd=1, activebackground="#78929c", bg="white", text="", font=(
            'arial 30 bold'), command=lambda: self.click('1'))
        self.but1.place(x=0, y=38, relwidth=0.2532, relheight=0.199)

        self.but2 = Button(self.frame, fg="black", bd=1, bg="#59bdff", activebackground="#78929c", text="", font=(
            'arial 30 bold'), command=lambda: self.click('2'))
        self.but2.place(x=63.3, y=38, relwidth=0.2532, relheight=0.199)

        self.but3 = Button(self.frame, fg="black", bd=1, bg="white", activebackground="#78929c", text="", font=(
            'arial 30 bold'), command=lambda: self.click('3'))
        self.but3.place(x=126.6, y=38, relwidth=0.2532, relheight=0.199)

        self.but6 = Button(self.frame, fg="black", bd=1, bg="#59bdff", activebackground="#78929c", text="", font=(
            'arial 30 bold'), command=lambda: self.click('6'))
        self.but6.place(x=0, y=93.7, relwidth=0.2532, relheight=0.199)

        self.but5 = Button(self.frame, fg="black", bd=1, bg="white", activebackground="#78929c", text="", font=(
            'arial 30 bold'), command=lambda: self.click('5'))
        self.but5.place(x=63.3, y=93.7, relwidth=0.2532, relheight=0.199)

        self.but4 = Button(self.frame, fg="black", bd=1, bg="#59bdff", activebackground="#78929c", text="", font=(
            'arial 30 bold'), command=lambda: self.click('4'))
        self.but4.place(x=126.6, y=93.7, relwidth=0.2532, relheight=0.199)

        self.but7 = Button(self.frame, fg="black", bd=1, bg="white", activebackground="#78929c", text="", font=(
            'arial 30 bold'), command=lambda: self.click('7'))
        self.but7.place(x=0, y=150.4, relwidth=0.2532, relheight=0.199)

        self.but8 = Button(self.frame, fg="black", bd=1, bg="#59bdff", activebackground="#78929c", text="", font=(
            'arial 30 bold'), command=lambda: self.click('8'))
        self.but8.place(x=63.3, y=150.4, relwidth=0.2532, relheight=0.199)

        self.but9 = Button(self.frame, fg="black", bd=1, bg="white", activebackground="#78929c", text="", font=(
            'arial 30 bold'), command=lambda: self.click('9'))
        self.but9.place(x=126.6, y=150.4, relwidth=0.2532, relheight=0.199)

        self.btn_label = Label(self.frame, bd=0.5, bg="purple").place(
            x=189.3, y=105, relwidth=0.33, relheight=0.1)

        Label(self.frame, bd=0.5, bg="purple", image=self.image2).place(
            x=0, y=208, relwidth=1, relheight=0.3)

        Button(self.btn_label, text="Restart", bd=0.5, fg="purple", font=('calibri 10 bold'),  command=self.refresh2).place(
            x=195, y=110, relwidth=0.2, relheight=0.08)

        Button(self.frame, text="Reset", bd=0.5, fg="blue", font=('calibri 10 bold'),  command=self.reset).place(
            x=198, y=255, relwidth=0.2, relheight=0.08)
        ########## confirm quit button ###########
        Button(self.frame, text="Exit", bd=0.5, fg="white", bg="red", font=('calibri 10 bold'),  command=self.confirm_exit).place(
            x=0, y=255, relwidth=0.2, relheight=0.08)

    ####################################
    ####################################
    ####################################
    ####################################
    ####################################
    ####################################
    ##  function Confirm the program quit ##

    def reset(self):
        ask = messagebox.askokcancel(
            'Reset Progress?', 'This action cannot be reversed!')
        if ask == True:
            file = open('file.txt', 'w')
            file.write('')
            file.close()
            self.play = 0
            self.clicked = []
            self.refresh()
            self.checkresult()
            self.x_score = 0
            self.o_score = 0
            self.result_label1.configure(text="x : %d" % self.x_score)
            self.result_label2.configure(text="o : %d" % self.o_score)
        else:
            pass

    ###########################
    ###########################
    ###########################
    def confirm_exit(self):
        quest = messagebox.askquestion("Confirm Exit", "Are you sure to exit?")
        if quest == 'yes':
            root.quit()
        else:
            pass

    ###########################
    ###########################
    ###########################
    def click(self, num):
        num = int(num)
        if self.play % 2 == 0:
            if num not in self.clicked:
                self.clicked.append(num)
                self.player = 'x'
                self.color = 'blue'

                for ind in range(1, 9):
                    if num in self.ways_to_win[f'win{ind}']:
                        self.wins[f'win{ind}'].append(self.player)

                if num == 1:
                    self.but1.configure(
                        text=self.player, fg=self.color, command='')
                elif num == 2:
                    self.but2.configure(
                        text=self.player, fg=self.color, command='')
                elif num == 3:
                    self.but3.configure(
                        text=self.player, fg=self.color, command='')
                elif num == 4:
                    self.but4.configure(
                        text=self.player, fg=self.color, command='')
                elif num == 5:
                    self.but5.configure(
                        text=self.player, fg=self.color, command='')
                elif num == 6:
                    self.but6.configure(
                        text=self.player, fg=self.color, command='')
                elif num == 7:
                    self.but7.configure(
                        text=self.player, fg=self.color, command='')
                elif num == 8:
                    self.but8.configure(
                        text=self.player, fg=self.color, command='')
                elif num == 9:
                    self.but9.configure(
                        text=self.player, fg=self.color, command='')

                self.play += 1
                if self.play % 2 == 0:
                    self.player2 = 'x'
                else:
                    self.player2 = 'o'
                self.label2.configure(text=f"Turn: {self.player2.upper()}")

                self.checkforwin()
                if len(self.clicked) >= 9:
                    time.sleep(1)
                    self.refresh()
                self.robotplay()
            else:
                self.robotplay()

        else:
            self.player = 'o'
            self.color = 'purple'
    ###########################
    ###########################
    ###########################
    def checkforwin(self):

        for i in range(1, 9):
            if self.wins[f'win{i}'].count('o') == 3:
                self.winner = 'o'
                self.o_score += 1
                writefile = open('file.txt', 'w')
                writefile.write(f'{self.x_score}\n{self.o_score}')
                writefile.close()
                self.alertwinner()
            elif self.wins[f'win{i}'].count('x') == 3:
                self.winner = 'x'
                self.x_score += 1
                writefile = open('file.txt', 'w')
                writefile.write(f'{self.x_score}\n{self.o_score}')
                writefile.close()
                self.alertwinner()

        self.checkresult()

    ##########################
    ##########################
    ##########################
    def checkresult(self):
        try:
            readfile2 = open('file.txt', 'r')
            file_line2 = readfile2.readlines()
            score_list2 = []
            for i in file_line2:
                if i == '':
                    i = '0'
                score_list2.append(int(i))
            self.x_score = score_list2[0]
            self.o_score = score_list2[1]
            self.result_label1.configure(text="x : %d" % self.x_score)
            self.result_label2.configure(text="o : %d" % self.o_score)
        except:
            file = open('file.txt', 'w')
            file.write('0\n0')
            file.close()
    ##########################
    ##########################
    ##########################

    def alertwinner(self):
        if self.winner == 'x':
            messagebox.showinfo(
                'You win!', f'Congratulations, You won as {self.winner.upper()}!')
            self.play = 1
            self.clicked = []

        elif self.winner == 'o':
            messagebox.showwarning(
                'You Loose!', f'Computer won you!')
            self.play = 0
            self.clicked = []

        self.refresh()

    ########################
    ########################
    ########################
    def refresh(self):
        if len(self.clicked) >= 9:
            self.clicked = []

        self.wins = {'win1': [], 'win2': [], 'win3': [],
                     'win4': [], 'win5': [], 'win6': [], 'win7': [], 'win8': []}

        self.but1.configure(
            text='', fg='black', command=lambda: self.click('1'))
        self.but2.configure(
            text='', fg='black', command=lambda: self.click('2'))
        self.but3.configure(
            text='', fg='black', command=lambda: self.click('3'))
        self.but4.configure(
            text='', fg='black', command=lambda: self.click('4'))
        self.but5.configure(
            text='', fg='black', command=lambda: self.click('5'))
        self.but6.configure(
            text='', fg='black', command=lambda: self.click('6'))
        self.but7.configure(
            text='', fg='black', command=lambda: self.click('7'))
        self.but8.configure(
            text='', fg='black', command=lambda: self.click('8'))
        self.but9.configure(
            text='', fg='black', command=lambda: self.click('9'))

        self.setmode()

    ########################
    ########################
    ########################
    def refresh2(self):
        self.clicked = []
        self.play = 0

        self.wins = {'win1': [], 'win2': [], 'win3': [],
                     'win4': [], 'win5': [], 'win6': [], 'win7': [], 'win8': []}

        self.but1.configure(
            text='', fg='black', command=lambda: self.click('1'))
        self.but2.configure(
            text='', fg='black', command=lambda: self.click('2'))
        self.but3.configure(
            text='', fg='black', command=lambda: self.click('3'))
        self.but4.configure(
            text='', fg='black', command=lambda: self.click('4'))
        self.but5.configure(
            text='', fg='black', command=lambda: self.click('5'))
        self.but6.configure(
            text='', fg='black', command=lambda: self.click('6'))
        self.but7.configure(
            text='', fg='black', command=lambda: self.click('7'))
        self.but8.configure(
            text='', fg='black', command=lambda: self.click('8'))
        self.but9.configure(
            text='', fg='black', command=lambda: self.click('9'))

    #########################
    ######| Robot Play |#####
    ######|    with    |#####
    ######|   Person   |#####
    #########################

    def robotplay(self):
        num = self.generate()

        if self.play % 2 == 1:
            self.clicked.append(num)
            self.player = 'o'
            self.color = 'purple'

            for ind in range(1, 9):
                if num in self.ways_to_win[f'win{ind}']:
                    self.wins[f'win{ind}'].append(self.player)
            time.sleep(0.5)
            if num == 1:
                self.but1.configure(
                    text=self.player, fg=self.color, command='')
            elif num == 2:
                self.but2.configure(
                    text=self.player, fg=self.color, command='')
            elif num == 3:
                self.but3.configure(
                    text=self.player, fg=self.color, command='')
            elif num == 4:
                self.but4.configure(
                    text=self.player, fg=self.color, command='')
            elif num == 5:
                self.but5.configure(
                    text=self.player, fg=self.color, command='')
            elif num == 6:
                self.but6.configure(
                    text=self.player, fg=self.color, command='')
            elif num == 7:
                self.but7.configure(
                    text=self.player, fg=self.color, command='')
            elif num == 8:
                self.but8.configure(
                    text=self.player, fg=self.color, command='')
            elif num == 9:
                self.but9.configure(
                    text=self.player, fg=self.color, command='')

            self.play += 1
            if self.play % 2 == 0:
                self.player2 = 'x'
            else:
                self.player2 = 'o'
            self.label2.configure(text=f"Turn: {self.player2.upper()}")

            self.checkforwin()
            if len(self.clicked) >= 9:
                time.sleep(1)
                self.refresh()

        else:
            self.player = 'x'
            self.color = 'blue'

    ########################
    ########################
    ########################
    def generate(self):
        file = open('mode.txt', 'r')
        line = file.readlines()

        mode = int(line[0])
        file.close()

        num = 11
        if len(self.clicked) >= 0:
            for x in range(1, 9):
                if self.wins[f'win{x}'].count('x') == 0:
                    if self.ways_to_win[f'win{x}'][random.randint(0, 2)] not in self.clicked:
                        num = self.ways_to_win[f'win{x}'][random.randint(0, 2)]

            for i in range(1, 9):
                if self.wins[f'win{i}'].count('x') == 2:
                    for n in self.ways_to_win[f'win{i}']:
                        if n not in self.clicked:
                            if mode == 3:
                                num = n

            for i in range(1, 9):
                if self.wins[f'win{i}'].count('o') == 2:
                    for n in self.ways_to_win[f'win{i}']:
                        if n not in self.clicked:
                            if mode == 2:
                                num = n

        if num == 11:
            list_no = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            if len(self.clicked) > 0:
                lent = len(self.clicked)
                ran = random.randint(0, lent-1)
                ran_click = self.clicked[ran]
                prob = {
                    'list1': [2, 3, 6, 7, 5, 9], 'list2': [1, 3, 5, 8],
                    'list3': [1, 2, 4, 9, 5, 7], 'list4': [6, 5, 3, 9],
                    'list5': [6, 4, 2, 8, 1, 9, 3, 7], 'list6': [5, 4, 1, 7],
                    'list7': [8, 9, 1, 6, 3, 5], 'list8': [7, 9, 2, 5],
                    'list9': [7, 8, 3, 4, 1, 5]
                }
                list_no = prob[f'list{ran_click}']
            left_num = []
            for i in list_no:
                if i not in self.clicked:
                    left_num.append(i)
            left_length = len(left_num)
            random_num = random.randint(0, left_length-1)
            num = left_num[random_num]

        return num

    def setmode(self):
        try:
            f = open('mode.txt', 'r')
            f_read = f.readline()
            mode_ind = int(f_read[0])-1
            mode = ['Easy', 'Hard', 'Difficult']
            mo = mode[mode_ind]
            self.label3.configure(text=f"{mo}")
            f.close()
        except:
            open('mode.txt', 'w').write('1')


#######################################
#######################################
#######################################
#######################################
#######################################
#icon = __file__.replace('tic-tac-toe.py', 'xender.ico')
root = Root()
root.title("XenderGame")
root.geometry("250x300+400+150")
root.resizable(0, 0)
#root.iconbitmap(icon)


def createmode(num):
    file = open('mode.txt', 'w')
    file.write(str(num))
    file.close()
    root.setmode()


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Easy", command=lambda: createmode(1))
filemenu.add_command(label="Hard", command=lambda: createmode(2))
filemenu.add_command(label="Difficult", command=lambda: createmode(3))
filemenu.add_separator()
filemenu.add_command(label="OneTwo Player", command="")
menubar.add_cascade(label="Menu", menu=filemenu)
root.config(menu=menubar)

if __name__ == "__main__":
    root.mainloop()

#END    