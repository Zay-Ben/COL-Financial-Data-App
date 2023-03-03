import pandas as pd

def cf(path_col):

    path_pse = "inputs/PSE.xlsx"

    # All Shares Index (ASI)

    asi = pd.read_excel(io = path_col, sheet_name = "ASI", index_col = 1, skiprows = 1)

    asi.index.rename(name = "Ticker", inplace = True)

    # Investment Guide (IG)

    ig = pd.read_excel(io = path_col, sheet_name = "IG", index_col = 0)

    ig.index.rename(name = "Ticker", inplace = True)

    # Technical Guide (TG)

    tg = pd.read_excel(io = path_col, sheet_name = "TG", index_col = 0, parse_dates = [10])

    tg.drop(columns = "Company Name", inplace = True)

    # Company List (CL)

    cl = pd.read_excel(io = path_pse, sheet_name = "Sheet1", index_col = 1, parse_dates = [4])

    cl.index.rename(name = "Ticker", inplace = True)

    # COL Financial (COL) Temporary

    col_temporary = cl.join(asi.join(ig.join(tg)))

    # Export Data

    return col_temporary
