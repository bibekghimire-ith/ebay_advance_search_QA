from playwright.sync_api import Page


class SearchResultsPage:
    
    # Initiating locators
    def __init__(self, page: Page):
        self.page = page
        self.search_items_list = self.page.locator("ul.srp-results.srp-list.clearfix")
        self.search_message = self.page.locator("h1.srp-controls__count-heading")
    
    def get_search_message(self) -> str:
        return self.search_message.text_content()
    
    def get_search_results(self) -> list:
        rows = self.search_items_list.locator("div.s-item__wrapper.clearfix").all()
        return rows
    
    def get_prices(self) -> list:
        price_list = self.search_items_list.locator("span.s-item__price").all_text_contents()
        new_list = []
        for price in price_list:
            if 'to' in price:
                parts = price.split(' to ')
                new_list.extend([float(part.replace('$', '')) for part in parts])
            else:
                new_list.append(float(price.replace('$', '')))
        return new_list
    
    def test(self):
        self.page.goto("https://www.ebay.com/sch/i.html?_nkw=iphone+16gb&_in_kw=3")
        # print(self.search_items_list)
        # print(self.search_message.text_content())
        
        rows = self.search_items_list.locator("div.s-item__wrapper.clearfix").all()
        print(len(rows))
        # print(rows)
        for row in rows:
            # print(row.text_content())
            # print("", end="\n")
            
            # if "iphone 16gb" not in row.text_content().lower():
            #     print(row.text_content())
            
            if not re.search(r'iphone.*16.*gb', row.text_content(), re.IGNORECASE):
                print(row.text_content())
        

# import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=True)
#     context = browser.new_context()
#     page = context.new_page()
    
#     sp = SearchResultsPage(page)
#     sp.test()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)