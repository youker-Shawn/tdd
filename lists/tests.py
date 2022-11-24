from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Item


# Create your tests here.

class HomePageTest(TestCase):
    def test_use_home_template(self):
        # found = resolve("/")
        # self.assertEqual(found.func, home_page)
        response = self.client.get("/")  # 隐式地测试如上URL映射view函数的过程

        # 不要去测试常量内容，比如一堆字符串内容是否正确，而是测实现逻辑。
        # Django中测试使用了正确html模板的方式如下
        # 而不是去：进行复杂地decode，去除换行空白制服等，最后比较字符串相等。
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_a_POST_request(self):
        item_text = 'A new list item'
        response = self.client.post('/', data={'item_text': item_text})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.last()
        self.assertEqual(new_item.text, item_text)

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')
    
    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)
    
    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/')

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')

