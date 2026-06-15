python
# dup.py
n = input("enter the string:")
result = ""
for char in n:
    if char not in result:
        result += char
print("string after removing duplicates:", result)
