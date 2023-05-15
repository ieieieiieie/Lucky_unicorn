show_instructions = ""
while show_instructions.lower() !="xxx":
  #input prompt
  show_instructions = input("have you played before? ").lower()
  
  #yes options
  if show_instructions == "yes" or show_instructions == "y":
    show_instructions = "yes"
    print("program continues")
  
  #no options
  elif show_instructions == "no" or show_instructions == "n":
    show_instructions = "no"
    print("instructions displayed")
  
  #error message
  else: print("please answer y / n")
   
print()
print("you chose xxx")