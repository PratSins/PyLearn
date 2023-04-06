def func():
    print("\n**Hello!**\n")

func()
print(func)

greet = func
greet()

del func
# func()  # error
greet()
