from django.test import TestCase
from .models import Website

# Create your tests here.

class BasicTest(TestCase):
    def test_field(self):
        website = Website()
        website.first_service_detail = "table"
        website.second_service_detail = "chair"
        website.third_service_detail = "books"
        website.website_name = "Website name"
        website.round = 1
        website.has_won = "congratulations"
        website.save()

        record = Website.objects.get(pk=1)
        self.assertEqual(record,website)


