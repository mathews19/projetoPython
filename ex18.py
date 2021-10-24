#Functions
#ess aqui é como seus scripts com argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok aquele *args é desnecessário, podemos simplesmente fazer isso

def print_two_again(arg1, arg2):
    print(f"arg1 : {arg1},  arg2: {arg2}")

# Essa recebe apenas 1 argumento 

def print_one(arg1):
    print(f"arg1: {arg1}")

# Essa não recebe argumento

def print_none():
    print("I got nothin\'. ")

print_two("zed", "Shaw")
print_two_again("zed", "Shaw")
print_one("First")
print_none()

