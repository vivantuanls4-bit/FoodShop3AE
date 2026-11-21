from django.test import TestCase
from django.urls import reverse

from .models import User


class RegisterViewTests(TestCase):
    def test_invalid_registration_preserves_values_and_marks_invalid_field(self):
        User.objects.create_user(username='existing-user', password='ExistingPassword123!')

        response = self.client.post(
            reverse('accounts:register'),
            {
                'username': 'existing-user',
                'email': 'new@example.com',
                'fullName': 'Nguyen Van A',
                'phoneNumber': '0901234567',
                'address': '123 Example Street',
                'password1': 'ValidPassword123!Extra',
                'password2': 'ValidPassword123!Extra',
            },
        )

        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertEqual(form['email'].value(), 'new@example.com')
        self.assertEqual(form['fullName'].value(), 'Nguyen Van A')
        self.assertEqual(form['phoneNumber'].value(), '0901234567')
        self.assertEqual(form['address'].value(), '123 Example Street')
        self.assertIn('is-invalid', form['username'].field.widget.attrs['class'])
        self.assertNotIn('is-invalid', form['email'].field.widget.attrs['class'])
        self.assertContains(response, 'value="new@example.com"')
        self.assertContains(response, 'value="Nguyen Van A"')
        self.assertContains(response, 'value="0901234567"')
        self.assertContains(response, '123 Example Street</textarea>')
        self.assertContains(response, 'class="form-control is-invalid"')
        self.assertContains(response, 'type="password"')
        self.assertContains(response, 'aria-controls="id_password1"')
        self.assertContains(response, 'aria-controls="id_password2"')

    def test_login_page_has_password_visibility_toggle(self):
        response = self.client.get(reverse('accounts:login'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'data-password-toggle')
        self.assertContains(response, 'aria-controls="id_password"')
