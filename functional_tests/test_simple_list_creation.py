from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from functional_tests.base import FunctionalTest


class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_for_one_user(self) -> None:
        # Someone heard about a cool online to-do app. He goes to check out its homepage
        # self.browser.get("http://localhost:8000")
        self.browser.get(self.live_server_url)

        # He notices the page title and the header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", header_text)

        # He wants to enter a to-do item straight away.
        inputbox = self.browser.find_element_by_id("id_text")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # So he types "Buy eggs" into a text box.
        inputbox.send_keys("Buy eggs")

        # When he hits enter, the page updates, and now the page lists "1: Buy eggs" as an item in to-do list.
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy eggs')

        # There is still a text box inviting he to add another item to the to-do list. So he enters "Learn TDD".
        inputbox = self.browser.find_element_by_id("id_text")
        inputbox.send_keys('Learn TDD')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows two items on his list.
        self.wait_for_row_in_list_table('1: Buy eggs')
        self.wait_for_row_in_list_table('2: Learn TDD')

        # Satisfied, he goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # He notices that his list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Now a new user, Francis, comes along to the site.

        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page.  There is no sign of Edith's
        # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy eggs', page_text)
        self.assertNotIn('Learn TDD', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith...
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy eggs', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep
