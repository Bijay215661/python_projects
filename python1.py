def out_put(a,b,c,d):
    print(a, 'Add')
    print(b, 'Subraction')
    # print(c, 'Multiplay')
    # print(d, 'Devide')
    pass
out_put(1,2,3,4)

user_selet = int(input("Selece your calculation: "))

if user_selet == 1:
    def a():
        add = []
        number_value = int(input('Enter the numbers of addition\n==>'))

        for j in range(number_value):
            numbers = int(input('Enter value: '))
            add.append(numbers)        
        def addition(sum):            
            for num in add:
                sum+=num
            print('Total is =>',sum)
        addition(0)
    a()

if user_selet == 2:
    def b():
        sub = []
        
        number_value = 2
        
        for j in range(number_value):
            numbers = int(input('Enter value: '))
            sub.append(numbers)
            sub.sort()        

        def Subraction(sum):            
            for num in sub:
                sum=num-j-sum
            print('Total is =>',sum)
        Subraction(0)
    b()


