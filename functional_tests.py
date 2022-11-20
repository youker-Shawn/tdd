from selenium import webdriver

import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
    
    def tearDown(self) -> None:
        # Satisfied, he closes the browser.
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self) -> None:
        # Someone heard about a cool online to-do app. He goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # He notices the page title and the header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        # He wants to enter a to-do item straight away.

        # So he types "Buy eggs" into a text box.

        # When he hits enter, the page updates, and now the page lists "1: Buy eggs" as an item in to-do list.

        # There is still a text box inviting he to add another item to the to-do list. So he enters "Learn TDD".

        # The page updates again, and now shows two items on his list.

        # The site has generated a uniqe URL for him.

        # He visites the URL and his to-do list is still there.


if __name__ == '__main__':
    unittest.main()

