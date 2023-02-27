import pandas as pd
from datetime import datetime
import numpy as np

def dp(col_temporary):

    # Data Preprocessing

    # ASI (Change, Previous, and Out. Shares)

    col_temporary["P"] = col_temporary["Change"] + col_temporary["Previous"]

    col_temporary["P (%)"] = col_temporary["Change"] / col_temporary["Previous"] * 100

    col_temporary["MC (Billion)"] = col_temporary["Out. Shares"] * col_temporary["P"] / 10 ** 9

    # Year

    year = datetime.today().year

    year = year - 2000

    year = year - 1

    year = str(year)

    # IG (Unnamed: 7, Unnamed: 2, Unnamed: 9, and Unnamed: 10)

    col_temporary["EPS{}E (%)".format(year)] = col_temporary["Unnamed: 7"] * 100

    col_temporary["BV{}E".format(year)] = col_temporary["Unnamed: 2"] / col_temporary["Unnamed: 9"]

    col_temporary["D{}E".format(year)] = col_temporary["Unnamed: 2"] * col_temporary["Unnamed: 10"]

    col_temporary["P/BV{}E".format(year)] = col_temporary["P"] / col_temporary["BV{}E".format(year)]

    col_temporary["D{}E (%)".format(year)] = col_temporary["D{}E".format(year)] / col_temporary["P"] * 100

    # Drop Columns

    col_temporary.drop(columns = ["#", "Previous", "Last", "% Change", "Change", "Volume", "Out. Shares",
                                  "Unnamed: 1", "Unnamed: 2", "Unnamed: 5", "Unnamed: 7", "Unnamed: 8", "Unnamed: 9", "Unnamed: 10",
                                  "Price", "52 Wk High"], inplace = True)

    # Rename Columns

    col_temporary.rename(columns = {"Unnamed: 3" : "Fundamental Rating",
                                    "Unnamed: 4" : "FV",
                                    "Unnamed: 6" : "EPS{}E".format(year),
                                    "Short Term" : "32MA",
                                    "Medium Term" : "65MA",
                                    "High" : "52H",
                                    "Low" : "52L",
                                    "Trend Mode" : "Trend",
                                    "Recommendation" : "Technical Rating",
                                    "Rating Initiated" : "Technical Rating Initiated"}, inplace = True)

    # Create Columns

    # CL

    col_temporary["Age"] = col_temporary["Listing Date"].apply(lambda x: datetime.today().year - x.year)

    # IG

    col_temporary["FV (%)"] = (col_temporary["FV"] - col_temporary["P"]) / col_temporary["P"] * 100

    col_temporary["P/FV"] = col_temporary["P"] / col_temporary["FV"]

    col_temporary["PE{}E".format(year)] = col_temporary["P"] / col_temporary["EPS{}E".format(year)]

    col_temporary["PEG{}E".format(year)] = col_temporary["PE{}E".format(year)] / col_temporary["EPS{}E (%)".format(year)] / 100

    # TG

    col_temporary["32MA (S/R/B)"] = np.select(condlist = [col_temporary["P"] > col_temporary["32MA"],
                                                          col_temporary["P"] < col_temporary["32MA"],
                                                          col_temporary["P"] == col_temporary["32MA"]],
                                              choicelist = ["Support",
                                                            "Resistance",
                                                            "Breakdown/Breakout"],
                                              default = None)

    col_temporary["65MA (S/R/B)"] = np.select(condlist = [col_temporary["P"] > col_temporary["65MA"],
                                                          col_temporary["P"] < col_temporary["65MA"],
                                                          col_temporary["P"] == col_temporary["65MA"]],
                                              choicelist = ["Support",
                                                            "Resistance",
                                                            "Breakdown/Breakout"],
                                              default = None)

    col_temporary["32MA (%)"] = (col_temporary["32MA"] - col_temporary["P"])  / col_temporary["P"] * 100

    col_temporary["65MA (%)"] = (col_temporary["65MA"] - col_temporary["P"])  / col_temporary["P"] * 100

    col_temporary["52H (%)"] = (col_temporary["P"] - col_temporary["52H"])  / col_temporary["52H"] * 100

    col_temporary["52L (%)"] = (col_temporary["P"] - col_temporary["52L"])  / col_temporary["52L"] * 100

    col_temporary["P/52H"] = col_temporary["P"] / col_temporary["52H"]

    col_temporary["P/52L"] = col_temporary["P"] / col_temporary["52L"]

    # Format Data

    col_temporary = col_temporary[["Company Name", "Sector", "Subsector", "Listing Date", "Age",
                                   "P", "P (%)", "Value", "MC (Billion)",
                                   "Fundamental Rating", "FV", "FV (%)", "P/FV", "EPS22E", "EPS22E (%)", "PE22E", "PEG22E", "BV22E", "P/BV22E", "D22E", "D22E (%)",
                                   "Trend", "Technical Rating", "Technical Rating Initiated", "32MA (S/R/B)", "32MA", "32MA (%)", "65MA (S/R/B)", "65MA", "65MA (%)", "52H", "52H (%)", "P/52H", "52L", "52L (%)", "P/52L"]]

    numerical_variables = col_temporary.select_dtypes(include = float)

    numerical_variables = numerical_variables.columns

    numerical_variables = list(numerical_variables)

    numerical_variables.remove("P")

    col_temporary["P"] = round(col_temporary["P"], 4)

    col_temporary[numerical_variables] = round(col_temporary[numerical_variables], 2)

    # COL Financial (COL)

    col = col_temporary

    # Export Data

    return col