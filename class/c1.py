#class definition
class Dog:
    breed = 'Labrador'
    age = 3
    name = 'Tommy'

#object instantiation
dog1 = Dog()
dog1.name = 'Sheru'
dog1.age = 5
dog1.breed = 'German Shepherd'

dog2 = Dog()
dog2.name = 'Rex'
dog2.age = 2
dog2.breed = 'Golden retriever'

dog3 = Dog()
dog3.name = 'Buddy'
dog3.age = 4
dog3.breed = 'Pug'

print(dog1.name, dog1.age, dog1.breed)
print(dog2.name, dog2.age, dog2.breed)
print(dog3.name, dog3.age, dog3.breed)
