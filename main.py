"""
DPI(Dots per Inch) is 125% which is recommended mode in window os.
Therefore position of some objects such as line may change.
"""




import sys

# Adding gui file as module
sys.path.append('./Resource')
from gui import GUI

gui = GUI()
gui.mainloop()