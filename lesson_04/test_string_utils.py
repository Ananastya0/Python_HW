import pytest
from string_utils import StringUtils

@pytest.mark.parametrize(
     "input_text, expected_output",
     [
         ("hello", "Hello"),
         ("postman", "Postman"),
         ("between us", "Between us"),
    ],
 )
def test_capitilize_positive(input_text, expected_output):
     string = StringUtils()
     assert string.capitilize(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [("123", "123"), (" ", " ")])

def test_capitilize_negative(input_text, expected_output):
    string = StringUtils()
    assert string.capitilize(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
     [
         ("  some", "some"),
         (" nice", "nice"),
         ("   A one people", "A one people"),
    ],)

def test_trim_pozitive(input_text, expected_output):
    string = StringUtils()
    assert string.trim(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [("  ", ""), (".", ".")])

def test_trim_negative(input_text, expected_output):
    string = StringUtils()
    assert string.trim(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, delimeter, expected_output",
     [
         ("momy,popy", ",", ["momy", "popy"]),
         ("1,2,3", ",", ["1", "2", "3"]),
         ("a,b", ",", ["a", "b"]),
    ],)

def test_to_list_pozitive(input_text, delimeter, expected_output):
    string = StringUtils()
    assert string.to_list(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, delimeter, expected_output",
     [
         ("", ",", []),
         ("1,2,3", ",", ["1", "2", "3"])
    ],)

def test_to_list_negative(input_text, delimeter, expected_output):
    string = StringUtils()
    assert string.to_list(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
     [
         ("love", "v", True),
         ("money", "e", True),
         ("very", "y", True),
    ],)

def test_contains_pozitive(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.contains(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [("home", "a", False), ("long", "b", False)])

def test_contains_negative(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.contains(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
     [
         ("list", "l", "ist"),
         ("lovely", "ve", "loly"),
         ("high", "g", "hih"),
    ],)

def test_delete_symbol_pozitive(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.delete_symbol(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [("honey", "a", "honey"), ("", "bee", "")])

def test_delete_symbol_negative(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.delete_symbol(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
     [
         ("big momy", "b", True),
         ("Korn", "K", True),
         ("SOD", "S", True),
    ],)

def test_starts_with_pozitive(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.starts_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [(" dady", "d", False), (" ", "a", False)])

def test_starts_with_negative(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.starts_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
     [
         ("silly", "y", True),
         ("Kiss me", "e", True),
         ("System Of A Down", "n", True),
    ],)

def test_end_with_pozitive(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.end_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [("fail.", "l", False), (".", ",", False)])

def test_end_with_negative(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.end_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
     [
         ("   ", True),
         (" ",True),
         ("",True),
    ],)

def test_is_empty_pozitive(input_text, expected_output):
    string = StringUtils()
    assert string.is_empty(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [(".", False), ("n", False)])

def test_is_empty_negative(input_text, expected_output):
    string = StringUtils()
    assert string.is_empty(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, joiner, expected_output",
     [
         ([1,2,3,4], ", ", "1, 2, 3, 4"),
         (["a", "b", "c", "d"], ", ", "a, b, c, d"),
         (["love", "is"], "," , "love, is"),
    ],)

def test_list_to_string_pozitive(input_text, joiner, expected_output):
    string = StringUtils()
    assert string.list_to_string(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, joiner, expected_output",
    [(["1", "2"], ", ", "1,2"), (["a", "b"], ", ", "a,b")])

def test_list_to_string_negative(input_text, joiner, expected_output):
    string = StringUtils()
    assert string.list_to_string(input_text) != expected_output