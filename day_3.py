
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""



# def order(sentence):
#   final_sentence = []


#   for i in range(1,10):
#       for y in sentence.split():
#           if str(i) in y:
#               final_sentence.append(y)
              
#   return ' '.join(final_sentence)
      
   

# print(order("is2 Thi1s T4est 3a"))    

# def order(words):
#   return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"

# def spin_words(sentence):
#     final_word = []    
    
#     def reverse_word(word):
#         last_word = []
#         for i in word:
#             last_word.append(i)
#         last_word.reverse()
#         return " ".join(last_word).replace(" ", "")

    
        
#     for i in sentence.split():
#         if len(i) > 5:
#             final_word.append(reverse_word(i))
#         else:
#             final_word.append(i)
#     return " ".join(final_word)
    
    
# print(spin_words("Hey fellow warriors"))



# def to_weird_case(words):
#     all_word = words.split()

    
#     def uper_case(word):
#         final_word = []

#         for i in range(0, len(word)):
#             if i % 2 ==0:
#                 final_word.append(word[i].upper())
#             else:
#                 final_word.append(word[i].lower())

#         return " ".join(final_word).replace(" ", "")

    

#     return " ".join([uper_case(i) for i in all_word])


        


# def narcissistic( value ):

#     total = 0
#     for i in str(value):
#         total += pow(int(i), len(str(value)))
#     if total == value:
#         return True
#     else:
#         return False

# print(narcissistic(1652))

# def narcissistic(value):
#     return value == sum(int(x) ** len(str(value)) for x in str(value))




def move_zeros(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)            
            lst.append(i)            
    
    return lst    
    

    
print(move_zeros([1, 0, 1, 2, 0, 1, 3]))