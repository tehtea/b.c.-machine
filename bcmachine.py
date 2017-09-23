import itertools
import copy

#to-do: have two classes - unsigned binary and signed binary.
#to-do: add another class - the gray code class. I can foresee a graphical UI,
#with karnaugh maps and shit with it!!! This program will just be proof of
#concept for now.

def bitadder(x, y, carry=0):
    '''
    function bitadder - used to perform addition of two binary unsigned integers
    in the most inefficient way possible!

    each binary string is zipped together and iterated through in reverse order
    (assume the right bit is the least significant bit) to perform the computation.
    '''
    assert bin_valid(x) and bin_valid(y),\
           "one of the inputs is not valid!"
    assert carry == 0 or carry == 1, "carry in is not 0 or 1!"
    result = []
    #make the length of x and y equal, then iterate them together.
    longest = max(len(x), len(y))
    x = x.rjust(longest,'0')
    y = y.rjust(longest,'0')
    for i,j in itertools.zip_longest(str(x)[::-1], str(y)[::-1]):
        if (i == '0' or i == '1') and (j == '0' or j == '1'):
            bit = (int(i)^int(j))^carry
            carry = int(i)&int(j)|int(i)&carry|int(j)&carry
            result.insert(0, str(bit))
        else:
            return "invalid input for x or y\
 - they must both be binary strings of the same length! (bitadder / line 30)"
    if carry == 1:
        result.insert(0, str(carry))
    else:
        pass
    return ''.join(result)

def twocomplement(x, MsbOnLeft = True):
    '''
    Get the two's complement of a binary string.

    It uses the shortcut method of finding two's complement of a binary string,
    which is to replicate the bits in the original binary string into the
    two's complement from the least significant bit to the most significant bit
    until the first '1' bit is found in the original binary string. After that,
    the remaining bits are inverted.

    '''
    assert bin_valid(x), "Invalid input"
    string = x
    result = []
    if MsbOnLeft == True:
        string = string [::-1] #flip the string to iterate from LSB
    else:
        pass   
    OneFound = False #switch for determining whether a '1' bit is found
    for i in string:
        if OneFound == False:
            #bit will be replicated if 1 isn't found
            bit = i 
            if bit == '1':
                OneFound = True
            else:
                pass
        elif OneFound == True:
            #bit will be flipped if 1 is found
            if i == '1':
                bit = '0' 
            elif i == '0':
                bit = '1'
            else:
                return "sth wrong happened with the program"
        else:
            return "sth wrong happened with the program"
        result.insert(0, bit)
    return ''.join(result)

def twoaddition(x,y, MsbOnLeft = True):
    '''
    twoaddition - reusues the algorithm in bitadder, but performs
    a two's complement conversion for signed binary with 1 at MSB, and
    discards the carry out.
    '''
    assert bin_valid(x) and bin_valid(y),\
           "one of the inputs is not valid!"
    carry = 0
    result = []

    #sign bit padding for x
    if x[0] == '0':
        x = x.rjust(max(len(x), len(y)),'0')
    elif x[0] == '1':
        x = x.rjust(max(len(x), len(y)),'1')
    else:
        pass

    #sign bit padding for y
    if y[0] == '0':
        y = y.rjust(max(len(x), len(y)),'0')
    elif y[0] == '1':
        y = y.rjust(max(len(x), len(y)),'1')
    else:
        pass

    for i,j in itertools.zip_longest(str(x)[::-1], str(y)[::-1]):
        if (i == '0' or i == '1') and (j == '0' or j == '1'):
            bit = (int(i)^int(j))^carry
            carry = int(i)&int(j)|int(i)&carry|int(j)&carry
            result.insert(0, str(bit))
        else:
            return "invalid input for x or y\
 - they must both be binary strings of the same length! (twoaddition, line 126)"
    return ''.join(result)

def unsignedMultiplication(x,y,MsbOnLeft=True):
    '''
    unsignedMultiplication - takes two unsigned binary strings, converts them into int,
    returns the product of two as a binary string
    '''
    x = int(x, 2)
    y = int(y, 2)
    output = x*y
    output = bin(output)
    return output[2:]

