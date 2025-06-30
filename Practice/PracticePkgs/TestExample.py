'''
Created on 16 Jun 2025

@author: User
'''

class TestExample(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        print("param passed is "+params)
        '''
    
    def testModelWorking(self,test):
        print("WOrking of the mode is "+test)
    
obj=TestExample("test")
obj.testModelWorking("Model-o1")