# PakGov Document Search CLI

A Python command-line tool for searching keywords across Pakistani government documents.

The tool searches multiple `.txt` documents, returns matching lines with surrounding context, and records searches in a CSV history file.

## Features

* **Keyword Search** — search across multiple government text documents.
* **Context Display** — shows one line before and after each matching result.
* **Search History** — records searches with date and time in `history.csv`.
* **Error Handling** — handles invalid queries and missing document folders.
* **Modular Structure** — separates document reading, search logic, and custom exceptions.
* **Command-Line Interface** — designed to run directly from a terminal.

## Technologies

* Python 3
* `os`
* `csv`
* `re`
* `datetime`
* `sys`

## Concepts Demonstrated

* File I/O
* Text processing
* Regular expressions
* Command-line arguments
* CSV data handling
* Exception handling
* Modular Python design

## Project Structure

```text
Pakgov-search-cli/
│
├── docs/                  # Text documents searched by the tool
├── search.py              # Main search functionality
├── document_reader.py     # Document reading logic
├── exceptions.py          # Custom exceptions
├── history.csv            # Search history
├── .gitignore
├── LICENSE
└── README.md
```

## How It Works

1. Place searchable `.txt` documents inside the `docs/` directory.
2. Run the CLI from the project directory.
3. Enter a keyword to search.
4. The program scans the available documents.
5. Matching results are displayed with surrounding context.
6. The search is recorded in `history.csv`.

## Installation

Clone the repository:

```bash
git clone https://github.com/salikhussain71-code/Pakgov-search-cli.git
```

Enter the project directory:

```bash
cd Pakgov-search-cli
```

## Running the Project

Run the main program:

```bash
python search.py
```

Make sure the `docs/` directory contains the `.txt` documents you want to search.

## Why This Project

Finding specific information across large collections of government documents can be time-consuming when performed manually.

This project provides a lightweight command-line approach for searching local document collections and displaying relevant context around matches.

## License

This project is licensed under the MIT License.
