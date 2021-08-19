#i was thinking how can i link my dopamine with programming, get back to programming and learn datascience, machine learning, and make myself expert in everything that i come across
# what is stopping me? What are the things that are stopping me 
# this is the question that i am searching the answer

print('dopamine research')
import numpy as np
#lets build a little game to get back to what i am missing for quite long time

guess_numbers = [1,2,3,4,5,6,7,8,9,10]
guessed_number = np.random.choice(guess_numbers)
if guessed_number%2 == 0:
    print("It seems the number is even")
else:
    print("Well the number seems to be odd try to guess it")
user_input = int(input("Enter a number: "))
score = 0
if user_input == guessed_number:
    score = score+1
    print("You guess corrected :)")
    print("Your score is : "+str(score))
else:
    print("sorry try again :(")
