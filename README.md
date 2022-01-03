# Takeaway Assignment
[Installation](#installation)
[Running tests](#running)
[Test Results](#results)

<a name="installation"/></a>
## Tech Stack
[Python](python.org) - Interpreted high-level general-purpose programming language <br/>
[Behave](https://behave.readthedocs.io/en/stable/) - BDD(Behavior-driven development), Python style <br/>
[Selenium](https://www.selenium.dev/) - Suite of tools for automating web browsers <br/>
[Allure](https://github.com/allure-framework) - Test report tool <br/>

<a name="installation"/></a>
## Installation
Please, follow below list starting from #1 to end.
1. Install Chrome browser on your computer or server
2. Make sure Python 3 is installed, not python 2.
3. Open the repo in terminal/commandline.
4. Create virtual environment:
    ```bash
    virtualenv env 
    ```
5. Activate the environment(Make sure it is activated by seeing "(env)" at the beginning of new line).
    ```bash
    source env/bin/activate
    ```
6. Install required dependencies to run the test. 
    ```bash
    pip install -r requirements.txt
    ```

<a name="running"/></a>
## Running tests
Make sure the environment is activated and rund the script bellow.
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

