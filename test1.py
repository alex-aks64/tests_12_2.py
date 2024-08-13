import unittest
import runner_and_tournament as Runner

class TournamentTest(unittest.TestCase):
    usain: Runner.Runner
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            for k, v in v.items():
                print(f'{k}:{v}')
    def setUp(self):
        self.usain = Runner.Runner("Усэйн", 10)
        self.andrey = Runner.Runner("Андрей", 9)
        self.nick = Runner.Runner("Ник", 3)

    def test_tournament_results_usain_nick(self):
        print('id:',+self.id())
        tournament = Runner.Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.assertEqual(results[1], self.usain)
        TournamentTest.all_results['Усэйн vs Ник'] = results[1].name

    def test_tournament_results_andrey_nick(self):
        tournament = Runner.Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.assertEqual(results[1], self.andrey)
        TournamentTest.all_results["Андрей vs Ник"] = results[1].name

    def test_tournament_results_usain_andrey_nick(self):
        tournament = Runner.Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.assertEqual(results[1], self.usain)
        TournamentTest.all_results["Усэйн vs Андрей vs Ник"] = results[1].name

if __name__ == '__main__':
    unittest.main()