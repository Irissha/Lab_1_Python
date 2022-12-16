with open('text.txt') as f:
  n = int(f.readline())
  for i in range(n):
    a, b = map(int, f.readline().split())
    print(a+b)
