# NOT READY FOR USE!!!!
import Tkinter as tk

root = tk.Tk()
root.title('PyPad')
root.geometry('800x800')

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
	textPad.event_generate('<<Undo>>')
def redo_action():
	textPad.event_generate('<<Redo>>')
def cut_action():
	textPad.event_generate('<<Cut>>')
def copy_action():
	textPad.event_generate('<<Copy>>')
def paste_action():
	textPad.event_generate('<<Paste>>')
def find_action():
	pass
def selectAll_action():
	pass

# Define your image icons
newicon = tk.PhotoImage(file='icons/newfile.gif')
openicon = tk.PhotoImage(file='icons/open.gif')
saveicon = tk.PhotoImage(file='icons/jesus.gif')
undoicon = tk.PhotoImage(file='icons/undo.gif')
redoicon = tk.PhotoImage(file='icons/redo.gif')
cuticon = tk.PhotoImage(file='icons/sting.gif')
copyicon = tk.PhotoImage(file='icons/copy.gif')
pasteicon = tk.PhotoImage(file='icons/paste.gif')

# Create a main row for the menu
menuBar = tk.Menu(root)
menuBar.add_cascade(label='PyPad')

# File Menu
fileMenu = tk.Menu(menuBar)
# Displays the column needed to see the add_commands
menuBar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', accelerator='Command+N', compound=tk.LEFT,
					 image=newicon, underline=0, command=new_file)
fileMenu.add_command(label='Open', accelerator='Command+O', compound=tk.LEFT,
					 image=openicon, underline=0, command=open_file)
fileMenu.add_command(label='Save', accelerator='Command-S', compound=tk.LEFT,
					 image=saveicon, underline=0, command=save_file)
fileMenu.add_command(label='Save as', accelerator='Shift+Command+S', command=save_file_as)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', accelerator='Command+W', command=exit_program)

# Edit menu
editMenu = tk.Menu(menuBar)
menuBar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Undo', accelerator='Command+Z', compound=tk.LEFT,
					image=undoicon, underline=0, command=undo_action)
editMenu.add_command(label='Redo', accelerator='Shift-Command+Z', compound=tk.LEFT,
					 image=redoicon, underline=0, command=redo_action)
editMenu.add_command(label='Cut', accelerator='Command+X', compound=tk.LEFT,
					 image=cuticon, underline=0, command=cut_action)
editMenu.add_command(label='Copy', accelerator='Command-C', compound=tk.LEFT,
					 image=copyicon, underline=0, command=copy_action)
editMenu.add_command(label='Paste', accelerator='Command+V', compound=tk.LEFT,
					 image=pasteicon, command=paste_action)
editMenu.add_separator()
editMenu.add_command(label='Find', accelerator='Command+F', command=find_action)
editMenu.add_command(label='Select all', accelerator='Command+A', command=selectAll_action)

# View Menu
viewMenu = tk.Menu(menuBar)
menuBar.add_cascade(label='View', menu=viewMenu)
# Capture and create showLine, an instance of class IntVar
showLine = tk.IntVar()
# Set the initial value
showLine.set(1)
viewMenu.add_checkbutton(label='Show line number', variable=showLine)
showInBar = tk.IntVar()
showInBar.set(1)
viewMenu.add_checkbutton(label='Show info bar at bottom', variable = showInBar)
highlight = tk.IntVar()
viewMenu.add_checkbutton(label='Highlight current line', onvalue=1, offvalue=0, variable=highlight)
# A Theme Menu cascaded inside the view menu
themeMenu = tk.Menu(menuBar)
viewMenu.add_cascade(label='Themes', menu=themeMenu)
# Theme choices
themeSelection = {
'1. Default White': 'FFFFFF',
'2. Greygarious Grey':'D1D4D1',
'3. Lovely Lavender':'E1E1FF' , 
'4. Aquamarine': 'D1E7E0',
'5. Bold Beige': 'FFF0E1',
'6. Cobalt Blue':'333AA',
'7. Olive Green': '5B8340'
}
themeChoice = tk.StringVar()
themeChoice.set('1. Default White')
[themeMenu.add_radiobutton(label=i, variable=themeChoice) for i in sorted(themeSelection)]

# About Menu
aboutMenu = tk.Menu(menuBar)
menuBar.add_cascade(label='About', menu=aboutMenu)
aboutMenu.add_command(label='About')
aboutMenu.add_command(label='Help')

# The top shortcut bar
shortcutBar = tk.Frame(root, height=64, bg='#019875')
shortcutBar.pack(expand=tk.NO, fill=tk.X)

# Line label bar
lineLabelBar = tk.Label(root, width=2, bg='antique white')
lineLabelBar.pack(side=tk.LEFT, anchor='nw', fill=tk.Y)

# The text box
textPad = tk.Text(root, font='Helvetica', undo=True)
textPad.pack(expand=tk.YES, fill=tk.BOTH)

# The scroll bar, whose parent is textPad
scrollBar = tk.Scrollbar(textPad)
textPad.configure(yscrollcommand=scrollBar.set)
# need to dispaly the scroll bar
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
# Display the menu bar
root.config(menu=menuBar)
root.mainloop()
