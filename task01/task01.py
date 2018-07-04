# my version

import random
from collections import Counter
import pandas as pd
import time

'''
    conversion of upper case and lower case
    .upper
    .lower
    .isuper,islower => boolean
    .capitalize

    built-in module string attr
    string.digits + string.ascii_letters
    convert list to str
    `   list1 = ['1', '2', '3']
        str1 = ''.join(list1)
    `
    random module
    random.sample pick  
 '''
init = time.time()
alphatable = "azertyuiopqsdfghjklmwxcvbn"
alpha_uppercase = list(alphatable.upper())
alpha_lowercase = list(alphatable)
digits_table = list("1234567890")
table = alpha_lowercase + alpha_uppercase + digits_table
print(str(random.sample(table, 16)))

serial = []
for i in range(200):
    x = ""
    for j in range(15):
        if j is not 0:
            if (j) % 5 == 0:
                x += "-"

        # x.join(table[random.randint(0, len(table)-1)])
        x += table[random.randint(0, len(table) - 1)]

    serial.append(x)


# print(serial)
# print(time.time()-init)

"""
    rough estimation of time cost = 0.004528999328613281, more stable than the later one,
"""


y = pd.DataFrame(data=serial, columns=['result'])
y.to_csv('serialnum',)
# writer = pd.ExcelFile('serialnum.xlsx')
# y.to_excel(writer, 'Sheet1')
# writer.


# copypaste version

# import random
# import string
#
# # def ger_activation():
# init = time.time()
# number = 0
# list_activation = []
# while number < 201:
#     patter_str = list(string.digits + string.ascii_letters)
#     activation_code = ''.join(random.sample(patter_str, 16))
#     print(activation_code)
#     list_activation.append(activation_code)
#     number += 1
# print(list_activation)
# print(time.time() - init)

# ger_activation()