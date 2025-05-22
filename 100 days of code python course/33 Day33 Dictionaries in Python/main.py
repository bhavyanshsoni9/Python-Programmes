info = {'name':'karan','age':'19','egligible':True}
# print(info)
# print(info.keys())
# print(info.values())

# for value in info.values():
#     print(info[value])

print(info.items())
for key, value in info.items():
    print(f"The value correspoding to the key {key} is {value}")
    