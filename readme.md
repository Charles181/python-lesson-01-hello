## 📝 Python Study Group - Foundations lesson \#1

### Welcome to Python\!

Python is a high-level, interpreted programming language known for its **readability** and **simplicity**. Its design philosophy emphasizes clean code and plain English syntax, which is why it's a favorite for beginners and professionals alike.

### 🌐 Where is Python Used?

Python's versatility makes it one of the most widely used languages in tech:

  * **Web Development:** Used for creating the back-end (server-side) of websites and applications (e.g., Django, Flask).
  * **Data Science & Analysis:** The industry standard for processing large datasets, statistical modeling, and visualization (e.g., Pandas, NumPy).
  * **Artificial Intelligence (AI) & Machine Learning (ML):** Dominant language for building neural networks and training AI models (e.g., TensorFlow, PyTorch).
  * **Automation & Scripting:** Writing small scripts to automate repetitive tasks, manage systems, and perform testing.

### 🛠️ Setting Up and Running Python

For this course, you primarily need a text editor and the Python interpreter.

#### Installing Python (Optional for Codespaces)

  * **GitHub Codespaces:** No installation needed\! This is a pre-configured, cloud-based environment (VS Code in your browser) that has Python ready to go.
  * **Windows/macOS/Linux:** Download the latest installer from the official [Python website](https://www.python.org/downloads/). **Important:** On Windows, make sure to check the box that says **"Add python.exe to PATH"** during installation.

#### Running Python Code

| Method | Environment | How to Run |
| :--- | :--- | :--- |
| **GitHub Codespace** (Recommended) | In-browser VS Code | Click the **"Run"** button in the top right corner, or use the integrated terminal: `python yourfile.py` |
| **VS Code / Other IDE** | Local Computer | Open the file, then open the terminal (or press `Ctrl`+`Shift`+`P` and type 'Python: Run'), or use the terminal: `python yourfile.py` |
| **IDLE / Terminal** | Local Computer | Open the file in the editor, or use the Command Prompt/Terminal: `python yourfile.py` |

### 💬 Printing Output to the Console

The most basic and essential action in Python is displaying text. We do this using the built-in `print()` function:

```python
# The text you want to display goes inside the parentheses and quotes.
print("I am Python code!")
```

The text inside the quotes is called a **string**.

### Working with Strings in Python

Strings, in Python and most programming languages, are how we represent text. They can be created using single quotes (`'`) or double quotes (`"`). The opening and closing quote character must match, so either `'Hello'` or `"Hello"` are valid, but `"Hello'` is not.

Strings are very flexible, and there's no difference between using single or double quotes—it's mainly a matter of style, or which is more convenient for your content.

#### Using Quotes Inside Strings

If your string contains a quote character (for example, an apostrophe `'` in a word like "don't"), you can choose the alternative quote style to avoid errors:
- `'I don\'t know'` or `"I don't know"` both work.

Similarly, if you want to include a double quote inside the string:
- `"He said, \"Python is fun!\""` or `'He said, "Python is fun!"'`

#### Escape Characters

An escape character in Python is a backslash (`\`). You use it to tell Python to treat the next character as a literal value, not as a special symbol. This lets you:
- Put quotes inside strings opened with the same quote character, e.g., `'It\'s a sunny day'` or `"She said, \"Hi!\""`
- Insert special characters like a new line (`\n`), a tab (`\t`), or even a backslash itself (`\\`).

##### Examples
```python
print('It\'s easy to print apostrophes.')
print("He said, \"Welcome to Python!\"")
print('She replied, "That\'s awesome!"')
print("A backslash looks like this: \\")
```

These features make it easy to handle any type of text you need in your programs.

-----

## 🚀 Assignment: Hello, World\!

The traditional first step in learning any programming language.

### Goal

Edit the script named **`hello.py`** in this repository so that it executes the following instruction:

> **Print the exact phrase "Hello, World\!" to the console.**

### Instructions

1.  **Fork** this repository to your own GitHub account.
2.  Open **your forked repository** in **GitHub Codespaces**.
3.  Edit the code inside `hello.py`.
4.  Once finished, use the **Source Control** tool in Codespaces to **Commit & Push** your changes.
5.  Check the **Actions** tab on your repository to see your passing grade (Green Checkmark ✅).

**If you have any questions or issue regarding this assignment, feel free to ask for help in the [discord server](https://discord.gg/7FNyQk4gU) problems-and-answers channel**.
