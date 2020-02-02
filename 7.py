class Time:
    def __init__(self):
        self.clock = None
        self.minutes = None
        self.seconds = None
        
    def time_enter(self):
        self.clock = input('Clock: ')
        self.minutes = input('Minutes: ')
        self.seconds = input('Seconds: ')
        
    def time_print(self):
        print(f'{self.clock}.{self.minutes}.{self.seconds}')


t = Time()
t.time_enter()
t.time_print()