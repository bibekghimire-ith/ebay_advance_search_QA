# Project: Swagger Petstore
For API automation testing, I will use Postman for the following reasons:
1. Ease of Use: Postman has an intuitive user interface that simplifies the process of creating and managing API tests.
2. Extensive Features: It supports automated testing, creating test suites, scheduling runs, and integrates well with CI/CD pipelines.
3. Scripting Capabilities: Postman allows writing pre-request scripts and tests using JavaScript, providing flexibility in test scenarios.

Collection, environment, and test data files are included in this folder. These tests can be run using two methods:

### Method 1: Using Postman
Pre-requisite: Postman should be installed.        
**Steps:**    
1. Import the collection file and environment file in Postman
2. Collection file contains two folders which needs to be run separately.
3. First folder "End-to-end-Tests" includes tests for 4 different endpoints.
4. Run the folder by clicking on the "..." next to folder name.

5. Second folder "DDT_Tests" includes test for endpoint "Add a new pet to the store". This test is designed to run on the different sets of data from the csv file. Here, the test is run multiple times with different sets of data.
6. Click on the "..." next to folder name, then click "Run Folder". Then, under "Data" section, select the "test_data.csv" file and run it.

### Method 2: From command line
Pre-requisites: NodeJS and npm package manager should be installed
```
# Installing newman
npm install -g newman

# Installing html reporter
npm install -g newman-reporter-html

# Running End-to-end-Tests folder
newman run <collection_file> -e <environment_file> --folder End-to-end-Tests -r htmlextra --reporter-htmlextra-export ./ETE_htmlreport.html


# Running DDT_tests folder
newman run <collection_file> -e <environment_file> --folder DDT_tests -d test_data.csv -r htmlextra --reporter-htmlextra-export ./DDT_htmlreport.html
```

## Endpoints Included: 
**End-to-end-Tests folder:**
1. Add a new pet to the store
2. Update the pet details
3. Find pet by ID
4. Find pets by status

**EDDT_tests folder:**
1. Add a new pet to the store