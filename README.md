# Lab 5: Static Code Analysis — Todo Manager

## Overview

This project demonstrates the use of Python static code analysis tools to improve code quality, security, readability, and maintainability. The assigned Todo Manager program was analyzed using **Pylint, Bandit, and Flake8**, and the identified issues were fixed.

## Tools Used

- **Pylint** — Identifies code-quality issues, naming problems, and potential bugs.
- **Bandit** — Detects common security vulnerabilities and unsafe coding patterns.
- **Flake8** — Checks Python style and formatting according to PEP 8 guidelines.

## Issues Identified and Fixed

The following issues were addressed:

- Replaced the mutable default argument `labels=[]` with `labels=None`.
- Improved function and variable naming using `snake_case`.
- Added module and function docstrings.
- Added an explicit return value when a task search finds no match.
- Replaced unsafe `pickle` persistence with JSON.
- Replaced shell-based email execution using `os.system()` with Python's email and SMTP libraries.
- Added email-address validation.
- Specified UTF-8 encoding when reading and writing JSON files.
- Replaced `random.choice()` with `secrets.choice()` and handled an empty task list.
- Corrected formatting and whitespace violations reported by Flake8.

## Analysis Results

| Tool | Before fixes | After fixes |
|---|---|---|
| Pylint | 5.09/10 | 10.00/10 |
| Bandit | 4 findings | No issues identified |
| Flake8 | 4 violations | No violations |

## How to Run

### 1. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows Command Prompt:

```cmd
venv\Scripts\activate
```

### 2. Install the analysis tools

```bash
pip install pylint bandit flake8
```

### 3. Run the Todo Manager

```bash
python todo_manager.py
```

### 4. Run static analysis

```bash
python -m pylint todo_manager.py
python -m bandit todo_manager.py
python -m flake8 todo_manager.py
```

## Repository Contents

- `todo_manager.py` — Updated Todo Manager source code.
- `pylint_before.txt` and `pylint_after.txt` — Pylint reports before and after fixes.
- `bandit_before.txt` and `bandit_after.txt` — Bandit reports before and after fixes.
- `flake8_before.txt` and `flake8_after.txt` — Flake8 reports before and after fixes.
- `issues.md` — Table of identified issues and their fixes.
- `reflection.md` — Reflection on the static analysis exercise.

## Learning Outcomes

This exercise demonstrates how static analysis tools can help identify and fix security risks, coding mistakes, and style violations. Running the tools before and after the changes helps verify that the code has improved.

## Conclusion

The Todo Manager was updated to address the identified static analysis findings. The final checks achieved a Pylint score of 10.00/10, no Bandit findings, and no Flake8 violations.
