try:
    f = open("file.txt")
except FileNotFoundError as et:
    print(et)
except Exception as et:
    print(et)
else:
    print(f.read())
    f.close()
finally:
    print("Sucessful")
