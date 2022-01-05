# Takeaway Assignment
[Tech](#tech) |
[Installation](#installation) |
[Running Tests](#running) | 
[Pipeline Run](#pipeline)  |
[API Test](#api) | 
[Load Test](#load) |
[Test Results](#results) | 
[Troubleshooting](#troubleshooting) 



<a name="tech"/></a>
## Tech Stack
[Python](python.org) - Interpreted high-level general-purpose programming language <br/>
[Gherkin](https://docs.behat.org/en/v2.5/guides/1.gherkin.html) - Business Readable, Domain Specific Language <br/>
[Behave](https://behave.readthedocs.io/en/stable/) - BDD(Behavior-driven development), Python style <br/>
[Selenium](https://www.selenium.dev/) - Suite of tools for automating web browsers <br/>
[Locust](https://docs.locust.io/en/stable/index.html) - Scriptable and scalable performance testing tool <br/>
[Allure](https://github.com/allure-framework) - Test report tool <br/>

<a name="installation"/></a>
## Installation
Please, follow below list starting from #1 to end. <br/>
All scripts are written to run on linux or unix based OS. If your are using Windows OS, please convert them to work
on Windows OS.

1. Install Chrome browser on your computer or server. [Download & Install Chrome](https://support.google.com/chrome/answer/95346?hl=en&co=GENIE.Platform%3DDesktop)
2. Make sure Python 3.x is installed, not python 2. [Upgrade Python](https://phoenixnap.com/kb/upgrade-python)
3. Open the repo in terminal/commandline.
4. Install virtual environment:
    ```bash
    pip install virtualenv 
    ```
5. Create virtual environment:
    ```bash
    virtualenv env 
    ```
6. Activate the environment(Make sure it is activated by seeing "(env)" at the beginning of new line).
    ```bash
    source env/bin/activate
    ```
7. Install required dependencies to run the test. 
    ```bash
    pip install -r requirements.txt
    ```

<a name="running"/></a>
## Running Tests
Make sure the environment is activated and run the script bellow.
#### Running Web tests in GUI browser mode
   ```bash
  behave -D headless=false --tags=web
   ```
#### Running Web tests in headless browser mode
   ```bash
  behave -D headless=true --tags=web
   ```

<a name="api"/></a>
#### Running API tests
".env" file must be added and configured(if necessary)to the project under home directory. 
".env_sample" file can be copied and renamed to ".env".
   ```bash
  behave -D --tags=api
   ```
<a name="load"/></a>
#### Running Sample Load tests in normal mode
Run the 
   ```bash
  locust -f load_tests/posts.py 
   ```
#### Running Sample Load tests in headless mode
   ```bash
  locust -f load_tests/posts.py --headless
   ```
#### Running Sample Load tests with user number specified
This run can be with or without headless mode. User numbers can be change as needed more or less users.
```bash
  locust -f load_tests/posts.py --users 50
   ```

<a name="pipeline"/></a>
## Pipeline Run
To run the test on a server or pipeline step, run below 2 lines or add them pipeline step file.
Important! Scripts are to work with linux bases server. 
#### Running Web tests
   ```bash
    chmod +x ./run_scripts/web_run.sh 
    ./run_scripts/web_run.sh
   ```
#### Running API tests
Environment variables under .env_sample file and values must be added to Pipeline
   ```bash
    chmod +x ./run_scripts/api_run.sh 
    ./run_scripts/api_run.sh
   ```

<a name="results"/></a>
## Test Results
To see the result of the run. 
   ```bash
  allure serve reports/allure_results/
   ```

<a name="troubleshooting"/></a>
## Troubleshooting
* If virtualenv is not working in any case, please follow below steps after step 2 in the [Installation](#installation).
  * Install pipenv. 
      ```bash
    pip install pipenv 
    ```
  * Install required dependencies. 
    ```bash
    pipenv install -r requirements.txt
    ```
  * To run and see the result add ```pipenv run``` before all the shell scripts. For example ```pipenv run behave -D headless=true --tags=web```
* If requirements file cannot be reachable, make sure you are in the repo's directory. 
* In case allure server is not started, install allure on your computer or server. [Install Allure](https://github.com/allure-framework/allure2#download)
