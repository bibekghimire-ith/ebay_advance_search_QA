# Automation Tests for the Ebay Advanced Search feature
**Automation Framework:** pytest-playwright 
Playwright has been buzzword recently in test automation community. Cross-browser compatibility, multiple language support, automatic waiting, powerful debugging tools (trace viewer, playwright inspector, codegen), and ease to use has made playwright popular among SDET Engineers. Likewise, it is faster compared to Selenium and Cypress.

## Scenarios:
Two commonly/primarily used scenarios are automated in this tests.
### A. Keywords based search:
This scenario ensures that the search functionality accurately retrieves items based on user-specified keywords, which is fundamental to user experience and search accuracy.
**Steps:**
1. Go to Homepage
2. Click on "Advanced Search" link next to the "Search" button.
3. After navigating to the Advanced Search Page, fill the keywords, and other parameters:
    i. keywords = "smartphone 64gb"
    ii. keywords option (dropdown) = "Exact words, exact order"
    iii. exclude words = ["iphone", "blackberry", "samsung"]
4. Click on Search button
5. After navigating to the results page, validate results

**Validation Steps:**
1. Check if the search results are obtained from the search message at top
2. Obtain all the items from the results page
3. Check if the keyword "smartphone 64gb" is present in each of the items
4. Check and verify exclude words are not present in any of the items


### B. Price-based filtering
This scenario tests the system's ability to filter search results within a specified price range, which is crucial for users to find products within their budget effectively.
**Steps:**
1. Go to Homepage
2. Click on "Advanced Search" link next to the "Search" button.
3. After navigating to the Advanced Search Page, fill the keywords, and other parameters:
    i. keywords = "smartphone 64gb"
    ii. keywords option (dropdown) = "Exact words, exact order"
    iii. min_price = 300 and max_price = 1000
4. Click on Search button
5. After navigating to the results page, validate results

**Validation Steps:**
1. Check if the search results are obtained from the search message at top
2. Obtain all the items prices from the results page
3. Check if the prices are within the range of (min_price and max_price)


## Environment Setup
-> Python3 should be installed
```
# Configuration of playwright
pip3 install playwright
pip3 install pytest-palywright
playwright install

pip3 install pytest
pip3 install pytest-html    
pip3 install pytest-xdist   
```
**Alternatively:**
```
pip3 install -r requirements.txt
playwright install
```

## Test Execution
```
pytest
```

## Test Deliverables
HTML report in folder "Reports"

## Notes: 
1. 1st scenario is failing scenario
2. Tests can be parameterized to address data-driven test implementation