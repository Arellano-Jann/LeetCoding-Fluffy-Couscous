# https://app.codesignal.com/interview-practice/question/rMe9ypPJkXgk3MHhZ/description
# https://stackoverflow.com/questions/48783747/number-of-distinct-sums-from-non-empty-groupings-of-possibly-very-large-lists
def possibleSums(coins, quantity):
    purse = {}
    for coin, quant in zip(coins, quantity):
        purse[coin] = quant + purse.get(coin, 0) # creates a dictionary of the coins that we have. deals with double coins
    dp = set()
    for coin, quant in purse.items():
        to_add = set() # we have this here because i'm not sure if for val in dp changes if we're dynamically adding to the set. so this acts as a temp variable
        for i in range(1, quant+1): 
            to_add.add(coin * i) # brute forces the total value of what the coin has just by itself (with it's own quantity)
            for val in dp:
                to_add.add(coin * i + val) # adds the possible values that the coin can have by itself with previous values that we've calculated thereby essentially bruteforcing the values
        dp |= to_add # this ORS the two sets together which effectively adds them together
        # print(dp) # this was used for debugging
    return len(dp)
        
        
    

