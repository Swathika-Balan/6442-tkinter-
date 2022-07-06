#!/usr/bin/env python
# coding: utf-8

# In[41]:


from tkinter import * 
import tkinter as tk
from tkinter import filedialog as fd
import os
#tk.Label
root = tk.Tk()
root.title("Swati_tkinter")

def open_program():
    my_program= fd.askopenfilename()
    my_label.config(text= my_program)
    #open program
    os.system('"%s"' % my_program)
    
my_label= Label(root,text="")
my_label.grid(pady=20)  
    

#l1=Label(root,text="hello world",bg="yellow",fg="blue",font=("Arial")).grid(column=5000,row=0)
b1=Button(root,text="Images", command=open_program)
b1.grid(pady=20)


b2=Button(root,text="Preprocessing o/p")
b2.grid(pady=40)

b3=Button(root,text=" Segmentation output")
b3.grid(pady=50)

b4=Button(root,text="Result output.")
b4.grid(pady=70)


root.mainloop()


# In[38]:




import tkinter as tk

root = tk.Tk()


# In[6]:


root


# In[8]:


root.title("Swati_tkinter")


# In[9]:




