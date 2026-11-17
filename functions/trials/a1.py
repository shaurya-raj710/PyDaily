def add_item(lst):
    lst.append(99)

nums = [1, 2, 3]
add_item(nums)
print(nums) 

# the list gets changed but variables dont
# this is because , lists are passed by refrence


def replace(lst):
    lst = [7, 7, 7] 
    
          # rebinds the LOCAL name
nums = [1, 2, 3]
replace(nums)
print(nums)

# this did not work... because we are not 