import pytest
from main import greet_user, add_numbers

def test_add_numbers():
    result = add_numbers(3, 5)
    assert result == 8, f"Așteptam 8, dar am primit {result}"

def test_greet_user():
    from io import StringIO
    import sys

    captured_output = StringIO()
    sys.stdout = captured_output

    greet_user("Anastasia")

    sys.stdout = sys.__stdout__

    assert captured_output.getvalue().strip() == "Salut, Anastasia! Bun venit pe ramura feature-a și feature-b!", \
        f"Așteptam mesajul 'Salut, Anastasia! Bun venit pe ramura feature-a și feature-b!', dar am primit {captured_output.getvalue()}"
