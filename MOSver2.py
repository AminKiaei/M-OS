c = {"/assist" : "show this","/bored" : "Talks to you","/scramble" : "Scrambles","/multiple":"finds multiples",
     "/grade":"finds grade","/sort":"Sorts things","/stop":"Stops"}
a = input("password: ")
if a.isnumeric():
    a = int(a)
    if a==2914:
        print("Welcome to command board")
        print("If confused do /assist")
        b = input()
        if b=="/assist":
            print(c)
        elif b=="/bored":
                _al = input("Name: ")
                print('hello',_al,'how are you doing today')
                _bl = int(input("number 1: "))
                _cl = int(input("number 2: "))
                print('answer is: ','Addition:',_bl+_cl,'Subtraction:',_bl-_cl,'Multiplication:',_bl*_cl,'and','Division:',_bl/_cl)
                _dl = int(input('Age: '))
                _fl = 'You are about {} seconds old.'
                print(_fl.format(((_dl*365)+(_dl/5))*24*60*60))
                _g = ('Your name is: {} characters long.')
                print(_g.format(len(_al)))
                e = int(input('weight in pounds: '))
                _hl = 'You weigh {} kilograms'
                print(_hl.format(e/2.2))
                print(_al.capitalize(),"!!!!!",'you will retire in',60-_dl,'Years')
                _il = int(input('Pick a number any number'))
                print("Multiply it by two then add thirteen")
                print("You got: ",_il*2+13)
        elif b=="/multiple":
            p = input("number: ")
            o = input("number: ")
            if p.isnumeric() and o.isnumeric():
                p = int(p)
                o = int(o)
                if p%o==0:
                    print(o,"is the",p/o,"multiple of",p)
                else:
                    print(o,"is not a multiple of",p)
            else:
              print("please write number")
        elif b=="/sort":
            _dr = input("item: ")
            _cl = input("item: ")
            _dd = input("item: ")
            _egrd = input("item: ")
            _adgf = [_dr,_cl,_dd,_egrd]
            _adgf.sort()
            print(_adgf)
        elif b=="/grade":
            l = int(input("grade: "))
            if a>=90:
                print("A")
            elif a>=80:
                print("B")
            elif a>=70:
                print("C")
            elif a>=60:
                print("D")
            else:
                print("F")
        elif b=="/scramble":
            y = input("Word: ")
            print(y[int(len(y))//2:int(len(y))],y[0:int(len(y))//2])
        else:
            print("Command unknown")
    else:
        print("Incorect")
else:
    print("please enter positive integer")
i=1
while i<6:
    a = str(a)
    if a.isnumeric():
        a = int(a)
        if a==2914:
            b = input()
            if b=="/assist":
                print(c)
            elif b=="/bored":
                _al = input("Name: ")
                print('hello',_al,'how are you doing today')
                _bl = int(input("number 1: "))
                _cl = int(input("number 2: "))
                print('answer is: ','Addition:',_bl+_cl,'Subtraction:',_bl-_cl,'Multiplication:',_bl*_cl,'and','Division:',_bl/_cl)
                _dl = int(input('Age: '))
                _fl = 'You are about {} seconds old.'
                print(_fl.format(((_dl*365)+(_dl/5))*24*60*60))
                _g = ('Your name is: {} characters long.')
                print(_g.format(len(_al)))
                e = int(input('weight in pounds: '))
                _hl = 'You weigh {} kilograms'
                print(_hl.format(e/2.2))
                print(_al.capitalize(),"!!!!!",'you will retire in',60-_dl,'Years')
                _il = int(input('Pick a number any number'))
                print("Multiply it by two then add thirteen")
                print("You got: ",_il*2+13)
            elif b=="/multiple":
                p = input("number: ")
                o = input("number: ")
                if p.isnumeric() and o.isnumeric():
                    p = int(p)
                    o = int(o)
                    if p%o==0:
                        print(o,"is the",p/o,"multiple of",p)
                    else:
                        print(o,"is not a multiple of",p)
                else:
                    print("please write number")
            elif b=="/sort":
                _dr = input("item: ")
                _cl = input("item: ")
                _dd = input("item: ")
                _egrd = input("item: ")
                _adgf = [_dr,_cl,_dd,_egrd]
                _adgf.sort()
                print(_adgf)
            elif b=="/grade":
                l = int(input("grade: "))
                if a>=90:
                    print("A")
                elif a>=80:
                    print("B")
                elif a>=70:
                    print("C")
                elif a>=60:
                    print("D")
                else:
                    print("F")
            elif b=="/scramble":
                y = input("Word: ")
                print(y[int(len(y))//2:int(len(y))],y[0:int(len(y))//2])
            else:
                print("Command unknown")
