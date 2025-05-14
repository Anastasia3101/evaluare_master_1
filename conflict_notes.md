# Conflict Rezolvat între feature-a și feature-b

În urma îmbinării ramurilor `feature-a` și `feature-b`, a apărut un conflict în funcția `greet_user` din fișierul `main.py`. Conflictul a fost rezolvat astfel:

- Mesajul de întâmpinare a fost modificat pentru a include atât informațiile din `feature-a`, cât și cele din `feature-b`.
- Decizia a fost de a combina ambele mesaje, având în vedere că ambele ramuri aduc informații importante despre ramura specifică.

Noua funcționalitate este:
```python
def greet_user(name):
    print(f"Salut, {name}!")
    print(f"Bun venit pe ramura feature-a și feature-b!")
