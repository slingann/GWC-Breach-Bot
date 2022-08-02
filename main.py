#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Facebook data breach in 2019.")

#Introduces breach
print("Would you like to learn about the 2019 Facebook data breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the letter of one of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("The phone numbers, full names, locations, some email addresses, and other details from 553 million Facebook users were stolen and posted to an amateur hacking forum. The hack was done by malicious actors and was result of a vulnerability in a feature on the platform that enabled users to find each other by phone number that was exploited.")
  
  elif topic.lower() == "b":
    print("The phone numbers, full names, locations, some email addresses, and other details of 553 million Facebook users were stolen and posted to an amateur hacking forum. The hack was done by malicious actors and was result of a vulnerability in a feature on the platform that enabled users to find each other by phone number that was exploited.")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Introduces my take

print("\nI'm excited to share my take with you. Are you ready to hear my thoughts?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to hear more about? Enter the letter of one of the following options: \n(a) relation to the CIA Triad, (b) my reaction, (c) I would like to hear your reflection, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("The 2019 Facebook data breach related most to the Confidentiality portion of the CIA Triad because malicious actors gained access to personal information related to users and their accounts and this information was published to an amateur hacking forum, compromising the confidentiality between Facebook and their users. Furthermore, Facebook did not intent to notify its users of the breach, which would have kept them in the dark while hackers were stealing and using their private information.")
  
  elif topic.lower() == "b":
    print("I disagree with the organization's response because the company had no intention of notifying its platform’s users that their data could have been breached and shared among a community of hackers. Although the stolen/breached information did not include financial information, health information, and passwords, according to Facebook, the information that was breached is quite personal and private, and users had the right to know if their personal data was in the hands of malicious actors. Seeing as over 500 million users were impacted, Facebook should have been more urgent in their response rather than attempt to hide this breach from users.")
  
  elif topic.lower() == "c":
    print("I would convince victims to take action by explaining that that their breached personal information can be used by hackers and other malicious actors to commit identity theft and gain access to one’s financial assets. It’s important to confront the companies and organizations whose data was breached and hold them as accountable for the breach as the hackers.\n\nMy advice would be to use tools like haveibeenpawned.com to check if your phone number and email address were breached and if so, through what platforms. I would additionally advise victims to change passwords to their social media, bank, email, etc. accounts to ensure that if their passwords are breached, their accounts cannot be accessed by malicious actors.")
		
  elif topic.lower() == "d":
    break  
		
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
