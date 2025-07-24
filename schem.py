from os.path import basename
import mcschematic
from tkinter.filedialog import askopenfilename
from tkinter import Tk, Button
codeschem = mcschematic.MCSchematic()
root = Tk()
root.title("POOP SchemConverter")
zcounter = 0 
ycounter = 0
def get_poop():
    filename = askopenfilename(filetypes=[("PMC Files", "*.pmc")])
    if not filename:
        return  
    with open(filename, "r") as f:
        code = f.read()
        code = code.splitlines()
        print(code)
        makeschem(code)
        codeschem.save( "programs", f"{basename(filename)}", mcschematic.Version.JE_1_20_4)
        print("done")

def makeschem(code):
    global zcounter, ycounter
    instruction_num = 0  
    for i in range(len(code)):
        for j in code[i]:
            if j == "1":
                if instruction_num >= 192:
                    x = 10
                    facing = "west"
                elif instruction_num >= 128:
                    x = 2
                    facing = "east"
                elif instruction_num >= 64:
                    x = 12
                    facing = "east"
                else:
                    x = 0
                    facing = "west"
                if instruction_num == 192 or instruction_num == 128 or instruction_num == 64:
                    zcounter = 0
                codeschem.setBlock((x, ycounter, zcounter), f"repeater[facing={facing}]")
            elif j == "0":
                if instruction_num >= 192:
                    x = 10
                    facing = "west"
                elif instruction_num >= 128:
                    x = 2
                    facing = "east"
                elif instruction_num >= 64:
                    x = 12
                    facing = "east"
                else:
                    x = 0
                    facing = "west"
                if instruction_num == 192 or instruction_num == 128 or instruction_num == 64:
                    zcounter = 0
                codeschem.setBlock((x, ycounter, zcounter), "stone")
            ycounter -= 2

        instruction_num += 1
        if (((i + 1) % 8) == 0):
            zcounter += 3
        else:
            zcounter += 2
        ycounter = 0
button = Button(root, text="Open PMC file", command=get_poop)
button.pack()

root.mainloop()
