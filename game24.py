#Evan Long Ma & Sherry Zhuang
#elm454 xz1741
#24 Points!

import datetime
import math
import random

try:
    import pyautogui
except:
    pass


class Twentyfour:
    def __init__(self,time,seed):
        self.time = time
        self.seed = seed
        random.seed(self.seed)
    
    def start_game(self):
        win = 24
        #User score #Not actually a constant, but yeah
        POINTS = 0
        rounds_won = 0
        
        #Playing Cards / Numbers
        #a, b, c, d = 2, 4, 3, 6
        a, b, c, d = 5, 5, 5, 1
        #a, b, c, d = 4, 4, 7, 7
        
        #COUNT_OF_NUMBER = 4
        NUMBER_TO_BE_CAL = win
        
        #Regarding printouts
        showrules = False
        showrulesinside = False
        last = ""
        
        #controls states
        st = 0
        
        # count games
        count = 10
        
        unsolvable = True
        
        print("Here are the rules:\nEnter \"hide\" to hide them, and \"show\" to show them\n")
        print("Create a mathematical expression that equals the goal number!")
        print("Traditionally only +-*/ are used, but try these for fun.")
        print("% is for modulus (A%B), // for integer division (A//B), and ** for exponents (A**B)")
        print("! can be used for factorial, though you type it special:\nYou do !(A) for the factorial of A")
        print("Use every card once, no more, no less.")
        print("If your expression has errors, we will show the first error.")
        print("Be sure to use *, \"AB\" doesn't render as \"A\"*\"B\".\n")
        print("You can skip questions by just typing \"skip\"")
        print("If your expression is 卡ing, or takes too long,\npress Control-C on your keyboard to try with another expression")
        
        #Main game
        while count > 0:
            while st == 0:
                number_lst = [a,b,c,d]
                formula_lst = [str(a),str(b),str(c),str(d)]
                count -= 1
            #recursive solver
                def solve(n, real):
                    
                    if(1 == n):
                        if NUMBER_TO_BE_CAL - number_lst[0] == 0:
                            if real:
                                print("The answer is: " + formula_lst[0] + " = " + str(win) + "\n\n")
                            return True
                        else:
                            return False
                    else:
                        for i in range(0, n):
                            for j in range(i+1, n): 
                                x = number_lst[i] 
                                y = number_lst[j] 
                                #**********************************
                                #   Move the meaingful forward
                                #   answer saved in [i]
                                #   number[j]can just be overwritten by the last number
                                #   *******************************
                                number_lst[j] = number_lst[n - 1]
                                form_x = formula_lst[i] 
                                form_y = formula_lst[j]
                                formula_lst[j] = formula_lst[n - 1]
                                
                                # cal x+y
                                formula_lst[i] = '(' + form_x + '+' + form_y + ')'
                                number_lst[i] = x + y
                                if ( solve(n - 1, real) ):
                                    return True
                                # cal x-y
                                formula_lst[i] = '(' + form_x + '-' + form_y + ')'
                                number_lst[i] = x - y
                                if ( solve(n - 1, real) ):
                                    return True
                                # cal y-x
                                formula_lst[i] = '(' + form_y + '-' + form_x + ')'
                                number_lst[i] = y - x
                                if ( solve(n - 1, real) ):
                                    return True
                                # cal (x*y)
                                formula_lst[i] = '(' + form_x + '*' + form_y + ')'
                                number_lst[i] = x * y
                                if ( solve(n - 1, real) ):
                                    return True
                                
                                # cal (x/y)
                                if (y != 0) :
                                    formula_lst[i] = '(' + form_x + '/' + form_y + ')'
                                    number_lst[i] = x / y
                                    if ( solve(n - 1, real) ):
                                        return True
                                    
                                    # (x//y)
                                    formula_lst[i] = '(' + form_x + '//' + form_y + ')'
                                    number_lst[i] = x // y
                                    if ( solve(n - 1, real) ):
                                        return True
                                    
                                    #(x%y)
                                    formula_lst[i] = '(' + form_x + '%' + form_y + ')'
                                    number_lst[i] = x % y
                                    if ( solve(n - 1, real) ):
                                        return True
                                    
                                # cal (y/x)
                                    if (x != 0) :
                                        formula_lst[i] = '(' + form_y + '/' + form_x + ')'
                                        number_lst[i] = y / x
                                        if ( solve(n - 1, real) ):
                                            return True
                                        
                                        #(y//x)
                                        formula_lst[i] = '(' + form_y + '//' + form_x + ')'
                                        number_lst[i] = y // x
                                        if ( solve(n - 1, real) ):
                                            return True
                
                                        #(y % x)
                                        formula_lst[i] = '(' + form_y + '%' + form_x + ')'
                                        number_lst[i] = y % x
                                        if ( solve(n - 1, real) ):
                                            return True
                
                                # cal(x ** y)
                                formula_lst[i] = '(' + form_x + '**' + form_y + ')'
                                if (x == 1 or (x == 0 and y >= 0)
                                or (x == 2 and abs(y) <= 9) or (x == 3 and abs(y) <= 6)
                                or (x == 4 and abs(y) <= 5) or (x == 5 and abs(y) <= 4)
                                or (x == 6 and abs(y) <= 3) or (x == 7 and abs(y) <= 3)
                                or (x == 8 and abs(y) <= 3) or (x == 9 and abs(y) <= 3)
                                or (x == 10 and abs(y) <= 3) or (x == 11 and abs(y) <= 2)
                                or (x == 12 and abs(y) <= 2) or (x == 13 and abs(y) <= 2)): 
                                    number_lst[i] = x ** y 
                                    if ( solve(n - 1, real) ):
                                        return True
                                        
                                # cal(y ** x)
                                formula_lst[i] = '(' + form_y + '**' + form_x + ')'
                                if (y == 1 or (y == 0 and x >= 0)
                                or (y == 2 and abs(x) <= 9) or (y == 3 and abs(x) <= 6)
                                or (y == 4 and abs(x) <= 5) or (y == 5 and abs(x) <= 4)
                                or (y == 6 and abs(x) <= 3) or (y == 7 and abs(x) <= 3)
                                or (y == 8 and abs(x) <= 3) or (y == 9 and abs(x) <= 3)
                                or (y == 10 and abs(x) <= 3) or (y == 11 and abs(x) <= 2)
                                or (y == 12 and abs(x) <= 2) or (y == 13 and abs(x) <= 2)): 
                                    number_lst[i] = y ** x
                                    if ( solve(n - 1, real) ):
                                        return True
                                        
                                
                                #All the factorials
                                if y >= 0 and (int(y) - y == 0):
                                # cal(!(y) + x)
                                    formula_lst[i] = '(!(' + form_y + ')' + "+" + form_x + ')'
                                    if y <= 6:
                                        number_lst[i] = math.factorial(y) + x
                                        if ( solve(n - 1, real) ):
                                            return True
                                        
                                # cal(!(y) - x)
                                    formula_lst[i] = '(!(' + form_y + ')' + "-" + form_x + ')'
                                    if y <= 6:
                                        number_lst[i] = math.factorial(y) - x
                                        if ( solve(n - 1, real) ):
                                            return True
                                
                                # cal(!(y) * x)
                                    formula_lst[i] = '(!(' + form_y + ')' + "*" + form_x + ')'
                                    if y <= 6:
                                        number_lst[i] = math.factorial(y) * x
                                        if ( solve(n - 1, real) ):
                                            return True
                                        
                                # cal(!(y) / x)
                                    if x != 0:
                                        formula_lst[i] = '(!(' + form_y + ')' + "/" + form_x + ')'
                                        if y <= 6:
                                            number_lst[i] = math.factorial(y) / x
                                            if ( solve(n - 1, real) ):
                                                return True
                                
                                # cal(!(y) // x)
                                        formula_lst[i] = '(!(' + form_y + ')' + "//" + form_x + ')'
                                        if y <= 6:
                                            number_lst[i] = math.factorial(y) // x
                                            if ( solve(n - 1, real) ):
                                                return True
                                
                                # cal(!(y) % x)
                                        formula_lst[i] = '(!(' + form_y + ')' + "%" + form_x + ')'
                                        if y <= 6:
                                            number_lst[i] = math.factorial(y) % x
                                            if ( solve(n - 1, real) ):
                                                return True
                                
                                # cal(!(y) ** x)
                                    formula_lst[i] = '(!(' + form_y + ')' + "**" + form_x + ')'
                                    if (y <= 6 and (y == 0 or y == 1 or (y == 2 and abs(x) <= 9)
                                    or (y == 3 and abs(x) <= 3) or (y == 4 and abs(x) <= 3)
                                    or (y == 5 and abs(x) <= 2) or (y == 6 and abs(x) <= 1))):
                                        number_lst[i] = math.factorial(y) ** x
                                        if ( solve(n - 1, real) ):
                                            return True
                                
                                
                                #Double
                                    if x >= 0 and (int(x) - x == 0):
                                    # cal(!(y) + !(x))
                                        formula_lst[i] = '(!(' + form_y + ')' + " + !(" + form_x + '))'
                                        if y <= 6 and x <= 6:
                                            number_lst[i] = math.factorial(y) + math.factorial(x)
                                            if ( solve(n - 1, real) ):
                                                return True
                                            
                                    # cal(!(y) - !(x)))
                                        formula_lst[i] = '(!(' + form_y + ')' + " - !(" + form_x + '))'
                                        if y <= 6 and x <= 6:
                                            number_lst[i] = math.factorial(y) - math.factorial(x)
                                            if ( solve(n - 1, real) ):
                                                return True
                                    
                                    # cal(!(y) * !(x))
                                        formula_lst[i] = '(!(' + form_y + ')' + " * !(" + form_x + '))'
                                        if y <= 6 and x <= 6:
                                            number_lst[i] = math.factorial(y) * math.factorial(x)
                                            if ( solve(n - 1, real) ):
                                                return True
                                            
                                    # cal(!(y) / !(x))
                                        formula_lst[i] = '(!(' + form_y + ')' + " / !(" + form_x + ')'
                                        if y <= 6 and x <= 6:
                                            number_lst[i] = math.factorial(y) / math.factorial(x)
                                            if ( solve(n - 1, real) ):
                                                return True
                                
                                    # cal(!(y) // !(x))
                                        formula_lst[i] = '(!(' + form_y + ')' + " // !(" + form_x + '))'
                                        if y <= 6 and x <= 6:
                                            number_lst[i] = math.factorial(y) // math.factorial(x)
                                            if ( solve(n - 1, real) ):
                                                return True
                                
                                    # cal(!(y) % !(x))
                                        formula_lst[i] = '(!(' + form_y + ')' + " % !(" + form_x + '))'
                                        if y <= 6 and x <= 6:
                                            number_lst[i] = math.factorial(y) % math.factorial(x)
                                            if ( solve(n - 1, real) ):
                                                return True
                                    
                                    # cal(!(y) ** !(x))
                                        formula_lst[i] = '(!(' + form_y + ')' + " ** !(" + form_x + '))'
                                        if (y <= 6 and (y == 0 or y == 1 or (y == 2 and abs(x) <= 4)
                                        or (y == 3 and abs(x) <= 3) or (y == 4 and abs(x) <= 2)
                                        or (y == 5 and abs(x) <= 2) or (y == 6 and abs(x) <= 1))):
                                            number_lst[i] = math.factorial(y) ** math.factorial(x)
                                            if ( solve(n - 1, real) ):
                                                return True
                                
                                
                                        
                                #All the factorials part 2
                                if x >= 0 and (int(x) - x == 0):
                                # cal(!(x) + y)
                                    formula_lst[i] = '(!(' + form_x + ')' + "+" + form_y + ')'
                                    if x <= 6:
                                        number_lst[i] = math.factorial(x) + y
                                        if ( solve(n - 1, real) ):
                                            return True
                                        
                                # cal(!(x) - y)
                                    formula_lst[i] = '(!(' + form_x + ')' + "-" + form_y + ')'
                                    if x <= 6:
                                        number_lst[i] = math.factorial(x) - y
                                        if ( solve(n - 1, real) ):
                                            return True
                                
                                # cal(!(x) * y)
                                    formula_lst[i] = '(!(' + form_x + ')' + "*" + form_y + ')'
                                    if x <= 6:
                                        number_lst[i] = math.factorial(x) * y
                                        if ( solve(n - 1, real) ):
                                            return True
                                        
                                # cal(!(x) / y)
                                    if y != 0:
                                        formula_lst[i] = '(!(' + form_x + ')' + "/" + form_y + ')'
                                        if x <= 6:
                                            number_lst[i] = math.factorial(x) / y
                                            if ( solve(n - 1, real) ):
                                                return True
                                
                                # cal(!(x) // y)
                                        formula_lst[i] = '(!(' + form_x + ')' + "//" + form_y + ')'
                                        if x <= 6:
                                            number_lst[i] = math.factorial(x) // y
                                            if ( solve(n - 1, real) ):
                                                return True
                                
                                # cal(!(x) % y)
                                        formula_lst[i] = '(!(' + form_x + ')' + "%" + form_y + ')'
                                        if x <= 6:
                                            number_lst[i] = math.factorial(x) % y
                                            if ( solve(n - 1, real) ):
                                                return True
                                
                                # cal(!(x) ** y)
                                    formula_lst[i] = '(!(' + form_x + ')' + "**" + form_y + ')'
                                    if (x <= 6 and (x == 0 or x == 1 or (x == 2 and abs(y) <= 9)
                                    or (x == 3 and abs(y) <= 3) or (x == 4 and abs(y) <= 3)
                                    or (x == 5 and abs(y) <= 2) or (x == 6 and abs(y) <= 1))):
                                        number_lst[i] = math.factorial(x) ** y
                                        if ( solve(n - 1, real) ):
                                            return True
                                
                                        
                                #Double
                                    if y >= 0 and (int(y) - y == 0):
                                    # cal(!(x) + !(y))
                                        formula_lst[i] = '(!(' + form_x + ')' + " + !(" + form_y + '))'
                                        if x <= 6 and y <= 6:
                                            number_lst[i] = math.factorial(x) + math.factorial(y)
                                            if ( solve(n - 1, real) ):
                                                return True
                                            
                                    # cal(!(x) - !(y))
                                        formula_lst[i] = '(!(' + form_x + ')' + " - !(" + form_y + '))'
                                        if x <= 6 and y <= 6:
                                            number_lst[i] = math.factorial(x) - math.factorial(y)
                                            if ( solve(n - 1, real) ):
                                                return True
                                    
                                    # cal(!(x) * !(y))
                                        formula_lst[i] = '(!(' + form_x + ')' + " * !(" + form_y + '))'
                                        if x <= 6 and y <= 6:
                                            number_lst[i] = math.factorial(x) * math.factorial(y)
                                            if ( solve(n - 1, real) ):
                                                return True
                                            
                                    # cal(!(x) / !(y))
                                        formula_lst[i] = '(!(' + form_x + ')' + " / !(" + form_y + ')'
                                        if x <= 6 and y <= 6:
                                            number_lst[i] = math.factorial(x) / math.factorial(y)
                                            if ( solve(n - 1, real) ):
                                                return True
                                
                                    # cal(!(x) // !(y))
                                        formula_lst[i] = '(!(' + form_x + ')' + " // !(" + form_y + '))'
                                        if x <= 6 and y <= 6:
                                            number_lst[i] = math.factorial(x) // math.factorial(y)
                                            if ( solve(n - 1, real) ):
                                                return True
                                
                                    # cal(!(x) % !(y))
                                        formula_lst[i] = '(!(' + form_x + ')' + " % !(" + form_y + '))'
                                        if x <= 6 and y <= 6:
                                            number_lst[i] = math.factorial(x) % math.factorial(y)
                                            if ( solve(n - 1, real) ):
                                                return True
                                    
                                    # cal(!(x) ** !(y))
                                        formula_lst[i] = '(!(' + form_x + ')' + " ** !(" + form_y + '))'
                                        if (x <= 6 and (x == 0 or x == 1 or (x == 2 and abs(y) <= 4)
                                        or (x == 3 and abs(y) <= 3) or (x == 4 and abs(y) <= 2)
                                        or (x == 5 and abs(y) <= 2) or (x == 6 and abs(y) <= 1))):
                                            number_lst[i] = math.factorial(x) ** math.factorial(y)
                                            if ( solve(n - 1, real) ):
                                                return True
                                        
                                 # resume and recursion
                                number_lst[i] = x
                                number_lst[j] = y
                                formula_lst[i] = form_x
                                formula_lst[j] = form_y
                 
                    return False
            
                if showrules:
                    print("Here are the rules:\nEnter \"hide\" to hide them, and \"show\" to show them\n")
                    print("Create a mathematical expression that equals the goal number!")
                    print("Traditionally only +-*/ are used, but try these for fun.")
                    print("% is for modulus (A%B), // for integer division (A//B), and ** for exponents (A**B)")
                    print("! can be used for factorial, though you type it special:\nYou do !(A) for the factorial of A")
                    print("Use every card once, no more, no less.")
                    print("If your expression has errors, we will show the first error.")
                    print("Be sure to use *, \"AB\" doesn't render as \"A\"*\"B\".\n")
                    print("You can skip questions by just typing \"skip\"")
                    print("If your expression is 卡ing, or takes too long,\npress Control-C on your keyboard to try with another expression")
                    if last == "WIN":
                        print("\nWIN-WIN-WIN-WIN-WIN")
                        print("Total points:", POINTS, "\n\n")
                    elif last == "SKIP":
                        print("\nSkipSkipSkip")
                        print("Total points:", POINTS, "\n\n")
                
                st = 1
                #To measure time
                start = datetime.datetime.now()
                while st == 1:
                    if showrulesinside:
                        print("Here are the rules:\nEnter \"hide\" to hide them, and \"show\" to show them\n")
                        print("Create a mathematical expression that equals the goal number!")
                        print("Traditionally only +-*/ are used, but try these for fun.")
                        print("% is for modulus (A%B), // for integer division (A//B), and ** for exponents (A**B)")
                        print("! can be used for factorial, though you type it special:\nYou do !(A) for the factorial of A")
                        print("Use every card once, no more, no less.")
                        print("If your expression has errors, we will show the first error.")
                        print("Be sure to use *, \"AB\" doesn't render as \"A\"*\"B\".\n")
                        print("You can skip questions by just typing \"skip\"")
                        print("If your expression takes too long,\npress Control-C on your keyboard to try with another expression")
                        showrulesinside = False
                    
                    print("\n---\nCARDS:")
                    print("a:", a, "b:", b, "c:", c, "d:", d, end="\n\n")
                    print("Okay, try to make an expression that equals", win)
                            
                    status = 0
                    print("Press enter to start your expression")
                    sol = input("(e.g. a*b*(d-c), like you would in standard python code) (or skip/show/hide):")
                    soln = win-1
                    try:
                        #If the expression is invalid, flip status to -1/2/3/4 etc.
                        status = 1
                        #Counts the incidence of a/b/c/d respectively.
                        aa = 0
                        bb = 0
                        cc = 0
                        dd = 0
                        
                        #Checking every character in the string inputted
                        itt = 0
                        
                        #Allow skipping the round
                        if sol.lower() == "skip":
                            st = "SKIP"
                            solve(4, True)
                            break
                        
                        #Showing and hiding the rules
                        if sol.lower() == "show":
                            showrules = True
                            showrulesinside = True
                            continue
                        if sol.lower() == "hide":
                            showrules = False
                            continue
                        
                        for i in sol.lower():
                            #Using the notation of ! before a parentheses as
                            #meaning factorial, change that to math.factorial for python to use.
                            if i == "!":
                                sol = sol[:itt]+"math.factorial"+sol[itt+1:]
                            
                            #No self-inputting numbers
                            if i.isdigit():
                                status = -1
                                break
                                
                            #Can't use a card/number more than once
                            elif i.isalpha():
                                if i == "a":
                                    aa += 1
                                    if aa >= 2:
                                        status = -2
                                        break
                                elif i == "b":
                                    bb += 1
                                    if bb >= 2:
                                        status = -2
                                        break
                                elif i == "c":
                                    cc += 1
                                    if cc >= 2:
                                        status = -2
                                        break
                                elif i == "d":
                                    dd += 1
                                    if dd >= 2:
                                        status = -2
                                        break
                            itt +=1
                                    
                        #Must use every card/number once
                        if aa + bb + cc + dd < 4 and status > 0:
                            status = -3
                            
                        #Restrict calling math or random functions (but allow the factorial we implemented)
                        if sol.lower().find("math.factorial") > -1:
                            pass
                        elif sol.lower().find("math") > -1 or sol.lower().find("random") > -1:
                            status = -4
                                
                        #If the input doesn't seem to be cheating, evaluate it
                        if status > 0:
                            soln = eval(sol.lower())
                        #Otherwise help print out the error that was found
                        #(only shows the first error found, since we want to calculate faster)
                        elif status == -1:
                            print("---\n\nNot a valid expression (used numbers):\n")
                        elif status == -2:
                            print("---\n\nNot a valid expression (used a card twice):\n")
                        elif status == -3:
                            print("---\n\nNot a valid expression (didn't use a card):\n")
                        elif status == -4:
                            print("---\n\nNot a valid expression (cannot use math or random etc. python import functions):\n")
                    except:
                        print("---\n\nTry again, not a valid python expression:\n")
                        continue
                    
                    #If the evaluation succeeds and equals the goal number, count the win.
                    if soln == win:
                        end = datetime.datetime.now()
                        elapsed = end - start
                        #print("\n\n", elapsed.seconds, ".", elapsed.microseconds, " seconds", sep="")
                        time = elapsed.seconds + elapsed.microseconds/1000000
                        print("\n\nWin!\n===============================")
                        print(time, "seconds")
                        
                        #Points added are the seconds of time left per 30 second round.
                        if 60 - time > 0:
                            POINTS += 60 - time
                        rounds_won += 1
                        
                        st = "WIN"
                        #unsolvable = True
                    else:
                        end = datetime.datetime.now()
                        elapsed = end - start
                        #print("\n\n", elapsed.seconds, ".", elapsed.microseconds, " seconds", sep="")
                        time = elapsed.seconds + elapsed.microseconds/1000000
                        if 60 - time > 0:
                            print("---\n\nTry again.\n")
                        else:
                            if solve(4, True):
                                st = 'SKIP'
                            else:
                                print('There is no solution for this turn\n')
                                #This should never happen. And it never does so I guess we've done well.
                                st = 'SKIP'
                    
                
            while st == "WIN":
                print("Total points:", POINTS, "\n\n")
                #Create new cards randomly
                unsolvable = True
                while unsolvable:
                    #This loop ensures all cards shown to players are solvable.
                    a, b, c, d  = random.randint(1, 13), random.randint(1, 13), random.randint(1, 13), random.randint(1, 13)
                    try:
                        number_lst = [a,b,c,d]
                        formula_lst = [str(a),str(b),str(c),str(d)]
                        if solve(4, False):
                            unsolvable = False
                    except:
                        pass
                last = "WIN"
                st = 0
                
                if count <= 0:
                    print("End game!")
                    try:
                        pyautogui.typewrite(" ")
                        pyautogui.hotkey("enter")
                    except:
                        print("Return an empty space to continue")
                    return POINTS, rounds_won
                
                
            while st == "SKIP":
                print("\n=====\nTotal points: Still", POINTS, "\n\n")
                if count <= 0:
                    print("End game!")
                    try:
                        pyautogui.typewrite(" ")
                        pyautogui.hotkey("enter")
                    except:
                        print("Return an empty space to continue")
                    return POINTS, rounds_won
                    
                #Create new cards randomly
                unsolvable = True
                while unsolvable:
                    #This loop ensures all cards shown to players are solvable.
                    a, b, c, d  = random.randint(1, 13), random.randint(1, 13), random.randint(1, 13), random.randint(1, 13)
                    try:
                        number_lst = [a,b,c,d]
                        formula_lst = [str(a),str(b),str(c),str(d)]
                        if solve(4, False):
                            unsolvable = False
                    except:
                        pass
                
                last = "SKIP"
                st = 0
