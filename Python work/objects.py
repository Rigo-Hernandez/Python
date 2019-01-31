class Person: 
    def __init__(self, name, email, phone,):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count= 0
    
    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name)) 
        self.greeting_count += 1
    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")
    def num_friends(self):
        print(len(self.friends))
    def __str__(self):
        return f'Person: {self.name} {self.email} {self.phone}'

sonny = Person("Sonny","sonny@hotmail.com","483-485-4948")
jordan = Person("Jordan","jordan@aol.com","495-586-3456")
# sonny.greet(jordan)
# jordan.greet(sonny)
# print(sonny.email, sonny.phone)
# print(jordan.email, jordan.phone)
# Person.print_contact_info(sonny)
# jordan.friends.append(sonny)
# print(jordan.friends[0].name)
# sonny.friends.append(jordan)
# print(sonny.friends[0].name)
# print (len(jordan.friends))
# Person.num_friends(jordan)
# Person.num_friends(sonny)
# print (sonny.greeting_count)
# print(str(jordan))




# class Vehicle:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def print_info(self):
#         print(mustang.year,mustang.make,mustang.model)
# mustang = Vehicle("Ford","Mustang","2008")
# mustang.print_info()