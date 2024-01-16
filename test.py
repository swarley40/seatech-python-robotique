class Robot():
    
    __power = False
    __action = ''

    @property
    def power(self):
        return self.__power
    
    @power.setter
    def power(self, power):
        self.__power = power

    @property
    def action(self):
