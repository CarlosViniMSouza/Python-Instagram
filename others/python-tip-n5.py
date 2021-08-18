class random_things:

    def operators(v1, v2):
        v_sum = v1 + v2
        v_sub = v1 - v2
        print([v_sum, v_sub])

    def scanner():
        n1 = input("Write any word: ")
        n2 = input("Write a bollean value: ")
        print(f"{n1} and {n2} were writing!")

    #end of class.

var = random_things

var.operators(6, 2)

var.scanner()
