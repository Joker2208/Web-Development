class A:
    id = 20
    def test(self):
        print("test calling")

class B(A):
    def sample(self):
        print(self.id)
        print("Sample calling")

b = B()
b.sample()
b.test()


        