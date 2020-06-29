class Count(object):
    """Count forward class.
    Does not count backwards"""

    def __init__(self, inb=None, ine=None):
        def count_in():
            """Set input.
            Input the start and finish of some range."""

            if inb == None:
                self.inb = int(input('beginning>>> '))
            else:
                self.inb = inb
            if ine == None:
                self.ine = int(input('end>>> '))
            else:
                self.ine = ine
            return self.inb, self.ine


        def count_validation():
            """Loop to validate input."""

            while True:
                try:
                    self.vind, self.vran = count_in()
                    return self.vind, self.vran+1
                except:
                    print('Invalid input. Try again:\n')


        def count_out(self):
            """Procedure to format and output count."""

            ind, range_ = count_validation()
            print()
            o_str = ''
            while ind < range_:
                ind_str = str(ind)
                if ind==-1:
                    # zero is neutral
                    o_str += '%i'%ind+'\n'
                elif ind_str[-1]=='0':
                    # the last column of top and bottom
                    # zero is here too
                    o_str += '%3i'%ind+'\n'
                elif ind>0:
                    # numbers >0
                    o_str += '%3i'%ind+' '
##                else:
                elif ind<0:
                    # numbers <0
                    o_str += '%i'%ind+' '
                ind+=1
            print(o_str)


        count_out(self)


count3 = count2 = count = Count
# Ask for 2 arguments
##count()
# Set first argument and ask for last argument
##count2(5)
# Ask not for any argument
##count3(-102,102)
count3(1,18000)