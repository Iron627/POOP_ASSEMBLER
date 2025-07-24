from tkinter.filedialog import askopenfilename
from tkinter import Tk, Button
import assembler  

root = Tk()
root.title("POOP Assembler")

def get_poop():
    filename = askopenfilename(filetypes=[("POOP Files", "*.poop")])
    if not filename:
        return  

    with open(filename, "r") as f:
        code = f.read()
    try:
        assembled = assembler.assemble(code)
    except Exception as e:
        print(f"Assembly error: {e}")
        return

    with open(f"{filename}.pmc", "w") as out:
        for instruction in assembled:
            out.write(instruction + "\n")

button = Button(root, text="Open POOP file", command=get_poop)
button.pack()

root.mainloop()
