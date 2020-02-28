
def main():
  l = [1,2,3,4]
  l.append('toby')
  print(f'l: {l}', '\n')

  l.clear()
  print('clear(): ', l, '\n')

  target = ['im the target']
  l = target.copy()
  print(f"""
target = ['im the target']
l = target.copy()
l: {l}
  """)

  
  l.extend([1, 2, 3])
  print('l.extend([1, 2, 3]): ', l, '\n')

  l = [3,2,6,4,1]
  print('l: ', l)
  print('l.index(6, 0, 3): ', l.index(6, 0, 3), '\n')

  print('pop(): ', l.pop(1))
  print('l: ', l, '\n')

  l.remove(6)
  print('l.remove(): ', l, '\n')

  l.reverse()
  print(f'l.reverse(): {l}', '\n')

  l.sort()
  print(f'l.sort(): {l}', '\n')


  print(f'l[-1] (ith item): {l[-1]}', '\n')
  l = [1,2,3,4,5,6,7,8,9,10]
  print(f'l[1::2] (start @ 1 index & increment by 2): {l[1::2]}', '\n')

  print('l * 3', l * 3, '\n')

if __name__ == "__main__":
  main()
