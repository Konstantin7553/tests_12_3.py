import unittest

def check_is_frozen(func):
    def wrapper(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return func(self)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @check_is_frozen
    def test_run(self):
        pass

    @check_is_frozen
    def test_walk(self):
        pass

    @check_is_frozen
    def test_challenge(self):
        pass

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @check_is_frozen
    def test_first_tournament(self):
        pass

    @check_is_frozen
    def test_second_tournament(self):
        pass

    @check_is_frozen
    def test_third_tournament(self):
        pass






