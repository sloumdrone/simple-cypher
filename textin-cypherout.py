input1 = raw_input("Text to encode?")
dict01 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27, '?': 28, '.': 29, ',': 30}
dict02 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ' ', 28: '?', 29: '.', 30: ',', 31: 'a', 32: 'b', 33: 'c', 34: 'd', 35: 'e', 36: 'f', 37: 'g', 38: 'h', 39: 'i', 40: 'j', 41: 'k', 42: 'l', 43: 'm', 44: 'n', 45: 'o', 46: 'p', 47: 'q', 48: 'r', 49: 's', 50: 't', 51: 'u', 52: 'v', 53: 'w', 54: 'x', 55: 'y', 56: 'z', 57: ' ', 58: '?', 59: '.', 60: ','}
input1 = input1.lower()
counter = 0

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
