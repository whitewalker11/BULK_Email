from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

file = ''
INPUT = ''


def final_ui():
    global file
    global INPUT


    def Take_input():
        global INPUT
        INPUT = inputtxt.get("1.0", "end-1c")
        print(INPUT)

        root.destroy()

    def open_file():
        global file
        file = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("csv files",
                                                      "*.csv*"),
                                                     ("all files",
                                                      "*.*")))
        if file is not None:
            lm = Label(text="file opend:" + file, bg="white", fg="black", font=("Arial", 9, "bold"), width=68, height=3)
            lm.place(x=100, y=200)
            #content = file.read()
            print(file)

    root = Tk()
    master = root.frame()
    background = '#303030'
    background2 = '#305035'

    root.geometry('700x750')
    root.title("Bulk Email Automation")
    root.configure(bg=background, bd=0)

    logo_image = ImageTk.PhotoImage(Image.open(r'widgets/logo.png'))
    il = Label(root, bg=background, image=logo_image)
    tl = Label(root, text="SEND BULK MAIL", bg=background,
               fg="skyblue", font=("Arial", 24, "bold"))
    il.place(x=250 - 80, y=10)
    tl.place(x=400 - 130, y=29)

    l_csv = Label(text="Select your Excel sheet", bg=background2, fg="white", font=("Arial", 9, "bold"))
    l_csv.place(x=130, y=160)
    upload_image = ImageTk.PhotoImage(Image.open('widgets/open_file.png'))
    ui = Label(root, bg=background, image=upload_image)
    ui.place(x=90, y=150)

    btn = Button(root, text="Browse file", bg=background,
                 fg="white", font=("Arial", 8, "bold"), command=lambda: open_file())

    print("qqqq")
    l = Label(text="Write your message for email", bg=background2, fg="white", font=("Arial", 8, "bold"))

    inputtxt = Text(root, height=15,
                    width=60,
                    bg="light yellow")

    Display = Button(root, height=3,
                     width=20,
                     text="SEND",
                     command=lambda: Take_input())

    l.place(x=100, y=548 - 200)
    btn.place(x=95, y=187)
    inputtxt.place(x=100, y=570 - 200)
    Display.place(x=250, y=548 + 100)
    # Output.pack()

    mainloop()
    print(INPUT)
    return (file,INPUT)


