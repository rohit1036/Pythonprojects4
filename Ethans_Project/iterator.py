'''class iterator:
    def __init__(self,max=0):
        self.x=0
        self.max=max
    def __iter__(self):
        return self
    def __next__(self):
        if self.x <self.max:
         self.x+=1
         return self.x
        else:
            raise StopIteration
if __name__ == '__main__':
    obj=iterator(2)
    s=iterator.__iter__(obj)
    print(next(s))
    print(next(s))
    print(next(s))'''


class  Parent:
    college='ABC'
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    @classmethod
    def name_roll(cls,name_roll_str):
        name,roll=name_roll_str.split('_')
        return cls(name,roll)
class Child(Parent):
    @classmethod
    def name_roll(cls,name_roll_str):
        name,roll=name_roll_str.split('_')
        return cls(name,roll)
if __name__ =='__main__':
    s=Child.name_roll('rohit_103')
    print(s.name,s.roll)

