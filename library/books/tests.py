from django.test import TestCase
from django.urls import reverse
from .models import Book
# Create your tests here.

class BookTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="An excellent subtitle",
            author="Tom Christie",
            isbn="1234567890123",
        )

        # cls.book = Book(
        #     title="A good title",
        #     subtitle="An excellent subtitle",
        #     author="Tom Christie",
        #     isbn="1234567890123",
        # )
        # cls.book.save()

    def test_book_content(self):
        assert self.book.title == "A good title"
        assert self.book.subtitle == "An excellent subtitle"
        assert self.book.isbn == "1234567890123"                
        # self.assertEqual(self.book.title, "A good title")

    def test_book_listviwe(self):
        response = self.client.get(reverse("home"))
        assert response.status_code == 200
        self.assertContains(response, "excellent subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")