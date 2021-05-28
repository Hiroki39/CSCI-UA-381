def make_dice_function(number):
    funcname = 'dice' + str(number)

    def funcname():
        import random
        return(random.randint(1, 6))
    return funcname


function1 = make_dice_function(1)
function2 = make_dice_function(2)

for num in range(5):
    print(1, function1())
    print(2, function2())
