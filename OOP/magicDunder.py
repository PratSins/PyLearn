class Book():
    def __init__(self,title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__ (self): # this function is not needed for th edeltion of object
        # this function is only created when the coder wants to get certain tasks done b4 deletion...
        print("A book object has been deleted")



b = Book("Python Rocks", "Pratyush Singh", 587)

print(b) # invokes __str__ function
print(str(b))
print("Lenght of b - ",len(b)) # invokes __len__ func

del b # deletes object -b-
