while True :
  print("\U0001F31F Welcome to the Stage Name Generator \U0001F31F")
  firstName = input("What's your favourite color? ")
  lastName = input("What's your pet's name? ")
  print("Your stage name could be " + firstName.capitalize() + " " + lastName.capitalize() + "\n" )

  while True:
    restart = input("Do you want to create another stage name?  (y/n): ")
    if restart in ("y", "n"):  
      break
      # print("Invalid input")
  if restart == "y":
    continue
  else:
    print("Thanks for using the Apps, Good Day !")
    break