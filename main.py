# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2

lowered_case_string = combined_names.lower()

t = lowered_case_string.count("t")
r = lowered_case_string.count("r")
u = lowered_case_string.count("u")
e = lowered_case_string.count("e")

true = t + r + u + e

l = lowered_case_string.count("l")
o = lowered_case_string.count("o")
v = lowered_case_string.count("v")
e = lowered_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))


if (love_score < 10) or (love_score > 90):
  print(f"Your love score is{love_score} , you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is{love_score} , you are alright together.")
else:
  print(f"Your score is{love_score}")

