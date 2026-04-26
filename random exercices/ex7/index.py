print("File extension detector")

filename = input("Input a filename: ")


extension = filename.rsplit(".",)[1]

print("File extension:", extension)