# ég er að fara finna stærstu tölu sem er sett inn
max_int = 0
num_int = 0
while num_int >=0:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > max_int:
        max_int = num_int
print("The maximum is", max_int)
