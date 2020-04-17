xxx = ["H", "C", "O"]
elements = set(xxx)
while(True):
    chemical_formula = input("Enter chemical formula, or enter to quit: ")
    if chemical_formula == "":
        break
    else:
        characters = list(chemical_formula)
        n = 0
        print(characters)
        for i in characters:
            if characters[n] == "C":
                c = 12.0107
                if elements.intersection(set(characters[n+1])):
                    print(c)
                else:
                    number = int(characters[n+1])
                    print(number*c)

            elif characters[n] == "H":
                h = 1.00794
                if elements.intersection(set(characters[n+1])):
                    print(h)
                else:
                    number = int(characters[n+1])
                    print(number*h)

            elif characters[n] == "O":
                o = 15.9994
                if elements.intersection(set(characters[n+1])):
                    print(c)
                else:
                    number = int(characters[n+1])
                    print(number*o) 
            else:
                number = int(i)
                print(i*0)
