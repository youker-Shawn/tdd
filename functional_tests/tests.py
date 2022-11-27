from django.test import LiveServerTestCase
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
    
    def tearDown(self) -> None:
        # Satisfied, he closes the browser.
        self.browser.quit()
    
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self) -> None:
        # Someone heard about a cool online to-do app. He goes to check out its homepage
        # self.browser.get("http://localhost:8000")
        self.browser.get(self.live_server_url)

        # He notices the page title and the header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", header_text)

        # He wants to enter a to-do item straight away.
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a to-do item"
        )

        # So he types "Buy eggs" into a text box.
        inputbox.send_keys("Buy eggs")

        # When he hits enter, the page updates, and now the page lists "1: Buy eggs" as an item in to-do list.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)
        self.check_for_row_in_list_table('1: Buy eggs')

        # There is still a text box inviting he to add another item to the to-do list. So he enters "Learn TDD".
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys('Learn TDD')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy eggs')
        self.check_for_row_in_list_table('2: Learn TDD')

        self.fail('Finish the test!')
        # The page updates again, and now shows two items on his list.

        # The site has generated a uniqe URL for him.

        # He visites the URL and his to-do list is still there.
