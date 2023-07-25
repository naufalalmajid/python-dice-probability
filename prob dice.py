from random import randint

class Dadu(object):
    def __init__(self):
        self._mata_dadu_ = 0

    def get_mata_dadu(self):
        self._mata_dadu_ = randint(1, 6)
        return self._mata_dadu_

if __name__ == "__main__":
    number_of_roll = 2  # banyak dadu
    dadu = Dadu()
    list_icounter = []
    number_of_trials = 10  # banyak percobaan
    for i in range(number_of_trials):
        icounter = 0
        list_mata_dadu = []
        for i in range(number_of_roll):
            mata_dadu = dadu.get_mata_dadu()
            list_mata_dadu.append(mata_dadu)
            print(mata_dadu, end=" ")
            if list_mata_dadu[i] == 1:
                icounter += 1
        if icounter >= 1:
            list_icounter.append(1)
        else:
            list_icounter.append(0)
        print()  
    print("Kemungkinan angka 1:", list_icounter.count(1) / number_of_trials)
