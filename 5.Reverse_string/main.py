def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = input("Enter the string---->")

print("The reversed string using loops is :---> ", reverse(s))


print('================================================')

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


print("The reversed string using recursion is :---> ", reverse(s))

print('================================================')

print("The reversed string using Slicing is :---> ", s[::-1])
