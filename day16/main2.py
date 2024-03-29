from itertools import chain, cycle


input_signal = '59750530221324194853012320069589312027523989854830232144164799228029162830477472078089790749906142587998642764059439173975199276254972017316624772614925079238407309384923979338502430726930592959991878698412537971672558832588540600963437409230550897544434635267172603132396722812334366528344715912756154006039512272491073906389218927420387151599044435060075148142946789007756800733869891008058075303490106699737554949348715600795187032293436328810969288892220127730287766004467730818489269295982526297430971411865028098708555709525646237713045259603175397623654950719275982134690893685598734136409536436003548128411943963263336042840301380655801969822' * 10_000
l = len(input_signal)
print(l)
pattern = [0, 1, 0, -1]
res = ''


def construct_pattern(i):
    repeaters = list(chain(*[i*[0], i*[1], i*[0], i*[-1]]))
    return chain(*[(i-1) * [0], i * [1], i * [0], i * [-1]], cycle(repeaters))

phases = 1

for phase in range(phases):
    l = len(input_signal)
    res = ''
    for i in range(l):
        multipliers = construct_pattern(i + 1)
        ans = 0
        for index, val in enumerate(input_signal):
            v = next(multipliers)
            #print(f'{val}*{v} + ', end='')
            ans += int(val) * v 
        ans = abs(ans) % 10
        res += str(ans)
        #print(f' = {ans}')
    
    print(f'After {phase + 1} phase: {res[640:650]}')
    input_signal = str(res)

offset = input_signal[0:7]
#print(f'Final answer = {input_signal[offfset]}')
print(offset)
