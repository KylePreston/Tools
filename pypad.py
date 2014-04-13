# When this is finished, it will be a notepad app which the user can open, edit, write, and/or delete text files.
import Tkinter as tk

root = tk.Tk()

# myMenu = tk.Menu(root)
menuBar = tk.Menu(root)
# We've created a menuBar above, now we will add menu tabs to it.
# We pass Menu the menuBar parameter because we want it to be
# zee parent yeah?
fileMenu = tk.Menu(menuBar)
# We've created the fileMenu and now it is a child of menuBar.
# Now we can call it when we create a new hierarchical menu below.
menuBar.add_cascade(label='File', menu=fileMenu)

editMenu = tk.Menu(menuBar)
menuBar.add_cascade(label='Edit', menu=editMenu)

# Here is where your LPTHW is paying off. 
# 'Instantiate a viewMenu that is a menuBar'
viewMenu = tk.Menu(menuBar)
menuBar.add_cascade(label='View', menu=viewMenu)

aboutMenu = tk.Menu(menuBar)
menuBar.add_cascade(label='About', menu=aboutMenu)

# This step is needed to asctually display the menu bar
root.config(menu=menuBar)
root.mainloop()
