array_numbers={}
numbers= [1,'abi',2,'let',3,'abi',4,'cd',5,'abi']
for i in numbers:
    next = numbers[numbers.index(i)+1]
    if i in array_numbers:
        array_numbers[i].append(next)
    else:
        array_numbers[i]=[] 
        array_numbers[i].append(next)
print(array_numbers)