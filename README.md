# Takeaway Assignment
[Tech](#tech) |
[Installation](#installation) |
[Running tests](#running) | 
[Test Results](#results) 


<a name="tech"/></a>
## Tech Stack
[Python](python.org) - Interpreted high-level general-purpose programming language <br/>
[Gherkin](https://docs.behat.org/en/v2.5/guides/1.gherkin.html) - Business Readable, Domain Specific Language <br/>
[Behave](https://behave.readthedocs.io/en/stable/) - BDD(Behavior-driven development), Python style <br/>
[Selenium](https://www.selenium.dev/) - Suite of tools for automating web browsers <br/>
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
## Running tests
Make sure the environment is activated and run the script bellow.
#### Running Web tests in GUI browser mode
   ```bash
  behave -D headless=false --tags=web
   ```
#### Running Web tests in headless browser mode
   ```bash
  behave -D headless=true --tags=web
   ```

<a name="results"/></a>
## Test results
To see the result of the run. 
   ```bash
  allure serve reports/allure_results/
   ```

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
