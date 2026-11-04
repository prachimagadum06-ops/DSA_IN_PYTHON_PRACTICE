arr = [10, 25, 5, 45, 30]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest number:", largest)