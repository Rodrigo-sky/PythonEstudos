arr = [2, 3, 6, 6, 5]
n = len(arr) #numero de pontuacoes

#trecho especifico para o hackerrank------
orei = []
for item in arr:
    orei.append(item)
#-----------------------------------------
def runnerScore(orei):
    
    orei.sort(reverse=True)
    for runner in orei:
        if(runner < orei[0]):
            return(runner)

print(runnerScore(orei))
