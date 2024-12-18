import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up class for tests...")
        cls.fixture = None  # Пример инициализации общего ресурса для всех тестов

    @classmethod
    def tearDownClass(cls):
        print("Tearing down class after all tests...")
        if cls.fixture is not None:
            del cls.fixture  # Очистка общих ресурсов

    def test_first_test_case(self):
        print("Running first test case...")
        self.assertTrue(True)

    def test_second_test_case(self):
        print("Running second test case...")
        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
