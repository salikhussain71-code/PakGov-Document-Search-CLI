"""Tests for the PakGov Document Search CLI history log."""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import search


HEADER = ["timestamp", "keyword", "results_found"]


def read_history():
    with open("history.csv", newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


def test_save_to_history_empty_file_gets_header(tmp_path, monkeypatch):
    # A pre-existing but empty history.csv (e.g. a placeholder checked into
    # version control) used to stay headerless, corrupting the CSV.
    monkeypatch.chdir(tmp_path)
    open("history.csv", "w").close()
    search.save_to_history("pakistan", 3)
    rows = read_history()
    assert rows[0] == HEADER
    assert rows[1][1:] == ["pakistan", "3"]


def test_save_to_history_missing_file_gets_header(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    search.save_to_history("lahore", 1)
    rows = read_history()
    assert rows[0] == HEADER
    assert rows[1][1:] == ["lahore", "1"]


def test_save_to_history_existing_file_no_duplicate_header(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    search.save_to_history("a", 1)
    search.save_to_history("b", 2)
    rows = read_history()
    assert rows[0] == HEADER
    assert [r[1:] for r in rows[1:]] == [["a", "1"], ["b", "2"]]
