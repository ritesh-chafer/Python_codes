import random
s = 'abcde'
print("choice(abcde):", random.choice(s))

list = [10, 2, 3, 1, 8, 19]
print("shuffle(list):", random.shuffle(list))                     # shuffles the item in list, returns none
print("random.seed(20):", random.seed(20))                        # Gives the starting value for generatig a random number. Returns none.
print("random():",random.random())                                # Returns a random floating-point number which lies between 0 and 1
print("uniform(2,3):",random.uniform(2,3))                        # Generates random floating-point number n such that n>x and n<y
print("randrange(2,10,1):",random.randrange(3,10,1))              # randrange(start,stop,step)