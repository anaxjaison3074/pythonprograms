def remove_elements(lst):
    del lst[5]  
    del lst[4]  
    del lst[0]  
    return lst

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

modified_list = remove_elements(sample_list)
print("Modified List:", modified_list)
