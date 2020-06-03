import re
f = open('Text.txt','r')
if f.mode == 'r':
    contents = f.read()
  
y = re.findall('[]0-9]+', contents)

int_lst = [int(x) for x in y]
print(sum(int_lst))