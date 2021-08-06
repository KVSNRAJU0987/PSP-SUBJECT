#looping backwards   
    
colors = ['orange', 'grey', 'pink', 'red']


for i in range(len(colors)-1,-1,-1):
    print(colors[i])
    
colors = ['orange', 'grey', 'pink', 'red']
for color in reversed(colors):
    print(color)

names = ['harsha' , 'vardhan' , 'vamsi' , 'raju']
behavior = ['naughty', 'innocent', 'innocent', 'naughty']
n = min(len(names) , len(behavior))
for i in range(n):
    print(names[i] , '-->' , behavior[i])
   
names = ['harsha' , 'vardhan' , 'vamsi' , 'raju']
behavior = ['naughty', 'innocent', 'innocent', 'naughty']    
for name, behavior in zip(names, behavior):
    print(name, '-->',behavior)

names = ['harsha' , 'vardhan' , 'vamsi' , 'raju']
behavior = ['naughty', 'innocent', 'innocent', 'naughty']
for name,color in zip(names, behavior):
    print(name,'-->',behavior)
  
#sorted list
names = ['harsha' , 'vardhan' , 'vamsi' , 'raju']
for names in sorted(names):
    print(names)
  
names = ['harsha' , 'vardhan' , 'vamsi' , 'raju']
print(sorted(names, key = len))

#Looping over dictionary keys

d = {'harsha': 'pink', 'vamsi': 'grey', 'raju': 'orange'}

for i in d.keys():
    print(i)
 
d = {'harsha': 'pink', 'vamsi': 'grey', 'raju': 'orange'}


for i in d.keys():
    if i.startswith('m'):
         print(i)


#Looping over a range of numbers

for i in [0, 1, 2, 3, 4, 5]:
    print(i**2)

for i in range(6):
    print(i**2)
  
#Looping over a collection
colors = ['orange', 'grey', 'pink', 'green']

for i in range(len(colors)):
    print(colors[i])

colors = ['orange', 'grey', 'pink', 'green']

for color in colors:
    print(color)

# by using and and or

x = int(input("Please enter a number between 1 and 10: "))

if x > 0 and x < 11:
	print(x)
else:
	print("Invalid selection")


x = int(input("Please enter a number between 1 and 10: "))

if x < 1 or x > 10:
	print("Invalid selection")
else:
	print(x)



# by usiing of list in differnt way

student=("harsha","vardhan","vamsi","raju","rohit")
print(student[0:3])

student=("harsha","vardhan","vamsi","raju","rohit")
print(student[:3])

# by using list-

list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4]
  
print(list1)
print(list2)

list1 = [5, 4, 3, 2, 1]
list1 = list1 + [1, 2, 3, 4]
list2 = list1

print(list1)
print(list2)

#example(15)-

my_list = ['raju', 'harsha', 'bhuvi']
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

my_list = ['raju', 'harsha', 'bhuvi']
for element in my_list:
    print(element)
 
# example(16)-

def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
        L.append(a)
        return L
print(f(1))
print(f(2))
print(f(3))


#example(17)-

def print_list(list_value, sep):
    print('{}'.format(sep).join(list_value))
the_list = ['a', 'b', 'c']
the_other_list = ['raju', 'harsha', 'bhuvi']
print_list(the_list, ' ')
print_list(the_other_list, ' ')
print_list(the_other_list, ', ')

def print_list(list_value, sep=' '):
    print('{}'.format(sep).join(list_value))
the_list = ['a', 'b', 'c']
the_other_list = ['raju', 'harsha', 'bhuvi']
print_list(the_list)
print_list(the_other_list)
print_list(the_other_list, ', ')


# example-

def all_equal(a, b, c):
    result = False
    if a == b == c:
        result = False
        if a == b == c:
            result = True
            return result
        
def all_equal(a, b, c):
    return a == b == c


# example-

def add(x,y):
    return x+y
x=3
y=4
z = add(x,y)
print(z)

adder = lambda x,y: x+y
print(adder(3,4))



# example-
students = ["raju" , "harsha" , "vamsi", "bhuvi" , "vardhan"]
print(students[-1])

students = ["raju" , "harsha" , "vamsi", "bhuvi" , "vardhan"]
print(students[-1])


