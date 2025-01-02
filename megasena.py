import random

# INPUTS ------------------------------------------------------------------------------------------------
num_games = 6
megasena_numbers = set([1, 17, 19, 29, 50, 57])
megasena_award = 635000000
# END INPUTS ------------------------------------------------------------------------------------------------

bet_num = 0
bet_cost_by_game = {
    6: 5,
    7: 35,
    8: 140,
    9: 420,
    10: 1050,
    11: 2310,
    12: 4620,
    13: 8580,
    14: 15015,
    15: 25025,
    16: 40040,
    17: 61880,
    18: 92820,
    19: 135660,
    20: 193800,
}
while True:
    bet_num += 1
    bet = set()
    while True:
        bet.add(random.randint(1, 60))
        if len(bet) == num_games:
            break
    if megasena_numbers.issubset(set(bet)):
        total_cost = bet_num * bet_cost_by_game[num_games]
        award_after_taxes = megasena_award * 0.70
        profit = (award_after_taxes - total_cost)
        print(f"Parabéns! :)\nVoce ganhou a megasena na {bet_num:,} ª tentativa!\nVoce gastou um total de {total_cost:,.2f} reais!\nConsiderando o valor gasto com o premio ganho e tirando impostos voce ganhou {profit:,.2f} reais!")
        break
