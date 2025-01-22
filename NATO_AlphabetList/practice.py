# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(n) for n in list_of_strings]
# result = [n for n in numbers if n % 2 == 0]
# print(result)

# result = [set("file1.txt").intersection("file2.txt")]
# print(result)

with open("file1.txt") as file1:
  list1 = file1.readlines()
    
with open("file2.txt") as file2:
  list2 = file2.readlines()
    
result = [int(num) for num in list1 if num in list2]
 
print(result)
