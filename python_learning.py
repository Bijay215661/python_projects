# class Employee:
#     def __init__(self, fname,lname,pay):
#         self.fname = fname
#         self.lname =lname
#         self.pay = pay
#         self.email = fname + lname + "@gmail.com"

#     def fullname(self):
#         return '{} {}'.format(self.fname, self.lname)




# emp_1 = Employee('Bijay', 'Tamang', 6000000)
# emp_2 = Employee("Anu", "Bk", 600000 )

# print(emp_1.fullname())
# print(emp_2.fullname())




# print(emp_1)
# print(emp_2)



# emp_1.first = "Bijay"
# emp_1.last = "Tamang"
# emp_1.email = "Biaytamang@234gmail.com"
# emp_1.pay = 50000

# emp_2.first = "\nAnu"
# emp_2.last = "Tamang"
# emp_2.email = "tamanganu@234gmail.com"
# emp_2.pay = 40000

# print(emp_1.fname)
# print(emp_1.lname)
# print(emp_1.email)

# print(emp_2.fname)
# print(emp_2.lname)
# print(emp_2.email)

class Employee:
    def __init__(self, fname, lname, email,):
        self.fname = fname
        self.lname = lname
        self.email = email
        
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname,)
        

emp =  Employee(input("Your FName: "), 
                input("Your LName: "), 
                input("Your Email: ")
                )


print(emp.fullname())


        
        





