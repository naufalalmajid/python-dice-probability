import random

class Dadu(object):
    def __init__(self):
        self._mata_dadu_ = 0

    def get_mata_dadu(self):
        self._mata_dadu_ = random.randint(1, 6)
        return self._mata_dadu_


if __name__ == "__main__":
    number_of_roll = 5
    # ayo lempar dadu
    dadu = Dadu()
    list_mata_dadu = []
    for i in range(number_of_roll):
        list_mata_dadu.append(str(dadu.get_mata_dadu()))
    
    output = ", ".join(list_mata_dadu)
    print("output: ", output)
