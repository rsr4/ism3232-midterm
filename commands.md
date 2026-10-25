# Terminal Record: Cloudstep Software

## 1.Building the project:
```bash
history 500
```

```text

  820  mkdir ism3232-midterm
  821  cd ism3232-midterm
  822  ls
  823  python3 -m venv .venv
  824  source .venv/bin/activat
  825  source .venv/bin/activate
  826  python -m pip install pytest ruff
  827  python -m pip freeze > requirements.txt
  828  cat requirements.txt
  829  touch .gitignore
  830  print f'.venv/\n.__pycache__/\n.pytest_cache/\n.ruff_cache/\n' > .gitignore
  831  ls -la
  832  cat .gitignore
  833  printf '.venv/\n.__pycache__/\n.pytest_cache/\n.ruff_cache/\n' > .gitignore
  834  cat gitignore
  835  cat .gitignore
  836  gs
  837  git init
  838  gs
  839  git remote -v
  840  git remote add origin https://github.com/rsr4/ism3232-midterm.git
  841  git remote -v
  842  gs
  843  git add .
  844  ls
  845  touch business_rules.py
  846  ls
  847  touch main.py
  848  ls
  849  ls la
  850  ls -la
  851  touch commands.md README.md
  852  ls
  853  mkdir tests
  854  cd tests
  855  ls
  856  touch __init__.py test_business_rules.py
  857  ls
  858  ..
  859  cd ..
  860  tree
  861  gs
  862  git add .
  863  gs
  864  git commit -m 'ism3232 midterm file environment setup'
  865  git push
  866  git push -u origin main 
  867  ls
  868  ls
  869  cd ism3232-midterm
  870  ls
  871  code .
  872  source .venv/bin/activate
  873  code .
  874  source .venv/bin/deactivate
  875  deactivate
  876  cd ..
  877  cd ism3232-midterm
  878  ls
  879  code .
  880  source .venv/bin/activate
  881  code .
  882  deactive
  883  deactivate
  884  cd ..
  885  cd ism3232-midterm
  886  source .venv/bin/activate
  887  code .
  888  gs
  889  git add .
  890  gs
  891  git commit -m 'ism3232-midterm business rules functions created'
  892  git push
```

## 2. The virtual Environment:

```bash
which python3
```
```text
/Users/rahim/ism3232-midterm/.venv/bin/python3
```

The output of which python3 shows this file path, the .venv shows that the virtual environment is active.

## 3. The project structure:

```bash
tree -L 2
```

```text
.
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

A file that is not in my git repository would be the .venv and pip install files, this is because they are placed in my .gitignore file which git does not track.

## 4. Every function and test:

```bash
rg 'def '
```

```text
3:def calculate_license_cost(seat_price: float, seats: int) -> float:
7:def get_seat_discount(seats: int, education: bool = False) -> float:
15:def calculate_license_total(seat_price: float, seats: int, education: bool = False) -> float:
23:def needs_contract_review(total: float) -> bool:
29:def get_trainer(seats: int, total: float) -> bool:
35:def total_licensed(orders: list) -> float:
48:def largest_license(orders: list) -> str:
64:def format_license_line(company: str, total: float, contract_review: bool, trainer: bool) -> str:

tests/test_business_rules.py
4:def test_calculate_license_cost():
8:def test_get_seat_discount_education():
12:def test_get_seat_discount_seat_under():
16:def test_get_seat_discount_over():
20:def test_get_seat_discount_under():
24:def test_calculate_license_total_over():
28:def test_calculate_license_total_boundary_under():
32:def test_calculate_license_total_boundary_over():
36:def test_calculate_license_total_under_with_discount():
40:def test_calculate_license_total_under():
44:def test_needs_contract_review_over():
48:def test_needs_contract_review_under():
52:def test_needs_contract_review_boundary_over():
56:def test_needs_contract_review_boundary_under():
60:def test_get_trainer_true():
64:def test_get_trainer_false():
68:def test_get_trainer_true_seat():
72:def test_get_trainer_true_price():
76:def test_get_trainer_false_boundary():
80:def test_total_licensed():
89:def test_largest_license_tie():
98:def test_largest_license_empty():
104:def test_format_license_line():
109:def test_format_license_line_false():
```

There are 8 total functions that define the business_rules.py file, and 24 test functions that define the tests/test_business_rules.py file. 

## 5. Which files print:

```bash
rg -l 'print'
```
```text
main.py
```

Only main.py prints and not business_rules.py, this is due to keep the structure organized. The business_rule.py file does not contain print because the purpose is to define business logic and that return to main.py to run the program.

## 6. The commit history: 

```bash
git log --online
```
```text
2ff8032 (HEAD -> main, origin/main) test functions for business rules created
cc50e45 used business logic functions in main file to get output from test data, also fixed some syntax in bussiness_rules file
69c3855 ism3232-midterm business rules functions created
9323089 ism3232 midterm file environment setup
```

there are 4 commits in total so far in the project, each commit iteratively built on the projects requirements, documenting the changes at each step. 