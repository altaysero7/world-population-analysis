import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# Data set source: https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset?resource=download

# Read Data
data = pd.read_csv('world_population.csv')
print(data.head(100))

data.drop(columns=["Rank", "CCA3", "Capital"], inplace=True)

cols = data.columns
for col in range(2, 10):  # renaming columns
    data.rename({cols[col]: cols[col].split(" ")[0]}, axis=1, inplace=True)
data.head()

# plot a line chart with custom axes face color
figure, ax = plt.subplots(figsize=(15, 5))
growth = data.iloc[:, 2:10].sum()[::-1]
ax.plot(growth.index, growth.values, marker="o",
        markerfacecolor="red", markeredgewidth=1.5, markeredgecolor="black", markersize=10, color='black', linestyle='-', linewidth=2)
# set axis titles
ax.set_xlabel("Year")
ax.set_ylabel("Population")
# set chart title
ax.set_title("World Population Growth since 1970",
             fontsize=20, fontweight="bold")
# set axes facecolor
ax.set_facecolor("white")
plt.grid(color='navy', linestyle='--', linewidth=1)
plt.show()

# World Population Percentage of Top 10 countries
population = data.sort_values(
    by="World Population Percentage", ascending=False).head(10)
plt.figure(figsize=(10, 10))
x = population["Country"]
y = population["World Population Percentage"]
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title("World Population Percentage of Top 10 countries",fontsize=20, fontweight="bold")
plt.show()

# Below code is edited from the original code (Original code: https://www.kaggle.com/code/mustafacakir/world-population-analysis)
biggest10 = data.sort_values('2022', ascending=False).head(10)
biggest10 = biggest10.melt(id_vars=['Country', 'Area (km²)'],
                           value_vars=['1970', '1980', '1990',
                                       '2000', '2010', '2020', '2022'],
                           var_name='Year', value_name='Population')
biggest10['Space'] = (biggest10['Area (km²)'] /
                      biggest10['Population']) * 1000000
print(biggest10.head())

figure = px.line(biggest10, x='Year', y='Population', color='Country', markers=True,
                 title='Top 10 Countries with Biggest Population Growth between 1970-2020',
                 template="plotly_dark")
figure.update_layout(plot_bgcolor="#23262F",
                     title={'x': 0.5},
                     font={"family": "courier"})
figure.show()

# Below code is edited from the original code (Original code: https://www.kaggle.com/code/nanduvardhanreddy/world-population-analysis)
figure = px.choropleth(data,
                       locations='Country',
                       locationmode='country names',
                       color='2022',
                       hover_name='Country',
                       template='seaborn',
                       title='World Population per Country in 2022')
figure.show()
