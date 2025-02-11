def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

sample_list = [1, 2, 3, 2, 4, 5, 1, 6, 4]
print("List after removing duplicates:", remove_duplicates(sample_list))
