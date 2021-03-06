import pandas as pd


class FinStatements:
    balance = None
    pnl = None
    capital_change = None
    funds_movement = None

    def __init__(self, excelfile):
        excel = pd.ExcelFile(excelfile)
        self.balance = pd.read_excel(excel, 'Balance')
        self.pnl = pd.read_excel(excel, 'Financial Result')
        self.capital_change = pd.read_excel(excel, 'Capital Change')
        self.funds_movement = pd.read_excel(excel, 'Funds Movement')

    def find_in(self, string_code, year, df=None, codes=0, years={}):
        if string_code // 1000 == 1:
            df = self.balance
            years = {2019: 16, 2018: 22, 2017: 28}
            codes = 13
        elif string_code // 1000 == 2:
            df = self.pnl
            years = {2019: 20, 2018: 27}
            codes = 15
        n = df.iloc[:, codes]
        year_column = years[year]
        index = n.index[list(n).index(str(string_code))]
        value = df.iloc[index, year_column]

        negative = -1 if value[0] == '(' or value[0] == '-' else 1
        try:
            value = int("".join([x for x in value if x.isdigit()]))
        except:
            value = 0
        return negative * value
