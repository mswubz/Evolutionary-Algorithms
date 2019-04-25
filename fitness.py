
class Fitness(object):

    def __init__(self, password, test_word):
        self.__password = password
        self.__test_word = test_word

    @property
    def password(self):
        return self.__password

    @property
    def test_word(self):
        return self.__test_word

    def score (password, test_word):
        ''' Calculates the fitness score (number of characters correct / total number of characters) '''
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
