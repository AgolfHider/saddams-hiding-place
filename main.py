class Son1:
    def __init__(self):
        self.attribute_son1 = "Attribute from Son1"
    
    def method_son1(self):
        return "Method from Son1"

class Son2:
    def __init__(self):
        self.attribute_son2 = "Attribute from Son2"
    
    def method_son2(self):
        return "Method from Son2"

class Son3:
    def __init__(self):
        self.attribute_son3 = "Attribute from Son3"
    
    def method_son3(self):
        return "Method from Son3"

class Father:
    def __init__(self):
        self.son1 = Son1()
        self.son2 = Son2()
        self.son3 = Son3()

    def show_all_attributes_and_methods(self):
        print(self.son1.attribute_son1)
        print(self.son1.method_son1())
        
        print(self.son2.attribute_son2)
        print(self.son2.method_son2())
        
        print(self.son3.attribute_son3)
        print(self.son3.method_son3())

father_instance = Father()
father_instance.show_all_attributes_and_methods()
