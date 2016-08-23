import string


"""Convert the input into regular text, from cypher"""

def stringout ():
    """take input"""
    input2 = raw_input("Text to encode?")
    counter2 = 0

    """Create dictionary lookups"""
    chars = string.printable
    charlist = []
    dict02 = {}
    dict03 = {}

    for x in chars:
        charlist.append(x)

    for y, z in enumerate(charlist):
        dict02.update({y: z})
        dict03.update({y: z})

    dict01=dict((value,key) for key,value in dict02.iteritems())

    for key in dict02.iterkeys():
        if key < 100:
            dict02[key+100] = dict02.pop(key)
        else:
            break
    
    conversionstep1 = list(input2)
    conversionstep2 = []
    conversionstep3 = []
    conversionstep4 = []

    """get numbers from letters"""
    for x, y in enumerate(conversionstep1):
            conversionstep2.append(dict01[str(conversionstep1[x])])

    
    """convert numbers to decyphered numbers"""
    for x, y in enumerate(conversionstep2):
        if x < 1:
            conversionstep3.append(conversionstep2[x])
        else:
            try:
                counter2 =  conversionstep2[x] - conversionstep3[(x-1)]
                if counter2 < 0:
                    counter2 += 100
                conversionstep3.append(counter2)
            except IndexError:
                pass
            continue
    counter = 0

    for x, y in enumerate(conversionstep3):
        if y > 99:
            conversionstep4.append(dict02[conversionstep3[x]])
        else:
            conversionstep4.append(dict03[conversionstep3[x]])
    print ''.join(conversionstep4)

    cyphermenu()




"""Converts the input to cypher text"""
def stringin ():
    """Allow for input input"""
    input1 = raw_input("Text to encode?")
    counter = 0

    """Create dictionary lookups"""
    chars = string.printable
    charlist = []
    dict02 = {}
    dict03 = {}

    for x in chars:
        charlist.append(x)

    for y, z in enumerate(charlist):
        dict02.update({y: z})
        dict03.update({y: z})

    dict01=dict((value,key) for key,value in dict02.iteritems())

    for key in dict02.iterkeys():
        if key < 100:
            dict02[key+100] = dict02.pop(key)
        else:
            break

    dict02.update(dict03)

    conversionstep1 = list(input1)
    conversionstep2 = []
    conversionstep3 = []
    conversionstep4 = []
    for x, y in enumerate(conversionstep1):
            conversionstep2.append(dict01[str(conversionstep1[x])])
    
    conversionstep3.append(conversionstep2[0])

    for x, y in enumerate(conversionstep2,1):
        try:
            counter = conversionstep2[x] + conversionstep2[(x - 1)]
            conversionstep3.append(counter)
        except IndexError:
            pass
        continue
    
    counter = 0
    for x, y in enumerate(conversionstep3):
            conversionstep4.append(dict02[conversionstep3[x]])
    print ''.join(conversionstep4)

    cyphermenu()
            
    

def cyphermenu ():
    print 'What would you like to do?'
    print '[1] Encypher'
    print '[2] Decypher'
    menuchoice = input(':')


    if menuchoice == 1:
        stringin()
    elif menuchoice == 2:
        stringout()
    else:
        print 'Invalid Entry'

cyphermenu()
