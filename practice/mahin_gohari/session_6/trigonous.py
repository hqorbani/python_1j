A = int(input("please enter number greater than 0:"))
B = int(input("please enter number greater than 0:"))
C = int(input("please enter number greater than 0:"))
if A == B >= C and B == C:
    print("mosalas mosavi ast ba motasavi azla:")
elif A == B and B != C:
    print("mosalas mosavi ast ba motasavi saghain:")
elif C == B and A != C:
    print("mosalas mosavi ast ba motasavi saghain:")
elif A == C and A != B:
    print("mosalas mosavi ast ba motasavi saghain:")
else:
    print("an meghyas ast:")