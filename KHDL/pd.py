import pandas as pd

TT = pd.Series([1, 2, 3], index=[8,9,10])
MSV = pd.Series(['102190', '102191', '102192'], index=[8,9,10])
HoTen = pd.Series({8: 'a', 9: 'b', 10: 'c'})
df = pd.DataFrame({'STT': TT, 'MSV': MSV, 'Ten': HoTen})
# print(df['Ten'])
print(df.columns)