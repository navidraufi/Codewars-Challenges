# inputValue = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]


# def is_senor():
#     listOfOpen = []
    
#     for i in inputValue:
#         if i[0] >= 55 and i[1] > 7:
#             listOfOpen.append("Senior")
#         else:
#             listOfOpen.append("Open")
    
#     return listOfOpen

# print(is_senor())

# #return ['Senior' if x[0] > 54 and x[1] > 7 else 'Open' for x in data]

# def series(n):
#     num = 1
#     final_value = 0
    
#     for i in range(0, int(n)):
#         final_value += 1/num
#         num +=3
    
#     return format(round(final_value, 2), '.2f')

# print(series(1.0))
    
    
# def series_sum(n):
#     return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

# def nxt_square(sq):
    
#     square_num = int(pow(sq, 1/2))
#     is_square = False
    
#     i = 0
#     while i < sq:
#         if pow(i, 2) == sq:
#             is_square = True
#             break
#         else: 
#             is_square = False
#         i+=1

#     if is_square:
#         square_num+=1
#         return pow(square_num, 2)
#     else: 
#         return -1
    

# print(nxt_square())



# def remove_smallest(numbers):
#     my_list = numbers

#     final_list = []
    
#     smallest_num = min(my_list)

#     for i in my_list:
#         if i == smallest_num:
#             pass
#         else:
#             final_list.append()


# print(remove_smallest([10,2,4,5,10]))
    
    
# def sort_array(source_array):
#     final_array = []

#     for i in source_array:
#         if i%2 == 0:
        
#         else:
#             final_array.append(i)
            

# my_list = [3,1,5,9,2,5]


# def sort_array(source_array):
#     new_array = source_array.sort()
    
    
    
#     for i in new_array:
#         if i % 2 == 0:
#             new_array =  new_array.insert(source_array.index(i), i)
        
#     return new_array
    
# print(sort_array(my_list))
    
    
# def high(x):
    
#     score = 0
#     word = ""
    
    
#     string_of_word = x.split()

#     def get_score(word):
#         word_score = 0        
#         for i in word:
#             char = ord(i)-96
#             word_score +=char
    
#         return word_score
    
    
#     for each_word in string_of_word:
#         if get_score(each_word) > score:
#             score = get_score(each_word)
#             word = each_word
    

    
#     return word

# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

# sentence = "The quick brown fox jumps over the lazy dog"

# def is_pangram(s):
    
#     is_pangram_yet = False
    
#     "".lower()
    
#     all_letters = []
#     for i in range(97, 97+26):
#         all_letters.append(chr(i))
    
#     for each_letter in all_letters:
#         if s.find(each_letter) != -1:
#             is_pangram_yet = True
#         else:
#             is_pangram_yet = False
#             break
        
#     return is_pangram_yet

# print(is_pangram(sentence))
    
    
# import string

# def is_pangram(s):
#     s = s.lower()
#     for char in 'abcdefghijklmnopqrstuvwxyz':
#         if char not in s:
#             return False
#     return True


# def find_it(seq):    
#     for i in range(min(seq),max(seq) + 1):
#         if seq.count(i) % 2 !=0:
#             return i
        

    
    
# print(find_it([1,2,4,1,2,2]))



# def sum_dig_pow(a, b):
    
#     final_array = []
    
#     def divide_num(num):
#         total_num_pow = 0
#         value_power = 1 
#         for i in str(num):
#             total_num_pow += pow(int(i), value_power)
#             value_power += 1
#         return total_num_pow

#     for i in range(a, b+1):
#         if i == divide_num(i):
#             final_array.append(i)

#     return final_array



# print(sum_dig_pow(1, 100))

# def dig_pow(n):
#     return sum(int(x)**y for y,x in enumerate(str(n), 1))

# def sum_dig_pow(a, b): 
#     return [x for x in range(a,b + 1) if x == dig_pow(x)]