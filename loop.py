from another import numbers_array
import string

new_array = numbers_array
for i in new_array:
    if not i[-1].isnumeric():
        y = (i[-1])
        y = y.replace(' ', '')
    print(i)
print(new_array)
        

x= "  0908\n "

# print("first =" +x.replace(' ', ''))

