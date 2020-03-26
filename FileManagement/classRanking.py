class Ranking(object):                                          
    """A simple Class of 3 integer values:
       newest - The newest clip held by tracking array
       current - the current clip of concern in tracking array
       oldest - The oldest clip held by tracking array
    """
    def __init__(self, newest: int, current: int, oldest: int): # Python's reserved Function, called each time instantiated
        self.newest = newest
        self.current = current
        self.oldest = oldest

    def update_ranking(self, sizeOfArray):                      # Updates the Ranking
        self.newest = self.current                              # Newest clip becomes the previous current
        self.current = self.oldest                              # New current becomes the previous oldest
        if self.oldest == sizeOfArray:                          # oldest loops back to zero if at limit
            self.oldest = 0                                     # or
        else:                                                   # iterates by one
            self.oldest = self.oldest + 1
        print("Ranking Updated")
