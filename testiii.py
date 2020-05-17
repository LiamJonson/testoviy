def mean(*numbers):
    n = 0 
    for i in numbers:
        print(i)
        n+=i
    return float(n/len(numbers))


print(mean(1,2,2,4))