def func1():
    print "Hello World"

class MyClass:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        
    def hello(self):
        print "A {} {} {}?".format(self.year, self.make, self.model)
        if self.year < 2000:
            print "Your car is old"
        else:
            print "Your car is not too old"
            
    def not_hello(self):
        print "A {} {} {}?".format(self.year, self.make, self.model)
        if self.model == 'Mustang':
            print "My favorite car!"
        else:
            print "Mustangs are the best cars... not yours!"

class MyChildClass(MyClass):
    def hello(self):
        print "Is this a {} {} {}?".format(self.year, self.make, self.model)
        print "Can I have a ride?"

if __name__ == "__main__":
    print "You executed this module, didn't you?"
