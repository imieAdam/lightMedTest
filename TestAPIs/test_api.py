def login():
    return True

def logout():
    return 1

def test_login():
    assert login()

def test_logout():
    assert logout() == 1