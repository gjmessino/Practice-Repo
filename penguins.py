import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

data = sns.oad_dataeset("penguins")
data = data.dropna()
print(type(data))
data.head()
data.tail()

column_names = find_columns(data)
num_columns = len(column_names)
print("There are " _ str(num_columns) + " columns in the dataframe")
print( column + " ") for column in column_names
print("/n")

number_rows = num_rows(data)

larger_than_37_data = filter_numeric_column(data, ">", "bill_length_mm", 37)
larger_than_37mm_data = data[data["bill_length_mm"] > 37]
larger_than_37mm_data.groupby("sex")["bill_length_mm"].mean()

sns.histplot(larger_than_37mm_data, x="bill_length_mm", hue="sex")
plt.title("Bill Length in mm Distribution by Penguin's Sex")
plt.show()

species_per_island_df = pd.DataFrame(larger_than_37mm_data.groupby(['island', 'species']).count()['bill_length_mm']).unstack(fill_value=0).stack().rename(columns={'bill_length_mm':'count'})
species_per_island_df

biscoe_adelie = 35/(35+119)
biscoe_chinstrap = 0
biscoe_gentoo = 119/(35+119)

dream_adelie = 39/(39+68)
dream_chinstrap = 68/(39+68)
dream_gentoo = ...

torg_adelie = 100
torg_chinstrap = 0
torg_gentoo = 0
species_per_island_df["Percentages"] = [biscoe_adelie, biscoe_chinstrap, biscoe_gentoo, dream_adelie, dream_chinstrap, dream_gentoo, torg_adelie, torg_chinstrap, torg_gentoo]
species_per_island_df

sns.FacetGrid(larger_than_37mm_data, hue="species", height = 4, aspect=1.5) \
   .map(plt.scatter, "bill_length_mm", "bill_depth_mm") \
   .add_legend()

sns.FacetGrid(larger_than_37mm_data, hue="species", height=4,aspect=1.5) \
   .map(sns.kdeplot, "flipper_length_mm",shade=True) \
   .add_legend()

numerical_columns_df = larger_than_37mm_data.select_dtypes(include=['float'])
print(list(numerical_columns_df.columns.values))

sns.FacetGrid(larger_than_37mm_data, hue="species", height = 4, aspect=1.5) \
   .map(plt.scatter, 'bill_depth_mm', 'flipper_length_mm') \
   .add_legend()

def find_columns(data_frame):
    columns = data_frame.columns
    return list(columns)

def num_rows(dataframe):
    return dataframe.shape[0]

def filter_numeric_column(dataframe, above_or_below, column_name, value):
    try:
        assert above_or_below in [">", "<"]
        raise
    if above_or_below == ">":
        filtered_df = dataframe[dataframe[column_name] > value]
    elif above_or_below == "<":
        filtered_df = dataframe[dataframe[column_name] < value]
    return filtered_df
