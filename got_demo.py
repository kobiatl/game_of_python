from pprint import pprint
from characters import characters

count = 0

for character in characters:
    if character['died'] != '':
        count += 1
print(count)




# print(len(characters))

# # print out the key names individually
# for k in jon_snow:
#    print(k)

# # print out just the values
# for key in jon_snow:
#    print(jon_snow[key])

# # print both the key and the value
# for k in characters.jon_snow:
#    print("%s: %s" % (k, jon_snow[k]))
