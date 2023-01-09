def mean(*numbers):
    if not numbers:
        return None
    return sum(numbers)/len(numbers)

print(mean(1,2,3,4))
print(mean(1,22,1,1,2,3,1,321,23,123,1,312))
print(mean())