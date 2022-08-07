import imaplib
from tkinter.tix import INTEGER


finelist = [i for i in INTEGER]
list = [a for a in finelist]

def sort_nested_lists (list):
 for finelist in list:
    x = sum(finelist)
    x = sorted(list)
    return x
print (sort_nested_lists)