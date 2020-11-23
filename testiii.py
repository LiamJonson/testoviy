i = int(input())
x = 'Anja, Tom, Alexandra, Roma'
y = 'Phung'
#x, y = input(),input()
print(int(input() - len([i for i in set(input().split(', ')).union(input().split(', '))]))
