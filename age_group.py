def get_age_group(age):
    """
    Devuelve el grupo de edad basado en la edad en años.
    Si no se encuentra en un rango válido, devuelve 'desconocido'.
    """
    if age < 0:
        return 'desconocido'
    elif age <= 14:
        return 'infancia'
    elif age <= 24:
        return 'juventud'
    elif age <= 64:
        return 'adultez'
    elif age <= 89:
        return 'vejez'
    else:
        return 'desconocido'


def test_get_age_group():
    """Prueba unitaria para get_age_group"""
    assert get_age_group(-1) == 'desconocido'
    assert get_age_group(0) == 'infancia'
    assert get_age_group(14) == 'infancia'
    assert get_age_group(15) == 'juventud'
    assert get_age_group(24) == 'juventud'
    assert get_age_group(25) == 'adultez'
    assert get_age_group(64) == 'adultez'
    assert get_age_group(65) == 'vejez'
    assert get_age_group(89) == 'vejez'
    assert get_age_group(150) == 'desconocido'
