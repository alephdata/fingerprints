from fingerprints import clean_name_ascii, clean_name_light


def test_clean_name_ascii():
    assert clean_name_ascii("Владимир Путин") == "vladimir putin"
    assert clean_name_ascii("Владимир Пути'н") == "vladimir putin"


def test_clean_name_light():
    assert clean_name_light("Vladimir Putin") == "vladimir putin"
    assert clean_name_light("C.I.A.") == "cia"
    assert clean_name_light("UN") == "un"
    assert clean_name_light("U") is None
