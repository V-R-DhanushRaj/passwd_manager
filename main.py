import sys

# Adding gui file as module
sys.path.append('./Resource')
from gui import GUI

gui = GUI()
gui.mainloop()