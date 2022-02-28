# x = input("Enter list items:").split(" ,")
# print(x)

# a = 9
# b = a

# if id(a) is not id(b):
#     print("done")
# else:
#     print(id(a))
#     print(id(b))


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print(self.model)
        print(self.color)


audi = Car('model84', 'blue')

print(audi.model)
