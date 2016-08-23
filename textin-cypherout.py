import string

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

"""Converts the input to cypher text"""
def stringin ():
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
            
    

stringin()
