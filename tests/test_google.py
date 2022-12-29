import pytest

from pages.google_page import GooglePage
from tests.base_test import BaseTest


class TestGoogle(BaseTest):

    @pytest.fixture
    def google_page(self):
        self.page = GooglePage(self.webdriver)
        self.page.open()

    @pytest.mark.parametrize("search_term", ["cars", "dogs"])
    def test_google(self, google_page, search_term):
        self.page.normal_search(search_term)
        assert self.page.return_results_count() > 0
