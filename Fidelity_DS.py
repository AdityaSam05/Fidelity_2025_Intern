#Takes list as argument and the function will return a list that contains only numbers
def filter_numbers(list):
    """This function returns list of numbers."""
    return [i for i in list if list[i]==int]

list1=[1,2,3,'hello',7.2,'a']
num_list=filter_numbers(list1)
print(num_list)