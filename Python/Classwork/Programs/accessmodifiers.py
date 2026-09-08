class Demo:
    name = "test"                   #public (default)
    _email = "test@gmail.cpom"      #protected
    __age = 30                      #private

    def test(self):
        print(self.name,self._email,self.__age)

d = Demo()
d._email = "test1@gmial.com"                #chnageable just like that
d.__age = 100                               #wont chnage because python does allow it directly. If need be u have to use nameMangling

d.test()
                          