#! /usr/bin/env python
# -*- coding: utf-8 -*-


from time import *

print('Use \'ctrl+c\' to Exit\n')
min = 0
print('Work Checker is running properly!\n')

i = input("Wanna change \'cycle-time\'? (Type \'yes\' or \'YES\' or 1): ")
if i in ('yes', 'YES', '1'):
  try:
    x = int(input('\nSet \'cycle-time\' to ? minutes '))
    assert x>0
  except:
    print("Invalid time!")
    print('Setting \'cycle-time\' to defualt(5) minutes in next 5 seconds.\n')
    for _ in range(1,6):
      print(_)
      sleep(1)
    x = 5
else:
  print('Setting \'cycle-time\' to defualt(5) minutes in next 5 seconds.\n')
  for _ in range(1,5):
    print(str(_)+'..', end='')
    sleep(1)
  print(5)
  x = 5


while True:

  if min ==0:
    print('')
    print(ctime())
    print('')
    print('Cycle is running properly!')
    print('')
    print('COFFE & CODE!!')
    print('')
    print('Net Time initiallized to 0 Minutes.')
    print('')
    print('')
    print('')
  else:
    print(x, 'minutes has passed  $$ Total Time elapsed:',min, 'Minutes')

  min += x
  sleep(x*60)
