#we're creating a field element so we can define ECC math
# this is straight out of the Programming Bitcoin book

class FieldElement:

    def __init__(self,num,prime):
        if num>=prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(num, prime-1)
            raise ValueError(error)
        self.num = num
        self.prime = prime
        
    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime,self.num)
        
    def __eq__(self,o):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime
    
    def __neq__(self,o):
        pass
    def __add__(self,o):
        pass
    def __sub__(self,o):
        pass
    def __mul__(self,o):
        pass
    def __div__(self,o):
        pass
    def __pow__(self,o):
        pass
    
