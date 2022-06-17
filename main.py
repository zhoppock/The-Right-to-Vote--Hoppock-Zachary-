print("Welcome to the 2019 California Voter Registration Application.")
print("Please enter your full name to begin. \n")
firstName = input("What is your first name? ")
middleName = input("What is your middle name? ")
lastName = input("What is your last name? ")
fullName = (firstName + " " + middleName + " " + lastName)
print("\n")
print("Thank you,", fullName + ". \n")
print("We will now ask you some preliminary questions to determining if you are eligible to vote: \n")

citizenship = input("Are you currently a resident of the United States of America? ")
if citizenship == "yes" or citizenship == "Yes":
  print("Thank you for your input so far, " + firstName + ". \n")
  state = input("Are you currently a resident in the state of California? ")
  if state == "yes" or state == "Yes":
    print("Thank you for your input so far, " + firstName + ". \n")
    over18 = input("Are you over the age of 18? ")
    if over18 == "yes" or over18 == "Yes":
      legalYear = 2002
      birthYear = input("Please confirm your year of birth. ")
      birthYear = int(birthYear)
      if birthYear <= legalYear:
        print("Thank you for your input so far, " + firstName + ". \n")
        conviction = input("Are you about to face prison time for the conviction of a felony or are currently serving parole for the conviction of a felony? ")
        if conviction == "no" or conviction == "No":
          print("Thank you for your input so far, " + firstName + ". \n")
          mentalCondition = input("Lastly, have you been deemed by a court to be mentally incompetent? ")
          if mentalCondition == "no" or mentalCondition == "No":
            print("Thank you for your input, " + firstName + ". \n")
            print("Based upon the answers you have given us, " + fullName + ", we have determined that you are eligible to vote in the state of California.  Congratulations.")
          elif mentalCondition == "yes" or mentalCondition == "Yes":
            print("Based upon your response of Yes, we have determined that you are not eligible to vote in the state of California at this time.")
          else:
            print("Your response was not recognized.  Please refresh this form to try again.")
        elif conviction == "yes" or conviction == "Yes":
          print("Based upon your response of Yes, we have determined that you are not eligible to vote in the state of California at this time.")
        else:
          print("Your response was not recognized.  Please refresh this form to try again.")
      elif birthYear > legalYear:
        print("Based upon the year you have inputed, we have determined that you are not eligible to vote in the state of California at this time.")
      else:
        print("Your input was not recognized.  Please refresh this form to try again.")
    elif over18 == "no" or over18 == "No":
      print("Based upon your response of No, we have determined that you are not eligible to vote in the state of California at this time.")
    else:
      print("Your response was not recognized.  Please refresh this form to try again.")
  elif state == "no" or state == "No":
    print("Based upon your response of No, we have determined that you are not eligible to vote in the state of California at this time.")
  else:
    print("Your response was not recognized.  Please refresh this form to try again.")
elif citizenship == "no" or citizenship == "No":
  print("Based upon your response of No, we have determined that you are not eligible to vote in either the state of California or the United States of America at this time.")
else:
  print("Your response was not recognized.  Please refresh this form to try again.")