# ISM3232 Midterm: Cloudstep Software

- **Name:** Rahim Rozani
- **Version** Python 3.14.0
- **Date** 10/25/26

## What this program does:

This program takes customer data for Cloudstep Software and provides reports that can provide actionable decisions and insights. The program is able to generate an organized report that shows the customers name, total price, contract reviews, trainers needed, total orders, total sales, and average sales. The program is able to generate reports for these in order to help the owner and business generate insights.  

## Business Rules:

1. taking the companies seat number and multiplying it by the seat per cost to get the total license cost.
2. Based on the companies seat and whether they are an education customer, determine which level of discount they are able to fit in. 
3. Specifying a condition that only education customers with 50 seats or more get a 16% discount, othere more than 50 remain with a 7% discount.
4. A special condition that only customers with a final license cost of $400 or less get an onboarding fee of $60.
5. A customer with a total license cost exceeding $5,000 needs a contract review.
6. A customer that has purchased 25 seats or more or exceeds a license total of $3,000 gets a dedicated trainer.


## How to run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

```text
python3 -m venv .venv, creates the virtual environment for the program to be set up.

source .venv/bin/activate, activates the virtual environment in python.

python -m pip install -r requirements.txt, installs the python packages used to run the program. 

python main.py, starts and executes the program with data to generate business reports.
```

## How to test:

```bash
python -m ruff check .
python -m pytest tests/ -v
```

Ruff checks the python code for linting issues, and pytest runs the test functions.
In total there are 24 test functions defined in the test file.

## Files in this repository:

1. business_rules.py: contains the 8 functions defined for the business logic
2. main.py: contains the imported business rules functions along with executable code that generates the business report.
3. commands.md: contains the terminal records, showing what commands were typed in order to create the program. 
4. READ.ME: contains instructions on how to install and run the program.
5. requirements.txt: contains all the python packages that were installed to run the program. 
6. .gitignore: contains the .venv, pycache, pytestcache, and ruff cache files, which are not tracked by git.
7. tests/__init__.py: empty python file that makes the test folder as a python package.
8. test/test_business_rules.py: contains the test 24 functions defined in order to test the 8 functions created for the business rules. 
 

## AI use statement:

I did not use AI on this exam