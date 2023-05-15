show_instructions = ""
while show_instructions.lower() !="xxx":
  #input prompt
  show_instructions = input("have you played before? ").lower()
  
  #yes options
  if show_instructions == "yes":
    print("program continues")
  
  elif show_instructions == "y":
    print("program continues")
  
  #no options
  elif show_instructions == "no":
    print("instructions displayed")
  
  elif show_instructions == "n":
    print("instructions displayed")
  
  #error message
  else: print("please answer y / n")
   
print()
print("you chose xxx")