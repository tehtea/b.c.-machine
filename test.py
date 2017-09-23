import unittest
import bcmachine

class TestBCMachineFunctions(unittest.TestCase):

    def test_bitadder(self):
        self.assertEqual(bcmachine.bitadder('100000', '011111'), '111111')
        self.assertEqual(bcmachine.bitadder('1111','11'),'10010')
##        with self.assertRaises(AssertionError) as cm:
##            bitadder.bitadder('01110', '01','1')
##        the_exception = cm.exception
##        #self.assertEqual(the_exception, 'AssertionError\(\'carry in is not 0 or 1!\')')
        self.assertEqual(bcmachine.bitadder('01110', '10', 1),'10001')
        with self.assertRaises(AssertionError) as cm:
            bcmachine.bitadder('cat','dog'),'catdog'
        the_exception = cm.exception
        self.assertEqual(the_exception.__str__(), 'one of the inputs is not valid!')
    def test_twocomplement(self):
        self.assertEqual(bcmachine.twocomplement('1000'),'1000') #should this be the case, in rl?
        self.assertEqual(bcmachine.twocomplement('01000'),'11000')
        self.assertEqual(bcmachine.twocomplement('1111'),'0001')
    def test_unsignedMultiplication(self):
        self.assertEqual(bcmachine.unsignedMultiplication('100','10010'),'1001000')
        self.assertEqual(bcmachine.unsignedMultiplication('01111110','0111'),'1101110010')
    def test_twoaddition(self):
        #need to come up with different cases for twoaddition
        #overflow conditions - operator, operand
        #add by negative number, add by positive number
        self.assertEqual(bcmachine.twoaddition('10001','00010'),'10011')
        self.assertEqual(bcmachine.twoaddition('0100101','10101'),'0011010')
        self.assertEqual(bcmachine.twoaddition('1110111','10001'),'1101000')
        self.assertEqual(bcmachine.twoaddition('1000010', '1010'),'0111100')
        self.assertEqual(bcmachine.twoaddition('0111101', '0111110'),'1111011')
        self.assertEqual(bcmachine.twoaddition('0111101', '0'),'0111101')
    def test_twosMultiplication(self):
        self.assertEqual(bcmachine.twosMultiplication('100010','0101'),'101101010')
        self.assertEqual(bcmachine.twosMultiplication('100010','1101'),'001011010')
        self.assertEqual(bcmachine.twosMultiplication('0111011','01111'),'01101110101')
    def test_twosubtraction(self):
        self.assertEqual(bcmachine.twosubtraction('0111', '1111'),'1000')
        self.assertEqual(bcmachine.twosubtraction('0101', '01101'),'11000')

        
'''
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
'''
if __name__ == '__main__':
    unittest.main()
