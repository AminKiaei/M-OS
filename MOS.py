c = {"/assist" : "show this","/bored" : "Talks to you","/scramble" : "Scrambles"}
a = input("password: ")
if a.isnumeric():
    a = int(a)
    if a==2914:
        print("Welcome to command board")
        print("If confused do /assist")
        b = input()
        if b=="/assist":
            print(c)
        if b=="/bored":
            a = input("Name: ")
            print('hello',a,'how are you doing today')
            b = int(input("number 1: "))
            c = int(input("number 2: "))
            print('answer is: ','Addition:',b+c,'Subtraction:',b-c,'Multiplication:',b*c,'and','Division:',b/c,', ',a)
            d = int(input('Age: '))
            f = 'You are about {} seconds old.'
            print(f.format(((d*365)+(d/5))*24*60*60))
            g = ('Your name is: {} characters long.')
            print(g.format(len(a)))
            e = int(input('weight in pounds: '))
            h = 'You weigh {} kilograms'
            print(h.format(e/2.2))
            print(a.capitalize(),"!!!!!",'you will retire in',60-d,'Years')
            i = int(input('Pick a number any number'))
            print("Multiply it by two then add thirteen")
            print("You got: ",i*2+13)
        if b=="/scramble":
            y = input("Word: ")
            print(y[int(len(y))//2:int(len(y))],y[0:int(len(y))//2])
    else:
        print("Incorect")
else:
    print("please enter positive integer")
a = input("password: ")
if a.isnumeric():
    a = int(a)
    if a==2914:
        print("Welcome to command board")
        print("If confused do /assist")
        b = input()
        if b=="/assist":
            print(c)
        if b=="/bored":
            a = input("Name: ")
            print('hello',a,'how are you doing today')
            b = int(input("number 1: "))
            c = int(input("number 2: "))
            print('answer is: ','Addition:',b+c,'Subtraction:',b-c,'Multiplication:',b*c,'and','Division:',b/c,', ',a)
            d = int(input('Age: '))
            f = 'You are about {} seconds old.'
            print(f.format(((d*365)+(d/5))*24*60*60))
            g = ('Your name is: {} characters long.')
            print(g.format(len(a)))
            e = int(input('weight in pounds: '))
            h = 'You weigh {} kilograms'
            print(h.format(e/2.2))
            print(a.capitalize(),"!!!!!",'you will retire in',60-d,'Years')
            i = int(input('Pick a number any number'))
            print("Multiply it by two then add thirteen")
            print("You got: ",i*2+13)
        if b=="/scramble":
            y = input("Word: ")
            print(y[int(len(y))//2:int(len(y))],y[0:int(len(y))//2])
    else:
        print("Incorect")
else:
    print("please enter positive integer")