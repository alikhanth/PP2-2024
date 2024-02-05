def unique_elements(list):
    result_list = []
    for element in list:
        if element not in result_list:
            result_list.append(element)
    return result_list
list = [1, 2, 2, 3, 4, 4, 5]
unique_list = unique_elements(list)
print(unique_list)
