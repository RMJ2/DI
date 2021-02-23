# def numbersList (nums): 

#     sum = 0 
#     for num in nums∂: 
#         sum += num 
#     print(sum)

  

# names = ['harry', 'avi', 'james'] 

# def show_magicians(i):
#     for name in names:
#         print(name)

# magic = ['harry', 'avi', 'james'] 


# def make_great(i):
#     great = []
#     for name in names: 
#         great.append(f'the great {name}')
#     print(great)
    
# make_great(names)
# # show_magicians(magic)

def shoppingList(): 
    shopping = []
    while True: 
        new_item = input('enter your shopping list: (exit to quit)')
        if new_item == 'exit': break
        shopping.append(new_item)
    print(f'Your shopping list is: {shopping}')
    
shoppingList()