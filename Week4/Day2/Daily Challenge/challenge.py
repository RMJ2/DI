candles = input('How old are you? DD/MM/YYYY')
day, month, year = candles.split('/')
print(year)


year = int(year)
year_count = int(candles[-1])
line = '_'
candle = 'i'
space = ' ' 
top_count = int((11-year_count)/2) 
top_count_right = top_count
if year%2 ==0:
    top_count_right += 1

print(f'{space*8}{top_count*line}{year_count*candle}{top_count_right*line}') 
print({|:H:a:p:p:y:|})
print
long_string = '''
       |:H:a:p:p:y:|
     __|___________|__
    |^^^^^^^^^^^^^^^^^|
    |:B:i:r:t:h:d:a:y:|
    |                 |
    ~~~~~~~~~~~~~~~~~~~
'''
print(long_string)