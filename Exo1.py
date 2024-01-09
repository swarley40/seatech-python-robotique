class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    
        
    """
      Give your best code here ( •̀ ω •́ )✧
    """
    def __init__(self, name):
        self.__name = name

    def power_on(self):
        self.__status = 'powerUp' 

    def power_off(self):
        self.__status = 'powerDown' 
    
    
    