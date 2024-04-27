import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.label_1 = tk.Label(self, text="Please enter any password you like (just for fun, try making it a palindrome - that's a word that is the spelled the same forwards and backwards, like 'bob'): ",
                                fg="#009193", bg="#E9FEFC")
        self.label_1.pack()
        
        self.entry_0=tk.Entry(self, show='*', fg="#009193", bg="#E9FEFC")
        self.entry_0.pack()
        
        self.label_2=tk.Label(self, fg="#009193", bg="#E9FEFC")
        self.label_2.pack()
        
        self.btn = tk.Button(self, text = 'submit', 
            command=self.submit)
        self.btn.pack()
    
    def is_palindrome(self, user_password):
        user_password = user_password.lower()
        letters_in_word = list(user_password)
        reversed_word=letters_in_word[::-1]
        is_palindrome = letters_in_word == reversed_word
        return(is_palindrome)

    def submit(self):
        self.pswd = self.entry_0.get()
        if self.is_palindrome(self.pswd) is True:
            self.label_2["text"] = "Well done you clever thing - you created a palindrome password!"
        else:
            self.label_2["text"] = "Unfortunately, that password is not a palindrome. Wouldn't it have been fun if it was?! Better luck next time!"
        

if __name__ == '__main__':
    root = Root()
    root.title("The Palindrome Password Program - PPP!")
    root.geometry("1200x400")
    root['bg'] = '#FFF2CC'
    root.mainloop()