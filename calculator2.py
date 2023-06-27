#f = open("calc_file.txt", mode="r")
#print(f.read())
#print(f.read().splitlines())
#f.read().splitlines()
#for eachline in f.read().splitlines()

with open("calc_file.txt", 'r') as f:
    splitlines = f.read().splitlines()
    #print(splitlines)

total = 0

for eachline in splitlines:
    linebit = eachline.split()
    print(linebit)
    num1 = int(linebit[2])
    num2 = int(linebit[3])
    operation = linebit[1]

    if operation == "+":
        result = num1 + num2
        print(num1, operation, num2)
        print("= " + str(result))
    elif operation == "-":
        result = num1 - num2
        print(num1, operation, num2)
        print("= " + str(result))
    elif operation == "x":
        result = num1 * num2
        print(num1, operation, num2)
        print("= " + str(result))
    elif operation == "/":
        result = num1 / num2
        print(num1, operation, num2)
        print("= " + str(result))

    total += result
print("Total: " + str(total))

f.close()