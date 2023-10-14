# def introduce_yourself(name , family):
#     return f"Hello my name id {name} and my family is {family}"

# def introduce_yourself(name:str , family = "Mokhtari") -> str:
#     return f"Hello my name is {name} and my family is {family}"

# def introduce_yourself(name = "Farangis" , family = "Mokhtari") -> str:
#     return f"Hello my name is {name} and my family is {family}"

def introduce_yourself(family , name = "Farangis" ) -> str:
    return f"Hello my name is {name} and my family is {family}"


# result = introduce_yourself("Hamzeh" , "Qorbani")
# print(result)

# result = introduce_yourself("Qorbani" , "Hamzeh")
# print(result)

# result = introduce_yourself(family = "Qorbani" , name = "Hamzeh")
# print(result)

result = introduce_yourself("Mokhtari")
print(result)
