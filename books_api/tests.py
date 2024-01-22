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
        # Действие
        url = "/api/categories/"

        data = {
            "name": "Тестовая категория",
            "slug": "test_slug",
        }
        resp = self.client.post(url, data=data)

        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Category.objects.filter(id=resp.json()["id"]).exists())


class TestRetriveUpdateDelete(APITestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(**{
            "name": "Тестовая категория",
            "slug": "test_slug",
        })

    # /categories/<int:pk>
    def test_retrieve_category(self):
        url = f"/api/categories/{self.category.id}/"
        resp = self.client.get(url)

        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertIsInstance(resp.json(), dict, msg="Ожидается словарь")

    def test_update_category(self):
        update_data = {
            "name": "Новое название",
            "slug": "new_slug",
        }
        url = f"/api/categories/{self.category.id}/"
        resp = self.client.put(url, data=update_data)

        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertIsInstance(resp.json(), dict, msg="Ожидается словарь")

        excected_result = {
            "id": self.category.id,
            "name": "Новое название",
            "slug": "new_slug",
        }
        self.assertEquals(resp.json(), excected_result)

    def test_destroy(self):
        url = f"/api/categories/{self.category.id}/"
        resp = self.client.delete(url)

        self.assertEquals(resp.status_code, status.HTTP_204_NO_CONTENT)

    def test_object_not_exists(self):
        does_not_exists_id = 99999999999999
        url = f"/api/categories/{does_not_exists_id}/"
        resp = self.client.get(url)

        self.assertEquals(resp.status_code, status.HTTP_404_NOT_FOUND)
