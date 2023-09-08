class Student:


    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def tostudy (self):
        print('Time to study!')
        self.progress += 0.12
        self.gladness -= 3
    
    def to_sleep(self):
       print("I will sleap")
       self.gradnes += 3

    def tochill(self):
       self.gradnes += 5
       self.progress -= 0.1
    def is_alive(self):
        if self.progress < 0.5:
            print("cast lout")
            self.alive = False 
        elif self.gladness <= 0:
            print("Depresion") 
            self.alive = False
        elif self.progress < 5:
            print("passed externally")
            self.alive = False

    def end_day(self):
        print(f'Glandes = {self.gladness}')
        print(f'Progres = {round(self.progress, 2)}')   
    def live(self, day):
        day = 'day' + str(day) + 'of' + self.name + 'life'
        print(f'{day:=500}')         
