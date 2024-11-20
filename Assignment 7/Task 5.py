#!/usr/bin/env python3

# The signatures of this class and its task methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce grading/protected utility methods though.

class Publication:

    def __init__(self, authors, title, year):
        self.authors = authors
        self.title = title
        self.year = year

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return """Publication(""" + str(self.authors) + ', "' + self.title + """", """ + str(self.year) + """)"""

    def __eq__(self, __value):
        if not isinstance(__value, Publication):
            return NotImplemented
        return hash(self) == hash(__value)

        
    def __hash__(self):
        return hash(str(self))

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.
    # We've provided a starting point for one of the operators:
    def __le__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        elif self.authors < other.authors:
            return True
        elif self.authors > other.authors:
            return False
        elif self.title < other.title:
            return True
        elif self.title > other.title:
            return False
        elif self.year <= other.year:
            return True
        else:
            return False
        
    def __lt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        elif self.authors < other.authors:
            return True
        elif self.authors > other.authors:
            return False
        elif self.title < other.title:
            return True
        elif self.title > other.title:
            return False
        elif self.year < other.year:
            return True
        else:
            return False
        
    def __ge__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        elif self.authors > other.authors:
            return True
        elif self.authors < other.authors:
            return False
        elif self.title > other.title:
            return True
        elif self.title < other.title:
            return False
        elif self.year >= other.year:
            return True
        else:
            return False
        
    def __gt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        elif self.authors > other.authors:
            return True
        elif self.authors < other.authors:
            return False
        elif self.title > other.title:
            return True
        elif self.title < other.title:
            return False
        elif self.year > other.year:
            return True
        else:
            return False


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    print(str(p) == s)

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    print(p1 == p2)  # True
    print(p2 == p3)  # False

    sales = {
        p1: 273,
        p2: 398,
    }
