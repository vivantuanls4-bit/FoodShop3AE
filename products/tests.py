from django.test import TestCase

from .models import Category, Snack


class SnackIngredientsTests(TestCase):
    def test_ingredients_are_saved_and_optional(self):
        category = Category.objects.create(name='Đồ ăn vặt')
        snack = Snack.objects.create(
            category=category,
            snackName='Bánh thử nghiệm',
            price='10000.00',
            ingredients='Bột mì, đường',
        )

        snack.refresh_from_db()
        self.assertEqual(snack.ingredients, 'Bột mì, đường')

        snack_without_ingredients = Snack.objects.create(
            category=category,
            snackName='Sản phẩm chưa rõ thành phần',
            price='12000.00',
        )
        self.assertIsNone(snack_without_ingredients.ingredients)
