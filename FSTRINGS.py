import math
from datetime import datetime

me = "Harry"
a1 = 3
# a = "this is %s %s"%(me,a1)
# a = "This is {1} {0}"
# b = a.format(me,a1)
# print(b)

# F string
a = f"this is {me} {a1} {math.cos(65)} {datetime.today()}"
print(a)