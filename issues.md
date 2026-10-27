# Lab 5 — Static Code Analysis: Issues and Fixes

**File analyzed:** `todo_manager.py`  
**Tools:** Pylint, Bandit, Flake8

| Issue | Type | Original line(s) | Description / finding | Fix approach |
|---|---|---:|---|---|
| Shell command injection risk (`os.system`) | Security — High | 57 | Bandit B605 warned that `os.system()` starts a shell and can allow command injection when user-controlled input is concatenated into the command. | Removed the shell command and implemented email sending through Python's `smtplib` and `EmailMessage`; validate the email address before sending. |
| Unsafe deserialization with `pickle.load` | Security — Medium | 47 | Bandit B301 warned that loading pickle data can execute unsafe deserialization behavior if the file is untrusted. | Replaced pickle persistence with JSON serialization/deserialization. JSON does not deserialize arbitrary Python objects in the way pickle can. |
| Importing `pickle` | Security — Low | 3 | Bandit B403 flagged the pickle import because of its potential security implications. | Removed the `pickle` import after switching persistence to JSON. |
| Mutable default argument `labels=[]` | Code quality / bug risk | 11 | Pylint W0102 flagged a mutable default shared across calls, which can cause state to leak between calls. | Changed the default to `None` and creates a new list inside the function when labels are not supplied. |
| Inconsistent return behavior in `findTask` | Code quality | 33–36 | Pylint R1710 reported that the function returned a task ID for a match but implicitly returned `None` otherwise. | Added an explicit `return None` for the no-match case. |
| Non-PEP 8 naming and missing docstrings | Code quality | Multiple | Pylint flagged camelCase function/variable names and missing module/function docstrings. | Renamed functions and variables to `snake_case` and added module/function docstrings. |
| Unspecified file encoding | Code quality / portability | 51 | Pylint W1514 warned that `open()` was used without an explicit encoding. | Used file paths opened with `encoding="utf-8"` for JSON files. |
| Standard pseudo-random generator warning | Security lint warning — Low | 70 | Bandit B311 flagged `random.choice()` as unsuitable for security-sensitive randomness. In this task suggestion feature, cryptographic randomness is not strictly required, but the warning was addressed. | Replaced `random.choice()` with `secrets.choice()` and added a check for an empty pending-task list. |
| Flake8 whitespace and formatting violations | Style | 12, 40, 69, 74 | Flake8 reported E225 (missing operator whitespace), E303 (extra blank lines), E261 (inline comment spacing), and E231 (missing space after comma). | Reformatted expressions, removed excess blank lines, corrected inline-comment spacing, and added missing whitespace. |

## Verification results

- **Pylint before:** 5.09/10
- **Pylint after:** 10.00/10
- **Bandit before:** 4 findings (1 high, 1 medium, 2 low)
- **Bandit after:** No issues identified
- **Flake8 before:** 4 violations
- **Flake8 after:** No output; the command exited with code `0`, indicating no violations.
