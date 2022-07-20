def sum_of_ascii(input_string):
    sum = 0
    for i in input_string:
        var = ord(i)
        sum = sum + var
    return sum
total =sum_of_ascii('navneet')
print(total)

def summ_of_ascii(innput_string):
    return sum(map(ord,innput_string))
varr = summ_of_ascii('neets')
print(varr)

print(map(len,[['nav'],['neet']]))