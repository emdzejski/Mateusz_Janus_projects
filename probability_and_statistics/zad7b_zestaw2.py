from random import sample

trefl = list(range(1,14))
karty = sample(range(1,53), 3)

if True in [k in trefl for k in karty]:
    print('W wylosowanych kartach znajduje się trefl')
