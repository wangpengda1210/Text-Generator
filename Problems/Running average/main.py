numbers = [int(num) for num in input()]
print([sum(numbers[i - 2:i]) / 2 for i in range(2, len(numbers) + 1)])
