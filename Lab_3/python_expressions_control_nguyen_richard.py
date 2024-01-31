#Part 8: boolean
print(f"a: {20 > 12}")
print(f"b: {20 < 12}")
print(f"c: {20 == 12}")

#Part 9: boolean is int
print(f"Is 15 less than 12?", int(15<12))
print(f"Is 20 equal to 20?", int(20 == 20))

#Part 10: Literals and Variables
my_name = "richard"
my_age = 22
print(f"a: {17}")
print(f"b: {'Hi'}")
print(f"c: {True}")
print(f"d: {my_name}")
print(f"e: {my_age}")

#Part 11: Precedence
print((4+10/2),(4+1*6))
print((4*10/2),(4/1-6))
print((4/10-2),(4-1+6))

#Part 12: Relational Operators
print(f"Is 'rich' == 'richard'? {'rich' == 'richard'}")

#Part 13: Equality Operators
my_name = "rich"
print("assignment: ", my_name)
print("equality: ", my_name == "rich")

#Part 14: Comparison Operators
print("comparison:", "aa" > "a")
print("comparison:", 1 < 2)

a = 7
b = 13
print(f"Comparision: {a} is greater than {b}" if a > b else "")
print(f"Comparision: {a} is less than {b}" if a < b else "")
print(f"Comparision: {a} is greater than or equal to {b}" if a >= b else "")
print(f"Comparision: {a} is less than or equal to {b}" if a <= b else "")

#Part 15: If Statements
my_bank_balance = 0
if my_bank_balance < 100:
    money = 150
    my_bank_balance += money

#Part 16: Else Statements
my_bank_balance = 0
if my_bank_balance > 100:
    money = 150
    my_bank_balance += money
else:
    print("I'm poor")

#Part 17: Elif Statements
checking = 200
savings = 3500
if checking < 1000:
    money = 500
    checking += money
elif checking > 100:
    savings += 200
    checking -= 200
else:
    savings += 100
    checking -= 100
print(checking)
print(savings)

#Part 18: Ternary Statements
fuel = 7
print("Fill tank now" if fuel <= 10 else "There's not enough fuel")

#While Loops
fuel = 10
while fuel > 1:
    print("There's not enough fuel")
    fuel -=1

#For Loops
movies = ["barbie", "oppenheimer", "tmnt"]
for movie in movies:
    print(f"movie: {movie}")
for i in range (5):
    print(f'i: {i}')

for count in range(10):
    print(f"{count} times 7 is {count * 7}")
    if count == 5:
        break

for count in range(10):
    if count == 5:
        continue
    print(f"{count} times 7 is {count * 7}")