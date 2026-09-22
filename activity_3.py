print("Select your ride")
print("1 bike")
print("2 car")
choice = int(input("Enter your choice"))
if choice == 1:
  print("What type of bike you want")
  print("1 Scooter or 2 Scooty")
  choice2 = int(input("Enter your choice two"))
  if choice2 == 1:
    print("You have selected scooter")
  else:
    print("You have selected scooty")
else:
  print("What car do you want")
  print("1 honda or 2 toyota")
  choice3 = int(input("Enter your choice three "))
  if choice3 == 1:
    print("You have selected Honda")
  else:
    print("You have selected toyota")