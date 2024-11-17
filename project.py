class MyArray:
    
    araye = [0] * 50
    s = 0

    def __init__(self):
        pass

    def Insert(index, value):    
        for a in range(MyArray.s, index, -1):
            MyArray.araye[a] = MyArray.araye[a - 1]    
        MyArray.araye[index] = value
        MyArray.s += 1          

    def Append(value):
        MyArray.araye[MyArray.s] = value
        MyArray.s += 1  
                

    def Delete_By_Value(value):
        for a in range(MyArray.s):
            if MyArray.araye[a] == value:
                for b in range(a, MyArray.s - 1):
                    MyArray.araye[b] = MyArray.araye[b + 1]
                MyArray.s -= 1
                return a
        return -1   

    def Delete_By_Index(index):
        for a in range(index, MyArray.s - 1):
            MyArray.araye[a] = MyArray.araye[a + 1]
        MyArray.s -= 1     

    def Search_By_Value(value):
        for a in range(MyArray.s):
            if MyArray.araye[a] == value:
                return a
            
        return -1
    
    def Reverse():
        for i in range(MyArray.s // 2):
            temp = MyArray.araye[i]
            MyArray.araye[i] = MyArray.araye[MyArray.s - i - 1]
            MyArray.araye[MyArray.s - i - 1] = temp

    def Display():
        for a in range(MyArray.s):
            print(MyArray.araye[a])        


my_array = MyArray

my_array.Append(2)
my_array.Append(4)
my_array.Append(15)
my_array.Append(11)
my_array.Display()    


my_array.Insert(2, 3)
my_array.Display()


my_array.Reverse()
my_array.Display()


v = my_array.Search_By_Value(15)
if v == -1:
    print("There's no such value")
else:    
    print(v)


my_array.Delete_By_Index(3)
my_array.Display()


d = my_array.Delete_By_Value(2)
my_array.Display()
