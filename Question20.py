######## group three number whose sum is zero
abc=input('Enter list of +/- number separated by space : ').split()
array=[]
for element in abc:
    array.append(int(element))
result=[]
print('Input : ',array)
class Calculation:
    def group_num(self, array):
        array, result, i = sorted(array), [], 0
        while i < len(array) - 2:
            j, k = i + 1, len(array) - 1
            while j < k:
                if array[i] + array[j] + array[k] < 0:
                    j += 1
                elif array[i] + array[j] + array[k] > 0:
                    k -= 1
                else:
                    result.append([array[i], array[j], array[k]])
                    j, k = j + 1, k - 1
                    while j < k and array[j] == array[j - 1]:
                        j += 1
                    while j < k and array[k] == array[k + 1]:
                        k -= 1
            i += 1
            while i < len(array) - 2 and array[i] == array[i - 1]:
                i += 1
        return result
obj=Calculation()
print('Output : ',obj.group_num(array))
