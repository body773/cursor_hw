#Task 2.1
my_list=[]
i=11
k=1
for i in range(1,i):
    my_list.append(k)
    k+=3
print("Task 2.1 ",my_list)

#Task 2.2
my_listnew = my_list
my_listnew.extend([1, 5, 13, 20])
print ("Task 2.2 ",my_listnew)

#Task2.3
my_set = set(my_list)
print("Task 2.3 ",my_set)

#Task 2.4
def compare_elements(a:list, b:set):
    if len(a) > len(b):
       return "List is bigger"
    else:
       return "Set is bigger"

print("Task 2.4 ",compare_elements(my_listnew, my_set))

#Task 3
def get_value_from_list(data:list, index:int):
    try:
        return data[index]
    except:
        return "None"

print("Task 3 ",get_value_from_list([1,2,3], 1))
print("Task 3 ",get_value_from_list([1,2,3], 16))

#Task 4
dict = {"Name": "", "Age": "", "Hobby": ""}
def create_dict(name:str, age:int, hobby:str):
    dict["Name"] = name
    dict["Age"] = age
    dict["Hobby"] = hobby
    return dict
print("Task 4",create_dict("Denis", 26, "Books"))

#Task 5

def calculate_fibo(n:int):
    fibo = [0]
    a, b = 0, 1
    for i in range(1,n,1):
        fibo.append(b)
        a, b = b, a + b
    return fibo

print(calculate_fibo(10))
