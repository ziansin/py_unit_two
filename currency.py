money_input = input("How many dollars:")
money = float(money_input)
remainder_hunid = (money % 100) / 100
if money > 0:
    hunid = (money / 100) - remainder_hunid
    hunid = round(hunid)
    print("Hundred dollar bills:", hunid)
    money = money - (hunid * 100)
remainder_fity = (money % 50) / 50
if remainder_hunid > 0:
    fity = (money/50) - remainder_fity
    fity = round(fity)
    print("Fifty dollar bills:", fity)
    money = money - (fity * 50)
remainder_tweny = (money % 20) / 20
if remainder_tweny > 0:
    tweny = (money/20) - remainder_tweny
    tweny = round(tweny)
    print("Twenty dollar bills:", tweny)
    money = money - (tweny * 20)
remainder_tenn = (money % 10) / 10
if remainder_tenn > 0:
    tenn = (money/10) - remainder_tenn
    tenn = round(tenn)
    print("Ten dollar bills:", tenn)
    money = money - (tenn * 10)
remainder_fiv = (money % 5) / 5
if remainder_fiv > 0:
    fiv = (money/5) - remainder_fiv
    fiv = round(fiv)
    print("Five dollar bills:", fiv)
    money = money - (fiv * 5)
remainder_on = money
if remainder_on > 0:
    on = money
    on = round(on)
    print("One dollar bills:", on)
    money = money - on
