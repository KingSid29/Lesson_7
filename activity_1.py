medical_cause = input("Do you have a medical cause (Y/N)").strip().upper()
if medical_cause == 'Y':
  print("You are allowed")
else:
  attendence = int(input("Enter your attendence"))
  if attendence >= 75:
    print("You are allowed")
  else:
    print("Your are not allowed ")
    