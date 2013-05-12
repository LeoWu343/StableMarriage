from random import shuffle
# Creates a randomized chart of people, both men and women
def create_chart(people):
    male = []
    female = []
    for i in range(people):
        male.append(range(people))
        shuffle(male[i])
        female.append(range(people))
        shuffle(female[i])
    return male, female

# Solves the stable marriage problem
# Note that this destroys the lists "men" and "women"
def solve(men, women):
    def getNotNone(l):
        return next((i for i, v in enumerate(l) if v != None), -1)
    strings = [False for _ in range(len(men))]
    currs = [len(men) for _ in range(len(women))]
    def solve_helper(men, women):
        for i in range(len(men)):
            foo = getNotNone(men[i])
            if foo == -1:
                return None
            curr = men[i][foo]
            currWoman = women[curr]
            if currs[curr] == len(men):
                currs[curr] = i
                strings[i] = True
            elif currWoman.index(i) <= currWoman.index(currs[curr]):
                if currWoman.index(i) != currWoman.index(currs[curr]):
                    old = men[currs[curr]]
                    old[getNotNone(old)] = None
                    strings[currs[curr]] = False
                currs[curr] = i
                strings[i] = True
            else:
                men[i][foo] = None
        if strings[0] == True and len(set(strings)) == 1:
            return currs
        else:
            return solve_helper(men, women)
    return solve_helper(men, women)

# Gets number of men and women for the problem
def begin_input():
    try:
        people = int(raw_input("Number of men and women (max: 26): "))
    except:
        print "Improper input"
        exit()
    return people

# Gets another practice the problem if the user requests it
def again():
    try:
        again = str(raw_input("Again? "))
    except:
        print "Improper input"
        exit()
    if again.upper() == "YES" or again.upper() == "Y":
        main()
    else:
        exit()

# Creates a practice problem and solves it
def main():
    people = begin_input()
    x, y = create_chart(people)
    conversion = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
    printy = [[i + 1 for i in z] for z in y]
    printx = [[conversion[i].upper() for i in z] for z in x]
    print "Men\n---"
    for i in range(len(printx)):
        printable = str(printx[i])
        print str(i + 1) + ": " + printable[1:len(printable)-1].replace("'", "")
    print "Women\n-----"
    for i in range(len(printy)):
        printable = str(printy[i])
        print conversion[i].upper() + ": " + printable[1:len(printable)-1]
    z = solve(x, y)
    raw_input("Press enter to reveal the answer")
    print "Answer:"
    if z == None:
        print "There is no stable set of pairings possible."
    else:
        d = {}
        for i in z:
            d[i + 1] = conversion[z.index(i)].upper()
        printable = str(d)
        print printable[1:len(printable)-1].replace("'", "")
    again()

main()
