from rainbow_spirograph import create_rainbow_colors


def test_create_rainbow_colors():
    assert create_rainbow_colors(3) == [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
    ]
