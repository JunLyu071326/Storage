
def cube(num):
    return num*num*num

print(cube(3))

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not(is_tall):
    print("You are a short male")
else:
    print("You are a female.")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))

#a calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid.")


#dictionaries
month_conversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print(month_conversion["Jan"])
print(month_conversion.get("Luv", "Not a valid key"))


#while loop: "while" is a loop; "if" is not.
i = 1
while i <= 10:
    print(i)
    i = i + 1
print("Done with loop")


#build a guessing game

secret_word = "giraffe"
guess = ""
while guess != secret_word:
    guess = input("Enter a word: ")

print("You win!")

#set a limit on number of trials

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter a word: ")
        guess_count = guess_count + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you lose.")
else:
    print("You win!")


#"for" loop

for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]

for index in range(len(friends)):
    print(friends[index])

#exponent function
def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result*base_num
    return result

print(raise_to_power(3, 2))


#2d lists and nested loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][2])

for row in number_grid:
    for column in row:
        print(column)

#Build a translator

#Giraffe Language
#vowels -> g
#e.g. dog -> dgg; cat -> cgt

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

#Try & except

number = float(input("Enter a number: "))
print(number)
# if a string of letters is entered, error occurs.

try:
    number = float(input("Enter a number: "))
    print(number)
except:
    print("Invalid input.")


#read files: allows you to read different files
open("2019 Payment Prep Form Lyu travel.docx", "r")
open("2019 Payment Prep Form Lyu travel.docx", "w")
open("2019 Payment Prep Form Lyu travel.docx", "a") # append or add at the end

file = open("2019 Payment Prep Form Lyu travel.docx","r")
print(file.readable())
print(file.read())
file.close()

#write to files
file = open("2019 Payment Prep Form Lyu travel.docx", "a")

file.write("\nToby - Human Resources")

file.close()

file = open("2019 Payment Prep Form Lyu travel.docx", "w")
file.write("\nToby - Human Resources") #overwrite everything in the file
file.close()

#python can be used to create html files

file = open("file.html", "w")
file.write("<p>This is HTML.</p>")
file.close()


#classes and objects
class student: #define a new class and attributes associated with it

    def __init__(self, name, major, gpa, is_on_probation): #map out what attributes the class "student" should have
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

from demo import student

student1 = student("Jim", "Business", 3.1, False) #"student" object

print(student1.name)


#BUILD A MULTIPLE CHOICE QUESTION

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Red\n(b) Yellow\n(c) Orange\n\n"
]

#make a new py file, inside it:

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

#now in demo.py

from newfile import Question

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)





























