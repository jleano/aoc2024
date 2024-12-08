TEST1 = 18
RES1 = 2504

TEST2 = 9
RES2 = 1923


def process1(data):
    res = 0
    search = "XMAS"
    back = "SAMX"
    for line in data:
        # fwd
        res += line.count(search)
        # bckwd
        res += line.count(back)

    vert_data = _build_vert_data(data)

    for line in vert_data:
        # up
        res += line.count(search)
        # down
        res += line.count(back)

    diag_data = _build_diag_data(data)
    for line in diag_data:
        # diag
        res += line.count(search)
        # xdiag
        res += line.count(back)

    return res


def _build_vert_data(data):
    vert_data = []
    for i in range(len(data[0])):
        vertline = []
        for j in range(len(data)):
            vertline.append(data[j][i])
        vert_data.append("".join(vertline))
    return vert_data


def _build_diag_data(data):
    # go across top.
    diag_data = []
    for j in range(len(data)):
        diag_data.append(_diagonalize(0, j, data))
        diag_data.append(_xdiagonalize(0, j, data))

    # go down side.
    for i in range(1, len(data[0])):
        diag_data.append(_diagonalize(i, 0, data))
        diag_data.append(_xdiagonalize(i, len(data[0]) - 1, data))

    return diag_data


def _diagonalize(i: int, j: int, data: list[str]) -> str:
    """Get chars on diag from i/j and return as a str"""
    linelen = len(data[0])
    height = len(data)

    diag = []
    while i < linelen and j < height:
        diag.append(data[i][j])
        i += 1
        j += 1
    diagstr = "".join(diag)
    return diagstr


def _xdiagonalize(i: int, j: int, data: list[str]) -> str:
    """Get chars on diag from i/j and return as a str"""
    linelen = len(data[0])

    diag = []
    while i >= 0 and j >= 0 and i < linelen:
        # while i < linelen and j < height:
        diag.append(data[i][j])
        i += 1
        j -= 1
    diagstr = "".join(diag)
    return diagstr


def process2(data):
    linelen = len(data[0])
    height = len(data)

    res = 0
    for i in range(1, height - 1):
        for j in range(1, linelen - 1):
            v = data[i][j]
            if v == "A":
                if is_xmas(i, j, data):
                    res += 1

    return res


def is_xmas(i: int, j: int, data: list[str]) -> bool:
    topleft = data[i - 1][j - 1]
    topright = data[i - 1][j + 1]
    botleft = data[i + 1][j - 1]
    botright = data[i + 1][j + 1]

    if topleft == topright and botleft == botright:
        if (topleft == "M" and botleft == "S") or (topleft == "S" and botleft == "M"):
            return True
    if topleft == botleft and topright == botright:
        if (topleft == "M" and topright == "S") or (topleft == "S" and topright == "M"):
            return True
    return False
