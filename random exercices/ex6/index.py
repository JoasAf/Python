sequence = input("Input a sequence of # numbers with a comma separating them: ")

lsequence = sequence.replace(" ", "").split(",")
tsequence = tuple(lsequence)

print("List:", lsequence)
print("Tuple:", tsequence)