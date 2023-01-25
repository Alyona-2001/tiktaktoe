import pytest 

from tiktaktoe import (
    five_mark_check,
    create_game_area,
    output_game_area,
    set_mark_position,
    check_user_position,
    win_check,
    full_check
)


data_five_mark_check = [
    ("XXXXX", "X", True),
    ("XXXXX", "O", False),
]


@pytest.mark.parametrize(
    "temp, mark, result", data_five_mark_check
)
def test_five_mark_check(temp, mark, result):
    assert five_mark_check(temp, mark) is result


neg_data_five_mark = [
    ("", "X", False),
    ("", "", False),
    ("", 1, False),
]


@pytest.mark.parametrize(
    "temp, mark, result", neg_data_five_mark
)
def negative_test_five_mark_check(temp, mark, result):
    assert five_mark_check(temp, mark) is result


count_cells = [n for n in range(10)]


@pytest.mark.parametrize("count_cell", count_cells)
def test_create_game_area(count_cell):

    test_game_area = [numb for numb in range(count_cell * count_cell)]
    game_area = create_game_area(count_cell)

    assert game_area == test_game_area


def test_create_game_area_1():
    count_cell_test = -1
    count_cell = 1
    test_game_area = [numb for numb in range(count_cell * count_cell)]
    game_area = create_game_area(count_cell_test)

    assert game_area == test_game_area

    count_cell_test = "1"
    count_cell = 1
    test_game_area = [numb for numb in range(count_cell * count_cell)]
    game_area = create_game_area(count_cell_test)

    assert game_area == test_game_area


@pytest.mark.parametrize(
    "count_cell", ["", "none", None])
def neg_test_create_game_area(count_cell):
    try:
        game_area = create_game_area(count_cell)
    except Exception as ex:
        assert ex is ValueError


GAME_AREA = ([numb for numb in range(10 * 10)],)


@pytest.mark.parametrize(
    "game_area", GAME_AREA
)
def test_set_mark_position(game_area: list[int]):
    user_mark = "X"
    user_pos = 0

    assert set_mark_position(user_mark, game_area, user_pos) is True

    user_mark = "O"
    user_pos = 0

    assert set_mark_position(user_mark, game_area, user_pos) is False

    user_mark = "X"
    user_pos = 0

    assert set_mark_position(user_mark, game_area, user_pos) is False

    user_mark = "X"
    user_pos = -1
    assert set_mark_position(user_mark, game_area, user_pos) is False

    user_mark = "X"
    user_pos = 200
    assert set_mark_position(user_mark, game_area, user_pos) is False


GAME_AREA = ([numb for numb in range(10 * 10)],)


@pytest.mark.parametrize(
    "game_area", GAME_AREA
)
def test_check_user_position(game_area):
    user_mark = "X"
    user_pos = 0

    assert check_user_position(user_pos, 10, user_mark, game_area) is True

    user_mark = "O"
    user_pos = 0

    assert check_user_position(user_pos, 10, user_mark, game_area) is False

    user_mark = "X"
    user_pos = 0

    assert check_user_position(user_pos, 10, user_mark, game_area) is False

    user_mark = "X"
    user_pos = -1

    assert check_user_position(user_pos, 10, user_mark, game_area) is False

    user_mark = "X"
    user_pos = 200

    assert check_user_position(user_pos, 10, user_mark, game_area) is False


GAME_AREA = ([numb for numb in range(10 * 10)],)


@pytest.mark.parametrize(
    "game_area", GAME_AREA
)
def test_output_game_area(game_area):
    assert output_game_area(game_area, 10) is None


def test_full_check():
    game_area = [numb for numb in range(10 * 10)]

    assert full_check(game_area) is False

    for i in range(10 ** 2, 2):
        game_area[i] = "X"
        game_area[i] = "O"

    assert full_check(game_area) is False


def test_win_check():
    game_area = [numb for numb in range(10 * 10)]

    assert win_check(game_area, "X", 10, 1) is False

    game_area[0] = "X"
    game_area[1] = "X"
    game_area[2] = "X"
    game_area[3] = "X"
    game_area[4] = "X"

    assert win_check(game_area, "X", 10, 5) is True

    game_area = [numb for numb in range(10 * 10)]
    game_area[0] = "X"
    game_area[11] = "X"
    game_area[22] = "X"
    game_area[33] = "X"
    game_area[44] = "X"

    assert win_check(game_area, "X", 10, 44) is True

    game_area = [numb for numb in range(10 * 10)]
    game_area[9] = "X"
    game_area[18] = "X"
    game_area[27] = "X"
    game_area[36] = "X"
    game_area[45] = "X"

    assert win_check(game_area, "X", 10, 45) is True

    game_area = [numb for numb in range(10 * 10)]
    game_area[0] = "X"
    game_area[10] = "X"
    game_area[20] = "X"
    game_area[30] = "X"
    game_area[40] = "X"

    assert win_check(game_area, "X", 10, 40) is True
