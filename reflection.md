# Lab 5 — Static Code Analysis: Reflection

> **Note:** The supplied three-page handout describes the reflection deliverable but does not display the four reflection questions themselves. These responses cover four common reflection themes. If your instructor supplied a separate page or LMS questions, match these answers to that exact wording before submission.

## 1. What did you learn about static code analysis?

I learned that static analysis tools can identify problems without needing to execute the program. Pylint focuses on code quality and maintainability, Flake8 checks style and formatting, and Bandit looks for potentially unsafe coding patterns. Using all three gave a broader view of the same program.

## 2. Which issue was most important, and why?

The highest-severity finding was the use of `os.system()` with a command assembled using an email address. Passing user-controlled data into a shell command can create a command-injection risk. The code was changed to use Python's email and SMTP libraries instead. The unsafe `pickle.load()` call was also important because loading untrusted pickle data can be dangerous, so persistence was changed to JSON.

## 3. How did the fixes improve the program?

The fixes improved security, readability, and reliability. Replacing the mutable default list prevents values from unintentionally being shared between function calls. Consistent `snake_case` naming and docstrings make the code easier to understand. Explicit return behavior makes the search function predictable, while UTF-8 encoding improves portability. The final checks reported Pylint 10.00/10, no Bandit findings, and no Flake8 violations.

## 4. What challenges did you face, and how would you use these tools in future projects?

One challenge was interpreting findings from different tools and deciding which to address first. Bandit's severity levels helped prioritize the shell-command and pickle findings, while Pylint and Flake8 highlighted maintainability and formatting problems. In future projects, I would run these tools early and repeatedly, keep before-and-after reports, and use the results as part of code review rather than waiting until the end.
