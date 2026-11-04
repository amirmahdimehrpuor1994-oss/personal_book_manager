# Personal Book Manager
![Static Badge](https://img.shields.io/badge/python-blue?logo=python&logoColor=white)

A simple task manager built with python

# Features
- add multiple books
- save books
- load saved books
- admin mode

## Project Structure

`main.py` : get name , admin mode and password.

`books.py` : load and save the books

`.gitignore` : hide for git

`.env.example` : location of password

`requirements.txt` : install library

`images/` : show all images

`README` : toll all of the works for files

## How It Works

get the name person and get the person love go to the admin mode or no , get the password admin mode and save all the information!

## Troubleshooting

### 1. FileNotFoundError

**What does this error mean?**
Python is saying that the file the program is looking for does not exist — for example, when the code tries to open `books.json` but cannot find it.

**Why might this happen?**
- `books.json` has not been created yet.
- The program is being run from a different folder, while the file path in the code is relative.
- The file name has been changed, or it was saved with the wrong extension (for example, `books.json.txt`).

**What is the first thing I check to find the problem?**
I use `ls` (or `dir` on Windows) to check whether the file exists in the same folder where I am running the script, and I compare the path written in the code with the actual path.

### 2. JSONDecodeError when reading books.json

**What does this error mean?**
The program has found the file, but its contents are not valid JSON, so Python cannot read it.

**Why might this happen?**
- The file is completely empty (even an empty file is not valid JSON).
- A comma, curly brace, or bracket was added or removed during manual editing.
- The program was closed while writing the file, leaving it incomplete.
- The file was saved with the wrong encoding, or invisible characters were added to it.

**What is the first thing I check to find the problem?**
I open the file to make sure it is not empty. The error message usually gives the line and column number of the problem; I look at that line and, if needed, paste the content into an online JSON validator.

### 3. ModuleNotFoundError: No module named 'dotenv'

**What does this error mean?**
Python cannot find the `python-dotenv` package, either because it is not installed or because it was installed in an environment that is not currently being used.

**Why might this happen?**
- The command `pip install python-dotenv` has not been run.
- The package was installed in a different virtual environment (venv), and that environment is not currently active.
- The program is being run with a different Python version whose pip is separate.

**What is the first thing I check to find the problem?**
First, I make sure the virtual environment is active (`which python` or `where python`, and checking that the venv name appears in the terminal). Then I use `pip show python-dotenv` or `pip list` to see whether the package is installed in this environment.

### 4. Password is not read from the .env file

**What does this problem mean?**
The program runs, but the password value is empty (or `None`), and the database connection fails with an authentication error.

**Why might this happen?**
- The `.env` file does not exist, or its name was accidentally changed to `.env.txt`.
- The key name does not match the one read in the code (for example, `PASSWORD` versus `password`, or there is an extra space).
- `load_dotenv()` was not called, or it was called after the variables were read.
- The `.env` file is in a different folder, and the program cannot find it.
- The value is wrapped in quotes and has extra spaces.

**What is the first thing I check to find the problem?**
I check that the `.env` file is next to the main script and that the key name exactly matches `os.getenv("PASSWORD")` in the code. Then I temporarily add `print(os.getenv("PASSWORD"))` to see whether the value is read or whether it returns `None`.

# Requirements
- python
- python-dotenv

## Installation
Install the required paskages :

```bash
python -m pip install -r requirments.txt
```

## Envoirment setup
create a `env` file in the project folder

Use `.env.example` as a template

Add your admin password

```env
admin_pass=your_password_here
```
replase `your_password_here` with your own admin password

run the main file
```bash
python main.py
```

## Screenshot
![personal_book_manager_screenshot](images\world.png)

## Demo

![personal_book_manager_demo](images\Animation.gif)