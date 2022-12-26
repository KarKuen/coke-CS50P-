def main():
    remainder = 50
    while remainder > 0:
        coin = int(input('Insert coin: '))
        if coin == 30:
            coin = 0
        remainder = cents(coin, remainder)
        if remainder > 0:
            print('Amount due:', remainder)
    print('Change owed:', -1 * remainder)



def cents(coin, remainder):
    remainder = remainder - coin
    return(remainder)

main()