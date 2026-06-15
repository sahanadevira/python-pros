python
# repeat.py
text = input("enter input string:")
result = ""
i = 0
while i < len(text):
    char = text[i]
    num = int(text[i+1])
    result += char * num
    i += 2
print("output:", result)
