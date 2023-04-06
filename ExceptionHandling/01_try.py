while(True):
    print("\nPress q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        print("Trying...")
        a = int(a)
        print("-Successful type conversion ---> a = ",a)
    except Exception as e:
        print(f">>Your input resulted in an error: {e}")
    else:
        print("--No exception--")
    finally:
        print("--Executes With/Without Exception--")

print("\n-----------Thanks for playing this game---------------\n")