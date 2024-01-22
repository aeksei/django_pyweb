from rest_framework.test import APITestCase
from rest_framework import status

from books.models import Category


class TestCategoryViewSet(APITestCase):
    # /categories/
    def test_list_categories(self):
        """Тестирую список категорий."""
        # Подготовка данных
        list_categories = [
            Category(name=f"Тестовая_категория_{i}", slug=f"test_slug_{i}") for i in range(10)
        ]
        Category.objects.bulk_create(list_categories)  # массовую вставку

        # Действие
        url = "/api/categories/"
        resp = self.client.get(url)

        # Ожидаемые результаты
        actual_result = resp.status_code
        expected_result = status.HTTP_200_OK
        self.assertEquals(
            actual_result, expected_result,  # actual_result == expected_result
            msg="Ошибка ожидаемого статуса"
        )

        data = resp.json()

        self.assertIsInstance(data, list, msg="Ожидается список")

        expected_count = len(list_categories)
        actual_count = len(data)

        self.assertEquals(
            actual_count, expected_count,
            msg="Количество категорий не совпадает"
        )

    def test_create_categories(self):
        """Тестирую список категорий."""
        ...

    # /categories/<int:pk>
    def test_retrieve_category(self):
        ...

    def test_update_category(self):
        ...

    def test_destroy(self):
        ...