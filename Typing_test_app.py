import tkinter as tk
from time import time
import random
text = ["he sun dipped below the horizon, painting the sky in hues of orange and pink.",
        " Birds chirped softly as the wind rustled through the trees.",
        " A gentle breeze carried the scent of blooming jasmine, filling the air with sweetness. Children laughed in the distance, ",
        "chasing fireflies under the fading light. Time seemed to pause, caught between day and night.",
        " Somewhere nearby, a dog barked lazily. The world felt calm, at peace. ",
        "Moments like this reminded her of summer evenings from childhood—carefree and magical. She smiled",
        " knowing tomorrow would bring new stories", 
        "but tonight was perfect in its quiet simplicity."]
class Typingapp:
    def __init__(self, root):
        self.root= root
        self.root.title("Typing test")
        self.sample_text= random.choice(text)
        self.start_time=None

        self.label=tk.Label(root,text="Type the text below:",font=("Arial", 15))
        self.label.pack(pady=10)
        self.text_label=tk.Label(root ,text=self.sample_text,font=("Arial",15),wraplength=1000)
        self.text_label.pack(pady=10)
        self.entry=tk.Entry(root,font=("Arial",14),width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>",self.start_timer)
        self.entry.bind("<Return>",self.check_result)
        self.result_label=tk.Label(root , text="",font=("Arial",14))
        self.result_label.pack(pady=10)
        self.resetbutton=tk.Button(root,text="Reset",command=self.reset)
        self.resetbutton.pack(pady=10)
    def start_timer(self , event):
        if self.start_time is None:
            self.start_time= time()
    def check_result(self , event):
        end_time= time()
        type_text=self.entry.get()  
        time_taken=end_time- self.start_time
        word=len(type_text.split())
        wpm=word/(time_taken/60) 
        correct_char=sum(1 for a,b in zip(type_text,self.sample_text)if a==b)   
        accuracy=(correct_char/len(self.sample_text)*100)
        self.result_label.config(
            text=f"wpm:{wpm:.2f}\nAccuracy:{accuracy:.2f}%\nTimetaken:{time_taken:2f}s"
        )
    def reset(self):
        self.sample_text=random.choice(text)
        self.text_label.config(text=self.sample_text)
        self.entry.delete(0,tk.END)
        self.result_label.config(text="")
        self.start_time=None
root=tk.Tk()    
typingapp=Typingapp(root)
root.mainloop()
