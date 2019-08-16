# SpyPet - a combination of the "Screen Pet" and "Secret Messages" project
# from "Computer Coding Python Projects", DK books
# Double-click the pet to make it stick its tongue out
# Move the mouse over it to pat it and keep it happy
# Shift-Up-arrow triggers the spy mode
# Claire Quigley, November 2017


from tkinter import HIDDEN, NORMAL, Tk, Canvas
from tkinter import messagebox, simpledialog, Tk

#screen pet code

def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_colour if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)


def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)


def toggle_pupils():
    if not c.eyes_crossed:
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False


def toggle_tongue():
    if not c.tongue_out:
        c.itemconfigure(tongue_tip, state=NORMAL)
        c.itemconfigure(tongue_main, state=NORMAL)
        c.tongue_out = True
    else:
        c.itemconfigure(tongue_tip, state=HIDDEN)
        c.itemconfigure(tongue_main, state=HIDDEN)
        c.tongue_out = False


def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    root.after(1000, toggle_tongue)
    root.after(1000, toggle_pupils)
    return

def wear_disguise():
    c.itemconfigure(eye_left, state=HIDDEN)
    c.itemconfigure(eye_right, state=HIDDEN)
    c.itemconfigure(hat, state=NORMAL)
    c.itemconfigure(hat_band, state=NORMAL)
    c.itemconfigure(sunglasses_left, state=NORMAL)
    c.itemconfigure(sunglasses_bar, state=NORMAL)
    c.itemconfigure(sunglasses_right, state=NORMAL)
    
    return

def remove_disguise():
    c.itemconfigure(eye_left, state=NORMAL)
    c.itemconfigure(eye_right, state=NORMAL)
    c.itemconfigure(hat, state=HIDDEN)
    c.itemconfigure(hat_band, state=HIDDEN)
    c.itemconfigure(sunglasses_left, state=HIDDEN)
    c.itemconfigure(sunglasses_bar, state=HIDDEN)
    c.itemconfigure(sunglasses_right, state=HIDDEN)
    return

def show_happy(event):
   # print(event.x, event.y)
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(mouth_happy, state=NORMAL)

        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
        c.happy_level = 10
        root.focus()
    return


def hide_happy(event):
    c.itemconfigure(cheek_left, state=HIDDEN)
    c.itemconfigure(cheek_right, state=HIDDEN)
    c.itemconfigure(mouth_happy, state=HIDDEN)
    c.itemconfigure(mouth_normal, state=NORMAL)
    c.itemconfigure(mouth_sad, state=HIDDEN)
    c.happy_level = 10
    return


def sad():
    if c.happy_level == 0:
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=NORMAL)
    else:
        c.happy_level -= 1
    root.after(5000, sad)



# secret messages code

def is_even(number):
    return number % 2 == 0


def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters


def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters


def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message) / 2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message


def get_task():
    task = simpledialog.askstring('Task', 'Do you want Spy Pet to encrypt or decrypt?')
    #task.place(x=300, y=600)
    return task


def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message

def launch_spy_mode(event):
    wear_disguise()
    while True:
        task = get_task()
        if task == 'encrypt':
            message = get_message()
            encrypted = swap_letters(message)
            messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
        elif task == 'decrypt':
            message = get_message()
            decrypted = swap_letters(message)
            messagebox.showinfo('Plaintext of the secret message is:', decrypted)
        else:
            remove_disguise()
            break
    return

# main section
root = Tk()
c = Canvas(root, width=400, height=400)
c.configure(bg='dark blue', highlightthickness=0)
c.body_colour = 'SkyBlue1'
body = c.create_oval(35, 40, 365, 380, outline=c.body_colour, fill=c.body_colour)
ear_left = c.create_polygon(75, 100, 75, 30, 165, 90, outline=c.body_colour, fill=c.body_colour)
ear_right = c.create_polygon(255, 65, 325, 30, 320, 100, outline=c.body_colour, fill=c.body_colour)
foot_left = c.create_oval(65, 340, 145, 380, outline=c.body_colour, fill=c.body_colour)
foot_right = c.create_oval(250, 340, 330, 380, outline=c.body_colour, fill=c.body_colour)

eye_left = c.create_oval(130, 130, 160, 190, outline='black', fill='white')
pupil_left = c.create_oval(140, 165, 150, 175, outline='black', fill='black')
eye_right = c.create_oval(230, 130, 260, 190, outline='black', fill='white')
pupil_right = c.create_oval(240, 165, 250, 175, outline='black', fill='black')

mouth_normal = c.create_line(170, 270, 200, 292, 230, 270, smooth=1, width=2, state=NORMAL)
mouth_happy = c.create_line(170, 270, 200, 302, 230, 270, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(170, 270, 200, 252, 230, 270, smooth=1, width=2, state=HIDDEN)
tongue_main = c.create_rectangle(170, 270, 230, 310, outline='red', fill='red', state=HIDDEN)
tongue_tip = c.create_oval(170, 305, 230, 320, outline='red', fill='red', state=HIDDEN)

cheek_left = c.create_oval(70, 200, 120, 250, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.create_oval(280, 200, 330, 250, outline='pink', fill='pink', state=HIDDEN)


hat_points = [110,40,165,45,175,8, 195,20, 215, 8, 240,45, 290,40, 195,90]
hat_band_points = [165,40, 195, 57, 240, 40]

hat = c.create_polygon(hat_points, outline='tan', fill='tan', width=2,state=HIDDEN)
hat_band = c.create_polygon(hat_band_points, outline='black' , fill='black', width=2,state=HIDDEN)
sunglasses_left = c.create_arc(115,100, 185, 190, start= 180, extent=180,fill= 'black', outline= 'black',state=HIDDEN)
sunglasses_right = c.create_arc(210,100, 280, 190, start= 180, extent=180,fill= 'black', outline= 'black',state=HIDDEN)
sunglasses_bar = c.create_line(186, 146, 210, 146, fill= 'black',state=HIDDEN)

c.pack()

root.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
c.bind('<Double-1>', cheeky)
root.bind('<Shift-Up>', launch_spy_mode)

c.happy_level = 10
c.eyes_crossed = False
c.tongue_out = False

root.after(1000, blink)
root.after(5000, sad)
root.mainloop()
