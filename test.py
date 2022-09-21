array_numbers={}
numbers=['0701', 'Airtel', 'Nigeria', '07020', 'Smile', '07025', 'MTN', 'Nigeria', '(formerly', 'Visafone)', '07026', 'MTN', 'Nigeria', '(formerly', 'Visafone)', '07027', 'Multi-Links', '07028', 'Starcomms', '07029', 'Starcomms', '0703', 'MTN', 'Nigeria', '0704', 'MTN', 'Nigeria', '(formerly', 'Visafone[3])', '0705', 'Globacom', '0706', 'MTN', 'Nigeria', '0707', 'ZoomMobile', '(formerly', 'Reltel)', '0708', 'Airtel', 'Nigeria', '0709', 'Multi-Links', '0802', 'Airtel', 'Nigeria', '0803', 'MTN', 'Nigeria', '0804', 'Mtel', '0805', 'Globacom', '0806', 'MTN', 'Nigeria', '0807', 'Globacom', '0808', 'Airtel', 'Nigeria', '0809', '9mobile', '0810', 'MTN', 'Nigeria', '0811', 'Globacom', '0812', 'Airtel', 'Nigeria', '0813', 'MTN', 'Nigeria', '0814', 'MTN', 'Nigeria', '0815', 'Globacom', '0816', 'MTN', 'Nigeria', '0817', '9mobile', '0818', '9mobile', '0819', 'Starcomms', '0909', '9mobile', '0908', '9mobile', '0901', 'Airtel', 'Nigeria', '0902', 'Airtel', 'Nigeria', '0903', 'MTN', 'Nigeria', '0904', 'Airtel', 'Nigeria', '0905', 'Globacom', '0906', 'MTN', 'Nigeria', '0907', 'Airtel', 'Nigeria', '0915', 'Globacom', '0913', 'MTN', 'Nigeria', '0912', 'Airtel', 'Nigeria', '0916', 'MTN', 'Nigeria']
numbers__= ['1','abi','2','let','3','abi','4','cd','5','abi']
for i in numbers:
    if i.isnumeric():
        next = numbers[numbers.index(i)+1]
        if next in array_numbers:
            array_numbers[next].append(i)
        else:
            array_numbers[next]=[] 
            array_numbers[next].append(i)
print(array_numbers)
# this is what andy and i have been talking about