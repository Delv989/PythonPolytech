numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_of_missing_element = numbers.index(None)
sum_numbers = sum(numbers[:index_of_missing_element])+sum(numbers[index_of_missing_element+1:])
count_numbers = len(numbers)
average_numbers = sum_numbers/count_numbers

numbers[index_of_missing_element] = average_numbers
print("Измененный список:", numbers)
