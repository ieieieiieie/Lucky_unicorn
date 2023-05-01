# ask user if they have played before
show_instructions = input("have you played before? ").lower ()

# if yes, continue
if show_instructions == "yes" or show_instructions == "y":
  show_instructions = "yes"  
  print("program continues")

#if no, show instructions
elif  show_instructions == "no" or show_instructions == "n":
 print("show instructions")

else:
    print("please say y/n")