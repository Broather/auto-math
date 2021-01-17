def faktorials(n):
  if n == 0:
    return 1
  else:
    return n * faktorials(n - 1)


n = int(input('n = '))

for i in range(1, n+1):
    my_list = [str(n) for n in range(1,i+1)]
    string = ' * '.join(my_list)
    print(f'{i}! = {string} = {faktorials(i)}')

    
