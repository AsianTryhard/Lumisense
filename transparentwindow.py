from Tkinter import *
from msvcrt import getch
import argparse

parser = argparse.ArgumentParser(description='Enter in hex RGB for correction.')
parser.add_argument('hexcode', metavar='colorcode', type=str, nargs='+',help='#FF00FF')
args = parser.parse_args()

root = Tk()
root.attributes('-alpha', 0.3)
root.configure(bg=args.hexcode)#"#00b6ff")
w = str(root.winfo_screenwidth())
h = str(int(root.winfo_screenheight()*.75))
root.geometry(w+"x"+h+"+-10+-50")
#print w
#print h
while True:
    Button(root,compound=BOTTOM, text="Temp_Quit", command=quit).pack(side=BOTTOM)
    root.mainloop()

def quit():
    global root
    root.destroy()

