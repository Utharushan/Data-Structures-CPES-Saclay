class stack:
    """Class defining a stack"""

    def __init__(self, values=[]):
        self.values = list(values)

    def is_empty(self):
        """returns True if the stack is empty, False otherwise"""
        return self.values == []
    
    def push(self, c):
        """puts the element c at the top of the stack"""
        self.values.append(c)
        
    def pop(self):
        """ deletes the element at the top of the stack, if there is one. """
        if not self.is_empty():
            return self.values.pop()
        
    def peek(self):
        """returns the element at the top of the stack, if there is one. """
        if not self.is_empty():
            return self.values[-1]
        
    def size(self):
        """returns the length of the stack """
        return len(self.values)

    def __str__(self) :
        """ pretty print """
        if len(self.values)==0:
            return "[)"
        s = "["
        for e in self.values :
            s+=str(e)+"|"
        return s[:-1]+")"

    def __del__(self) :
        del self.values
