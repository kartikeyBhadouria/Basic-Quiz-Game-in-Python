def banner():
    print('\033[1m' + '################ QUIZ EXAM ################')

userDetails=[]
def userdetails():
    global userDetails
    print("*" * 10, "User Details", "*" * 10)
    print()
    name = input("Enter your Name: ")
    contact = input("Enter your Contact: ")
    userDetails.append([name, contact])
    print()
    print("Welcome",name)
    print()
    quiz()
    
def quiz():
    def python():
        global score
        score=0
        print("1. Who created Python?")
        Q1=input('''
        A. Zim Den
        B. Guido van Rossum
        C. Niene Stom
        D. Niene Stom \n ''').upper()
        
        if Q1=="B":
            print("Correct Answer!!")
            score+=1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct Answer is = Guido van Rossum")
        
        print("2. Which one of the following is the correct extension of the Python file?")
        
        Q2=input('''
        A. .py
        B. .python
        C. .p
        D. None of these \n ''').upper()
        
        if Q2=="A":
            print("Correct Answer!!")
            score+=1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct Answer is = .py")
        
        print("3. What do we use to define a block of code in Python language?")
        
        Q3=input('''
        A. Key
        B. Brackets
        C. Indentation
        D. None of these \n ''').upper()
        
        if Q3=="C":
            print("Correct Answer!!")
            score+=1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct Answer is = Indentation")
        
        print("4. In which language is Python written?")
        
        Q4=input('''
        A. English
        B. C
        C. PHP
        D. All of the above \n ''').upper()
        
        if Q4=="B":
            print("Correct Answer!!")
            score+=1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct Answer is = C")
        
        print("5. Which character is used in Python to make a single line comment?")
        
        Q5=input('''
        Your answer is..
        A. /
        B. //
        C. !
        D. # \n ''').upper()
        
        if Q5=="D":
            print("Correct Answer!!")
            score+=1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct Answer is = #")
        print()
        result()
        
    def java():
        global score
        score=0
        print("1. Who is known as father of Java Programming Language?")
        Q1=input('''
        A. James Gosling
        B. M. P Java
        C.Charel Babbage
        D.Blais Pascal \n ''').upper()
        
        if Q1=="A":
            print("Correct Answer!!")
            score+=1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct Answer is = James Gosling")
        
        print("2. Which of the following are not Java keywords ?")
        
        Q2=input('''
        A. double
        B. switch
        C. then
        D. instanceof  \n ''').upper()
        
        if Q2=="C":
            print("Correct Answer!!")
            score=score+1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct Answer is = then")
        
        print("3. Java language was initially called as ________")
        
        Q3=input('''
        A. Sumatra
        B. J++ 
        C. Oak
        D. Pine \n ''').upper()
        
        if Q3=="C":
            print("Correct Answer!!")
            score=score+1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct answer is= Oak ")
        
        print("4. What is the extension of Java?")
        
        Q4=input('''
        A. .gt
        B. .oak
        C. .java
        D. .exe \n ''').upper()
        
        if Q4=="C":
            print("Correct Answer!!")
            score=score+1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct Answer is = .java ")
        
        print("5. Modulus operator (%) can be applied to which of these?")
        
        Q5=input('''
        A. Integers
        B. Floating - point numbers
        C. Both A and B
        C.Both A and B \n ''').upper()
        
        if Q5=="C":
            print("Correct Answer!!")
            score=score+1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct answer is = Both A and B ")
        print()
        result()    
        

    def c_c():
        global score
        score=0
        print("1. C is _______ type of programming language.?")
        Q1=input('''
        A. Object Oriented
        B. Procedural
        C. Bit level language
        D. Functional \n ''').upper()
        
        if Q1=="B":
            print("Correct Answer!!")
            score=score+1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct Answer is = Procedural")
        
        print("2. Which of the following is the correct identifier?")
        
        Q2=input('''
        A. $var_name
        B. VAR_123
        C. varname@
        D. None of the above \n ''').upper()
        
        if Q2=="B":
            print("Correct Answer!!")
            score=score+1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct Answer is = VAR_123 ")
        
        print("3. C language was invented in the year.?")
        
        Q3=input('''
        A. 1999 
        B. 1978
        C. 1972
        D. 1990 \n ''').upper()
        
        if Q3=="C":
            print("Correct Answer!!")
            score=score+1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct answer is = 1972 ")
        
        print("4. Which of the following is the original creator of the C++ language?")
        
        Q4=input('''
        A. Dennis Ritchie
        B. Ken Thompson
        C. Bjarne Stroustrup
        D. Brian Kernighan \n ''').upper()
    
        if Q4=="C":
            print("Correct Answer!!")
            score=score+1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct Answer is = Bjarne Stroustrup ")
        
        print("5. How many times will the following loop execute?")
        print()
        print(" for(j = 1; j <= 10; j = j-1)  ")
        
        Q5=input('''
        A. Forever
        B. Never
        C. 0
        D. 1 \n ''').upper()
        print(Q5)
        if Q5=="A":
            print("Correct Answer!!")
            score=score+1
        else:
            print("Wrong Answer!!")
            print()
            print("Correct answer is = Forever ")
        print()
        result()    
        

    def quiz1():
        print("*"*10,"Choose Language","*"*10)
        lng=int(input('''
        1. PYTHON
        2. JAVA
        3. C/C++ \n'''))
    
        if lng==1:
            python()
        elif lng==2:
            java()
        elif lng==3:
            c_c()
        else:
            print("invalid choice:")
            print()
            quiz1()
        print()
    quiz1()
def result():
    score1=((score/5)*100)
    print("Your score is: "+str(score1)+"%")
    print()
    exit()
    
def exit():
    exit=int(input('''
    Do you want to play again:
    1. Yes
    2. No \n '''))
    
    if exit==1:
        fill_details()
    if exit==2:
        print()
        print('\033[1m' + '******* Thank You For Playing *******')

def fill_details():
    print("*"*10, "Welcome", "*"*10)
    option=int(input('''
    1. User Details
    2. Quiz
    3. Result
    4. Exit \n'''))
    
    if option==1:
        userdetails()
    elif option==2:
        quiz()
    elif option==3:
        result()
    elif option==4:
        exit()
    else:
        print("Invalid option:")
        fill_details()
 
banner()   
print()
print()
fill_details()
