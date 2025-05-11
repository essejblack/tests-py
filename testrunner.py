import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from unittest import TestSuite,TestLoader,TextTestRunner


def run():
    suite = TestSuite()
    loader = TestLoader()
    tests = loader.loadTestsFromName("tests.moduletestbookstore")
    suite.addTests(tests)
    runner = TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    run()