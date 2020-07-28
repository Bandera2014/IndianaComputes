'''
#challenge 1
def bake_cookie(dough,filling,cookieName):
    return "A "+cookieName+" made with "+dough+" dough and "+filling 

#challenge 2
def bake_cookie(dough,filling,cookieName):
    return "A {} made with {} dough and {}".format(cookieName,dough,filling)

#challenge 3 step 3
def bake_cookie(dough,filling,cookieName,quantity):
    return "{} count: {} made with {} dough and {}".format(quantity,cookieName,dough,filling)
'''

#challenge3
def bake_cookie(dough,filling,cookieName,quantity,cost):
    totalCost = cost*int(quantity)
    return "{} count for ${:4.2f}: {} made with {} dough and {}".format(quantity,totalCost,cookieName,dough,filling)

user_selection = input("Please either enter 'cookie' to enter a cookie or 'q' to stop the program:")
bake_sale_flyer = "\n!!BAKE SALE !!\n"
while user_selection != 'q':
    
    dough = input("What dough are you using? ")
    filling = input("What topping or filling will you use? ")+"\n"
    cookieName = input("And what is this cookie called? ")
    quantity = input("And how many are you baking? ")
    cost = float(input("How much does a single cookie cost? "))

    bake_sale_flyer+=bake_cookie(dough,filling,cookieName,quantity,cost)
    user_selection = input("Please either enter 'cookie' to enter a cookie or 'q' to stop the program:")
print(bake_sale_flyer)



