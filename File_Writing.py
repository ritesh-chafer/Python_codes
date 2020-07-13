# f = open("Demo.txt", "a")
# a = f.write("Adding new line\n") #returns no. of character written
# print(a)
# f.close()


# Handle read and write both
f = open("Demo.txt", "r+")
print(f.read())
f.write("Thank you")
f.close()