from random import sample
trefl = list(range(1,14))
i = 0
j = 0
p = 703/1700 #prawdopodobieństwo z zadania 7
while True:
    karty = sample(range(1,53), 3)
    if [k in trefl for k in karty] == [False, False, False]:
        j += 1
    i += 1
    
    if abs(j/i - p) < 10e-3 :
        break   
print(f'{i} --- tyle powtórzeń trzeba aby osiągnąć granice częstotliwości z zadania') 
    