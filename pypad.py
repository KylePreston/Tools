# NOT READY FOR USE!!!!!!
import Tkinter as tk

root = tk.Tk()
root.title('PyPad')

# Functions
def new_file():
	pass
def open_file():
	pass
def save_file():
	pass
def save_file_as():
	pass
def exit_program():
	pass
def undo_action():
	pass
def redo_action():
	pass
def cut_action():
	pass
def copy_action():
	pass
def find_action():
	pass
def selectAll_action():
	pass
# Define your icons
newicon = tk.PhotoImage(file='icons/newfile.gif')
openicon = tk.PhotoImage(file='icons/open.gif')
saveicon = tk.PhotoImage(file='icons/jesus.gif')
undoicon = tk.PhotoImage(file='icons/undo.gif')
redoicon = tk.PhotoImage(file='icons/redo.gif')
cuticon = tk.PhotoImage(file='icons/sting.gif')
copyicon = tk.PhotoImage(file='icons/copy.gif')

# Create a main row for the menu
menuBar = tk.Menu(root)
menuBar.add_cascade(label='PyPad')

# File Menu
fileMenu = tk.Menu(menuBar)
# We've created the fileMenu and now it is a child of menuBar.
# Now we can call it when we create a new hierarchical menu below.
# using menuBar.add_cascade
# fileMenu.add_command(label='New', accelerator='Ctrl+N', compound=tk.LEFT, image=newicon, underline=0)
fileMenu.add_command(label='New', accelerator='Command+N', compound=tk.LEFT,
					 image=newicon, underline=0, command=new_file)
fileMenu.add_command(label='Open', accelerator='Command+O', compound=tk.LEFT,
					 image=openicon, underline=0, command=open_file)
fileMenu.add_command(label='Save', accelerator='Command-S', compound=tk.LEFT,
					 image=saveicon, underline=0, command=save_file)
fileMenu.add_command(label='Save as', accelerator='Shift+Command+S', command=save_file_as)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', accelerator='Command+W', command=exit_program)
# This displays the actual column. Needed to see all the add_commands
menuBar.add_cascade(label='File', menu=fileMenu)

# Edit menu
editMenu = tk.Menu(menuBar)
editMenu.add_command(label='Undo', accelerator='Command+Z', compound=tk.LEFT,
					 image=undoicon, underline=0, command=undo_action)
editMenu.add_command(label='Redo', accelerator='Shift-Command+S', compound=tk.LEFT,
					 image=redoicon, underline=0, command=redo_action)
editMenu.add_command(label='Cut', accelerator='Command+X', compound=tk.LEFT,
					 image=cuticon, underline=0, command=cut_action)
editMenu.add_command(label='Copy', accelerator='Command-C', compound=tk.LEFT,
					 image=copyicon, underline=0, command=copy_action)
editMenu.add_separator()
editMenu.add_command(label='Find', accelerator='Command+F', command=find_action)
editMenu.add_command(label='Select all', accelerator='Command+A', command=selectAll_action)
menuBar.add_cascade(label='Edit', menu=editMenu)

# View Menu
viewMenu = tk.Menu(menuBar)
menuBar.add_cascade(label='View', menu=viewMenu)

aboutMenu = tk.Menu(menuBar)
menuBar.add_cascade(label='About', menu=aboutMenu)

# Display the menu bar
root.config(menu=menuBar)
root.mainloop()
