

class EngCorner:
    """A simple example class of the English Corner"""
    opened = True


    def isAndrewThere(self):
        return self.opened


    def whereIsAndrew(self):
        if(self.opened):
            print( 'Andrew is at the English Corner')
            return

        print( 'Andrew is NOT at the English Corner')


class EnglishCorner:
    """A class with full name of the English Corner"""

    def __init__(self, where='xiao zhou'):
        self.where = where

    def whereIs(self):
        print(self.where)


if __name__ == "__main__":
    print('test something')
