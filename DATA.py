from ROW import ROW
from COLS import COLS


class DATA:
    def __init__(self, src):
        self.cols = None
        self.rows = []

    def add(self, t, fun=None, row=None):
        row = t["cells"] if isinstance(t, dict) and "cells" in t else ROW(t)
        if self.cols:
            if fun:
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
            self.cols = COLS(row)

    def mid(self, cols=None):
        u = []
        for col in cols or self.cols.all:
            u.append(col.mid())
        return ROW(u)

    def div(self, cols=None):
        u = []
        for col in cols or self.cols.all:
            u.append(col.div())
        return ROW(u)

    def small(self, cols=None):
        u = []
        for col in cols or self.cols.all:
            u.append(col.small())
        return u

    def stats(self, cols=None, fun=None, ndivs=None):
        u = {".N": len(self.rows)}
        col_name = cols if cols else self.cols.all
        for col in (col_name):
            u[col.txt] = round(float(col.mid()), ndivs) if isinstance(col.mid(), (int, float)) else col.mid()
        return u