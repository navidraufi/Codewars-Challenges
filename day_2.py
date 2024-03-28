# def tower_builder(n_floors):
#     pyramid = [
        
#     ]
#     current_floor = 1
#     while 0 < n_floors:
#         floor = (n_floors - 1) * " " + current_floor * "*" + (n_floors - 1) * " " 
#         pyramid.append(floor)
#         n_floors-=1
#         current_floor += 2
#     return pyramid        


# print(tower_builder(4))

# def tower_builder(n):
#     return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]


def diamond(n):
    my_diamond = ""
    while n > 0:
        my_diamond += round(n/2, None)
        n -= 1  
    
    return my_diamond

print(diamond(5))