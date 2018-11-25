# generate a password with length "passlen" with no duplicate characters in the password

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print p

# And here is another, using internal Python functions:
#
# import string
# import random
#
# def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
# 	return ''.join(random.choice(chars) for _ in range(size))
#
# print
