user_input = input("Please Enter 3 numbers, separate each number with a comma:")
string_tokens = user_input.split(",")
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))
a, b, c = int_tokens
result = a + b - c
print(result)