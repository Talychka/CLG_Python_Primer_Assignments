import tkinter as tk
class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label_1 = tk.Label(self, text='Enter a password (your favourite language): ',
            fg='#ddf3f5', bg='#e36387')
        self.label_1.pack()
        self.entry_0=tk.Entry(self, show='*', bg='#ddf3f5')
        self.entry_0.pack()
        self_label_2 = tk.Label(self, fg='#a6dcef', bg='#e36387')
        self.label_2.pack()
        self.btn = tk.Button(self, text = 'submit', 
            command=self.submit)
        self.btn.pack()
        self.correct_pass = 'python'
    def submit(self):
        self,pswd = self.entry_0.get()
        if self.pswd == self.correct_pass:
            self.label_2['text'] = 'Congratulations!'
        else:
            self.label_2['text'] = 'Try again!'
        
if __name__ == '__main__':
    root = Root()
    root['bg'] = '#e36387'
    root.mainloop()
