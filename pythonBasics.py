x = 6
print(x)
string = "string"
print(string)
y = 4
if x > y:
    print("x is greater")

print("Hello World!", end=" ")
print("I will print on the same line.")
print(5*3)

float = 5.67
bool = True
false_bool = False
print(float + bool + false_bool)
print(type(bool))
message = f"my variable is {float} and my boolean is {bool}"
print(message)
#input = input("what is your name: ")
#print(f"hello {input}")
groceries = ['apples', 'bananas', 'carrots']
print(groceries[0])
groceries.append('milk')
print(len(groceries))

age = 54 
if age >= 65:
    print('is senior')
elif age >= 18:
    print('adult')
else:
    print('is minor')



for item in groceries:
    print(item)

def greet(name):
    print(f"Hello, {name}")

name = input("what is your name: ")
print(greet(name))