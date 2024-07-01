import pytest
import re
from playwright.sync_api import expect, Page

from pageObjects.homepage import Homepage
from pageObjects.advanceSearch import AdvancedSearchPage
from pageObjects.searchResults import SearchResultsPage

class TestAdvanceSearch:
    base_url = "https://www.ebay.com"
    
    def test_keyword_search(self, page: Page) -> None:
        """
            Tests the keywords based filtering in the advanced search.
        """
        page.goto(self.base_url)
        hp = Homepage(page)
        search_page = AdvancedSearchPage(page)
        results_page = SearchResultsPage(page)

        hp.navigate_advance_search()
        
        assert search_page.is_AdvancedSearchPage()
        
        # Perform search operation
        exclude_words = ["iphone", "blackberry", "samsung"]
        search_page.fill_keywords("smartphone 64gb")
        search_page.set_keyword_option("Exact words, exact order")
        search_page.set_exclude_words(exclude_words)
        search_page.click_search()
        
        # Validate search results
        search_msg = results_page.get_search_message()
        result_count = int(search_msg.split(" ")[0])
        if result_count:
            rows = results_page.get_search_results()
            for row in rows:
                # Validate exclude words are not present in the search results
                for item in exclude_words:
                    assert item not in row.text_content().lower()
                # Check if the "Exact words, exact order" keyboard option is valid
                if not re.search(r'smartphone.*64.*gb', row.text_content(), re.IGNORECASE):
                    assert False

    
    def test_price_based_filtering(self, page: Page) -> None:
        """
            Tests the price based filtering in the advanced search.
        """
        page.goto(self.base_url)
        hp = Homepage(page)
        search_page = AdvancedSearchPage(page)
        results_page = SearchResultsPage(page)

        hp.navigate_advance_search()
        
        assert search_page.is_AdvancedSearchPage()
        
        # Perform search operation
        min_price = 300
        max_price = 1000
        search_page.fill_keywords("smartphone 64gb")
        search_page.set_keyword_option("Exact words, exact order")
        search_page.set_min_max_price(min_price, max_price)
        search_page.click_search()
        
        # Validate search results
        search_msg = results_page.get_search_message()
        result_count = int(search_msg.split(" ")[0])
        if result_count:
            rows = results_page.get_prices()
            # Check if the prices are within the set price filter range
            assert min(rows) >= min_price
            assert max(rows) <= max_price