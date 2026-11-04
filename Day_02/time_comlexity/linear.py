#Example 1:
def find_sum(n):                  #Time Complexity is O(n)
    total = 0                     #Space Complexity is O(1)  : n, total, i these are the variables used in the function
    for i in range(n):
        total += i
    return total
print(find_sum(5))



#Example 2:
def count_even(arr):
    count = 0
    for n in arr:
        if n % 2 == 0:
            count += 1
    return count
print(count_even([1, 2, 3, 4, 5, 6]))




#Example 3:
def largest_num(arr):
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
        return largest
print(largest_num([10, 25, 5, 45, 30]))