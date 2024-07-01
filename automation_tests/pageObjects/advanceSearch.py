from playwright.sync_api import Page

class AdvancedSearchPage:
    
    # Initiating locators
    def __init__(self, page: Page) -> None:
        self.page = page
        self.heading = self.page.get_by_role("header").filter(has_text="Advanced Search")


    def is_AdvancedSearchPage(self) -> bool:
        title_text = "Advanced Search | eBay"
        return self.page.title() == title_text
    
    def fill_keywords(self, keyword: str) -> None:
        self.page.get_by_label("Enter keywords or item number").fill(keyword)
    
    def set_keyword_option(self, k_option: str) -> None:
        # page.get_by_test_id("s0-1-17-4[0]-7[1]-_in_kw")
        self.page.get_by_label("Keyword options").select_option(k_option)
        # self.page.get_by_label("Keyword options").select_option(label=k_option)
        # value as 1, 2, 3
        
    def set_exclude_words(self, exclude_words: list) -> None:
        words = " ".join(exclude_words)
        self.page.get_by_test_id("_ex_kw").fill(words)
        
    def set_category(self, category: str) -> None:
        self.page.get_by_test_id("s0-1-17-4[0]-7[3]-_sacat").select_option(label=category)
        
    def click_search(self) -> None:
        self.page.locator("fieldset").filter(has_text="Enter keywords or item").get_by_role("button").click()
        
    def set_min_max_price(self, min_price: str, max_price: str) -> None:
        if min_price:
            self.page.get_by_label("Enter minimum price range").fill(str(min_price))
        if max_price:
            self.page.get_by_label("Enter maximum price range").fill(str(max_price))