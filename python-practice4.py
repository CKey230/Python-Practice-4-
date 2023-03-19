#max_num()
def max_num(a, b, c):
    if a > b and a > c:
        return a 
    elif b > a and b > c: 
        return b 
    else: return c
print(max_num(3,8,6))

#mult_list()
def mult_list(list):
    result=1
    for num in list: 
        result *= num
    return result
    
my_list = [2, 3, 4, 5]
result = mult_list(my_list)
print(result)

#rev_string()
def rev_string(str):
    return str[::-1]

my_string = 'hello world'
reversed_string = rev_string(my_string)
print(reversed_string)

#num_within() 
def num_within(num, start, end):
    if start <= num <= end:
        return True
    else: 
        return False

result= num_within(3,2,4)
print(result) #true

result = num_within(3,1,3)
print(result) #true

result = num_within(10,2,5)
print(result) #false

#Pascal's Triangle
def pascal(n):
    row = [1]
    for i in range(n):
        print(row)

        next_row = [1]
        for j in range(len(row) - 1):
            next_row.append(row[j] + row[j + 1])
        next_row.append(1)
        row = next_row

pascal(5)