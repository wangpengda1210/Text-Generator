count = int(input())
results = [input().split() for i in range(count)]
winners = [result[0] for result in results if result[1] == "win"]
print(winners)
print(len(winners))
