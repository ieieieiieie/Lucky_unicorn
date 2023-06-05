def num_check(question, low, high):
  error = "please choose a whole number between 1 and 10/n"  

  valid = False
  while not valid:
   try:

      response = int(input(question))

      if low < response <= high:
          return response
        

      else: 
       print(error)
        
   except ValueError:
    print(error)

how_much = num_check("how much will you be playing with? ", 0, 10)

print("you will be spending ${}!".format(how_much))