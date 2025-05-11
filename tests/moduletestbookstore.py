import unittest
from bookstore import BookStore
import sys

class BookStoreTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Setting up BookStoreTestCase...")
        cls.store = BookStore([
            "C++ develop",
            "Devops",
            "Java Full Guide for Pros",
            "Java for dumms",
            "Android dev",
            "Active for admins"
        ])

    def setUp(self):
        self.secondStore = BookStore([
            "C++ develop",
            "Devops",
            "Java Full Guide for Pros",
            "Java for dumms",
            "Android dev",
            "Active for admins"
        ])

    def test_find_book_no_sense(self):
        found = self.store.find_book("dEv", False)
        expected = ["Android dev", "C++ develop", "Devops"]
        self.assertEqual(expected, found)

    def test_find_book_sense(self):
        found = self.store.find_book("Dev", True)
        expected = ["Devops"]
        self.assertEqual(expected, found)

    def test_find_book_after_buy(self):
        self.secondStore.buy("Devops")
        all = self.secondStore.find_book("")
        self.assertNotIn("Devops", all)

    @unittest.skip("skipping")
    def test_should_be_skipped(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(not sys.platform.startswith("linux"), "requires Linux")
    def test_linux_support(self):
        pass

    @unittest.skipIf(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        pass

    def test_python_minor_version(self):
        version = int("{}{}".format(sys.version_info.major, sys.version_info.minor))
        if version < 312:
            self.skipTest("requires Python 3.12 or higher")


if __name__ == "__main__":
    unittest.main()