def twosMultiplication(x,y,MsbOnLeft=True):
    '''
    twosMultiplication - takes two binary strings, multiplies them bit by bit
    using the algorithm for two's complement multiplication.
    '''
    assert bin_valid(x) and bin_valid(y),\
           "one of the inputs is not valid!"
    negativeMultiplier = False
    if y[0] == '1':
        negativeMultiplier = True
    else:
        pass
    if MsbOnLeft == True:
        x = x[::-1]
        y = y[::-1]
    j = 0
    sum1,sum2,intermediate = [],[],[]
    while j < len(y) and negativeMultiplier == False:
        i=0
        sum1.append('0'*j) #add a number of 0s to the back equivalent to the value of j
        while i < len(x):
            bit = int(x[i]) & int(y[j])
            sum1.insert(0, str(bit))
            i = i + 1
        if j % 2 == 0:
            sum1.insert(0, sum1[0]*(len(y)-j-1))
            try:
                intermediate = list(twoaddition(''.join(sum1), ''.join(sum2)))
            except Exception as e:
                #print(e)
                intermediate = list(twoaddition(''.join(sum1), '0'))
            sum2 = copy.copy(intermediate)
            intermediate = []
        elif j % 2 == 1:
            sum1.insert(0, sum1[0]*(len(y)-j-1))
            try:
                intermediate = list(twoaddition(''.join(sum1), ''.join(sum2)))
            except Exception as e:
                #print(e)
                intermediate = list(twoaddition(''.join(sum1), '0'))
            sum2 = []
            sum2 = copy.copy(intermediate)
            sum1 = []
            intermediate = []
        sum1 = []
        j = j + 1
    if negativeMultiplier == True:
        while j < len(y)-1:
            i=0
            sum1.append('0'*j) #add a number of 0s to the back equivalent to the value of j
            while i < len(x):
                bit = int(x[i]) & int(y[j])
                sum1.insert(0, str(bit))
                i = i + 1
            if j % 2 == 0:
                sum1.insert(0, sum1[0]*(len(y)-j-1))
                #smth feels wonky abt this entire block - what is the intermediate for?
                try:
                    intermediate = list(twoaddition(''.join(sum1), ''.join(sum2)))
                except Exception as e:
                    #print(e)
                    intermediate = list(twoaddition(''.join(sum1), '0'))
                sum2 = copy.copy(intermediate)
                intermediate = []
            elif j % 2 == 1:
                sum1.insert(0, sum1[0]*(len(y)-j-1))
                try:
                    intermediate = list(twoaddition(''.join(sum1), ''.join(sum2)))
                except Exception as e:
                    #print(e)
                    intermediate = list(twoaddition(''.join(sum1), '0'))
                sum2 = []
                sum2 = copy.copy(intermediate)
                #sum1 = [] #gonna try commenting this out
                intermediate = []
            sum1 = []
            j = j + 1
        sum1 = str(twocomplement(x[::-1])) + '0'*j
        sum2 = list(twoaddition(''.join(sum2), str(sum1)))
    return ''.join(sum2)
            
def twosubtraction(x,y,MsbOnLeft=True):
    assert bin_valid(x) and bin_valid(y),\
       "one of the inputs is not valid!"
    return twoaddition(x, twocomplement(y))

def bin_valid(x):
    '''Checks whether x is a binary string, which is a string only comprised of
1 and 0'''
    assert isinstance(x,str), "the number is not a string!"
    try:
        eval('0b{}'.format(x)) #check if x is a valid binary string
    except SyntaxError:
        return False
    return True

if __name__ == '__main__':
    choice = str
    while choice != 'q':
        choice = input("Hello! Please choose the operation that you wish to perform:\
    \n\n\t 1. Send 'ba' for addition of two unsigned binary strings.\n\t 2. Send 'tc' for the \
two's complement of a binary string. \n\t 3. Send 'ta' for two's complement addition of two\
binary strings. \n\t 4. Send 'um' for multiplication of two unsigned binary strings.\
\n\t 5. Send 'tm' for two's complement multiplication. \n\t 6. Send 'ts' for two's complement\
subtraction of y from x. \n\nLastly, send 'q' to exit. ")
        if choice.lower() == 'ba':
            a = input("Enter the first binary string: ")
            b = input("Enter the second binary string: ")
            print(bitadder(a,b))
        elif choice.lower() == 'tc':
            a = input("Enter the binary string to obtain two's complement from: ")
            print(twocomplement(a))
        elif choice.lower() == 'ta':
            a = input("Enter the first binary string: ")
            b = input("Enter the second binary string: ")
            print(twoaddition(a, b))
        elif choice.lower() == 'um':
            a = input("Enter the first binary string: ")
            b = input("Enter the second binary string: ")
            print(unsignedMultiplication(a,b))
        elif choice.lower() == 'tm':
            a = input("Enter the first binary string: ")
            b = input("Enter the second binary string: ")
            print(twosMultiplication(a,b))
        elif choice.lower() == 'ts':
            a = input("Enter the first binary string: ")
            b = input("Enter the second binary string: ")
            print(twosubtraction(a,b))


