class Sample:
    __id = 20       #private

    def set(self,id):   
        self.__id = id     #to change it without NameMangling use setter and getter method

    def get(self):
        print(self.__id)

s =Sample()
s.get()         #without changing the value

s.set(100)      #changes the value of the id
s.get()

