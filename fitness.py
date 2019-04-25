class Fitness:

    def __init__(self):
        self.__password = "password"
        self.__test_word = "test_word"

    def fitness(self, password, test_word):
        if (len(test_word) != len(password)):
            print("Taille Incompatible")
            return
        else:
            score = 0
            i = 0
            while (i < len(password)):
                if (password[i] == test_word[i]):
                    score += 1
                i += 1
        return score * 100 / len(password)
