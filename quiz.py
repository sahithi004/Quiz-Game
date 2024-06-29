def des():
    print("This is a Technical quiz consists of 5 questions.Each question has 4 options.You have to select a option.")
    print("The questions are asked on the basis of Software Companies.")
    print("Each correct answer carries Three marks and each incorrect answer carries a negative marking of one mark.")
    print("Once you have started the Game you should play it until end.")
print("Welcome to the Quiz Game🤗")
print("Instructions of the Game:")
des()
k=input("Feels Interesting👻! Would you like to play? ")
if k.lower()!="yes":
    quit()
s=0
q=input("Who is the founder of Microsoft?\nA) Steve Henry\nB) Bill Gates\nC)Andrew Wilson\nD)Milan ")
if(q.lower()=="b"):
    print("Correct😊")
    s+=3
else:
    print("Incorrect😟! Better Luck next time")
    s-=1
q=input("Who is the founder of Apple?\nA) Steve Jobs\nB)Phil Hughes\nC) Henry Smith\nD)Simpson")
if(q.lower()=="a"):
    print("Correct😊")
    s+=3
else:
    print("Incorrect😟! Better Luck next time")
    s-=1
q=input("What does IBM stands for?\nA)International Business Machines\nB)International Business Modlel\nC)International Bureau of Machines\nD)Industry Business Model")
if(q.lower()=="a"):
    print("Correct😊")
    s+=3
else:
    print("Incorrect😟! Better Luck next time")
    s-=1
q=input("Windows is a product of?\nA)Google LLC\nB)Apple Inc\nC)Oracle Corporation\nD)None of the above")
if(q.lower()=="d"):
    print("Correct😊")
    s+=3
else:
    print("Incorrect😟! Better Luck next time")
    s-=1
q=input("What does HP stand for?\nA)Henry-Packard\nB) Hewiit-Packard\n C)Hewlett-Packard\nD)None of the above")
if(q.lower()=="c"):
    print("Correct😊")
    s+=3
else:
    print("Incorrect😟! Better Luck next time")
    s-=1
print("The Game ends.")
print("Your score is ",s)