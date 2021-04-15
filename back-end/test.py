dic = {'person-01': ['157×274', 0.883], 'dog-02': ['144×234', 0.78], 'dog-03': ['130×199', 0.75], 'cow-04': ['204×260', 0.482], 'cow-05': ['225×386', 0.462]}
for key,value in dic.items():
    # print(key,value)
    print(key+" 的概率:"+ str(round(value[1] * 100 , 4)) + "%")