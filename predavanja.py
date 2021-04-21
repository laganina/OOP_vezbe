'''primes = [2,3,5,7]
for prime in primes:
    print(prime)

    square = 0
    number = 1
    while square < 81:
        square = number**2
        print(square)
        number += 1

    var1 = 'Moj tekst'
    print(var1[1])
    print(var1[3:])
    print(var1[0:])
    print(var1[1:])
'''

class Student:
    def __init__(self,ime,prez,id):
        self._name = ime
        self.lastname = prez
        self.__index = id
    def get_index(self):
        return self.__index
    def set_index(self, id):
        self.__index = id
    def to_string(self):
        return 'name:'+ self._name + ', lastname:' + self.lastname + ', index:' + str(self.__index)
s = Student('Stevan','Stevanovic',1234)
s.get_index()
s.set_index(345)
print(s.get_index())

class Diplomac(Student):
    def __init__(self, ime, prez, id, prosek):
        super().__init__(ime, prez, id)
        self.prosek = prosek
    def print_index(self):
        print(self.get_index())

o = Diplomac('Pera','Sindjelic',6543, 8.98)
o.print_index()
