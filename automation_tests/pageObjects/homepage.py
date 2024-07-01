from playwright.sync_api import Page


class Homepage:
    
    base_url = "https://www.ebay.com"
    
    # Initiating locators
    def __init__(self, page: Page):
        self.page = page
        self.advance_search_link = self.page.get_by_role("link", name="Advanced Search")
        # page.get_by_label("Advanced Search").click()


    def is_homepage(self):
        title_text = "Electronics, Cars, Fashion, Collectibles & More | eBay"
        return self.page.title() == title_text
    
    
    def navigate_advance_search(self) -> None:
        """This function navigates page to Advanced Search page
        """
        self.advance_search_link.click()
        self.page.wait_for_load_state()