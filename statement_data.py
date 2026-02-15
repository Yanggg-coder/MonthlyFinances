
# Class definition for the Statement Data
class StatementData():

    # Populate the internal class member variables passed in the constructor __init__
    # Default them to None type to catch bad value passes
    def __init__(
            self,
            transaction_month   = None,
            transaction_day     = None,
            posting_month       = None,
            posting_day         = None,
            charge_amount       = None,
            category_type       = None
        ):
        
        self.transaction_month  = transaction_month
        self.transaction_day    = transaction_day
        self.posting_month      = posting_month
        self.posting_day        = posting_day
        self.charge_amount      = charge_amount
        self.category_type      = category_type


        # __dict__ returns a dictionary of the "self" attributes and values
        # for example
        #
        # def __init__(self,x=10,y="fun:):
        #   self.x = x
        #   self.y = y
        #
        # the call self.__dict__ gives the dictionary 
        # { x : 10 , y : "fun " }
        #
        # So, instead of looping over the values manually to print out,
        # we can iterate through the attribute and value in self.__dict__.items()
        for attribute, val in self.__dict__.items():

            # throw an error if a class variable is not initialized correctly
            if (attribute == None):
                raise TypeError(f"{attribute} has not been initialized correctly!")
            if (val == None):
                raise TypeError(f"value for {attribute} has not been initialized correctly!")

    def printStatementData(self):

        # See comment in the constructor __init__ routine for 
        # what this is doing
        for attribute, val in self.__dict__.items():
            print(f"attribute {attribute} has value {val}")


        

