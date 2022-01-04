import pandas as pd
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt


file_train = pd.read_csv('train.csv', error_bad_lines=False)

file_train = file_train[file_train["total_vaccinations"].notna()]
vac_india = file_train[file_train["country"].str.contains("India")]
# file_train["country"].unique()

dates = vac_india['date'].apply(lambda x: np.array(x))
total = vac_india['total_vaccinations'].apply(lambda x: np.array(x))
plt.figure(1)
India = sns.lineplot(x=dates, y=total)

plt.yticks(
    India.get_yticks(),
    India.get_yticks() * 1
)
plt.xticks(
    rotation=90,
    horizontalalignment='right',
    fontweight='light',
    fontsize='8'
)

plt.show()

people = vac_india['daily_vaccinations_raw'].apply(lambda x: np.array(x))
plt.figure(2)
raw_india = sns.lineplot(x=dates, y=people)
plt.xticks(
    rotation=90
)

plt.show()

file_train = file_train[file_train["total_vaccinations"].notna()]
vac_uk = file_train[file_train["country"].str.contains("United Kingdom")]
dates = vac_uk['date'].apply(lambda x: np.array(x))
total = vac_uk['total_vaccinations'].apply(lambda x: np.array(x))
plt.figure(3)
UK = sns.lineplot(x=dates, y=total)
plt.yticks(

    UK.get_yticks(),
    UK.get_yticks() * 1
)
plt.xticks(
    rotation=90,
    horizontalalignment='right',
    fontweight='light',
    fontsize='7',

)

people = vac_uk['daily_vaccinations_raw'].apply(lambda x: np.array(x))
plt.figure(4)
raw_uk = sns.lineplot(x=dates, y=people)
plt.xticks(
    rotation=90
)

file_train = file_train[file_train["total_vaccinations"].notna()]
vac_us = file_train[file_train["country"].str.contains("United States")]
dates = vac_us['date'].apply(lambda x: np.array(x))
total = vac_us['total_vaccinations'].apply(lambda x: np.array(x))
plt.figure(5)
US = sns.lineplot(x=dates, y=total, data='details')
plt.yticks(

    US.get_yticks(),
    US.get_yticks() * 1
)

plt.xticks(
    rotation=90,
    horizontalalignment='right',
    fontweight='light',
    fontsize='7',

)

people = vac_us['daily_vaccinations_raw'].apply(lambda x: np.array(x)).notna()
plt.figure(6)
raw_us = sns.lineplot(x=dates, y=people)
plt.yticks(
    raw_us.get_yticks(),
    raw_us.get_yticks() * 100000,
    fontsize='10',
)
plt.xticks(
    rotation=90
)

file_train = file_train[file_train["total_vaccinations"].notna()]
vac_italy = file_train[file_train["country"].str.contains("Italy")]
dates = vac_italy['date'].apply(lambda x: np.array(x))
total = vac_italy['total_vaccinations'].apply(lambda x: np.array(x))
plt.figure(7)
italy = sns.lineplot(x=dates, y=total, data='details')
plt.yticks(

    italy.get_yticks(),
    italy.get_yticks() * 1
)
plt.xticks(
    rotation=90,
    horizontalalignment='right',
    fontweight='light',
    fontsize='7',

)


people = vac_italy['daily_vaccinations_raw'].apply(lambda x: np.array(x)).notna()
plt.figure(8)
raw_ita = sns.lineplot(x=dates, y=people)
plt.yticks(
    raw_ita.get_yticks(),
    raw_ita.get_yticks() * 100000,
    fontsize='10',
)
plt.xticks(
    rotation=90
)

file_train = file_train[file_train["total_vaccinations"].notna()]
vac_spain = file_train[file_train["country"].str.contains("Spain")]
dates = vac_spain['date'].apply(lambda x: np.array(x))
total = vac_spain['total_vaccinations'].apply(lambda x: np.array(x))
plt.figure(9)
spain = sns.lineplot(x=dates, y=total, data='details')
plt.yticks(

    spain.get_yticks(),
    spain.get_yticks() * 1
)
plt.xticks(
    rotation=90,
    horizontalalignment='right',
    fontweight='light',
    fontsize='7',

)


people = vac_spain['daily_vaccinations_raw'].apply(lambda x: np.array(x)).notna()
plt.figure(10)
raw_spa = sns.lineplot(x=dates, y=people)
plt.yticks(
    raw_spa.get_yticks(),
    raw_spa.get_yticks() * 100000,
    fontsize='10',
)
plt.xticks(
    rotation=90
)


file_train = file_train[file_train["total_vaccinations"].notna()]
vac_tur = file_train[file_train["country"].str.contains("Turkey")]
dates = vac_tur['date'].apply(lambda x: np.array(x))
total = vac_tur['total_vaccinations'].apply(lambda x: np.array(x))
plt.figure(11)
turkey = sns.lineplot(x=dates, y=total, data='details')
plt.yticks(

    turkey.get_yticks(),
    turkey.get_yticks() * 1
)
plt.xticks(
    rotation=90,
    fontsize='10',

)

people = vac_tur['daily_vaccinations_raw'].apply(lambda x: np.array(x))
plt.figure(12)
raw_tur = sns.lineplot(x=dates, y=people)
plt.xticks(
    rotation=90
)


file_train = file_train[file_train["total_vaccinations"].notna()]
vac_sri = file_train[file_train["country"].str.contains("Sri Lanka")]
dates = vac_sri['date'].apply(lambda x: np.array(x))
total = vac_sri['total_vaccinations'].apply(lambda x: np.array(x))
plt.figure(13)
srilanka = sns.lineplot(x=dates, y=total)
plt.yticks(

    srilanka.get_yticks(),
    srilanka.get_yticks() * 1
)
plt.xticks(
    rotation=90,
    horizontalalignment='right',
    fontweight='light',
    fontsize='7',

)


people = vac_sri['daily_vaccinations_raw'].apply(lambda x: np.array(x))
plt.figure(14)
raw_sri = sns.lineplot(x=dates, y=people)

plt.xticks(
    rotation=90
)

# sum of vaccines used 

# #file_train['vaccines'].unique()
file_train["vaccines"].apply(lambda x: np.array(x))
sum_pfizer = file_train['vaccines'].str.contains("Pfizer/BioNTech").sum()
sum_moderna = file_train['vaccines'].str.contains("Moderna").sum()
sum_oxford = file_train['vaccines'].str.contains("Oxford/AstraZeneca").sum()
sum_cnbg = file_train['vaccines'].str.contains("CNBG").sum()
sum_covaxin = file_train['vaccines'].str.contains("Covaxin").sum()
sum_sinopharm = file_train['vaccines'].str.contains("Sinopharm").sum()
sum_sinovac = file_train['vaccines'].str.contains("Sinovac").sum()
sum_sputnik = file_train['vaccines'].str.contains("Sputnik V").sum()

# function for making the piechart

def piechart():
    vaccines = ['Pfizer', 'Moderna', 'Oxford/AstraZeneca', 'CNBG', 'Covaxin', 'Sinopharm', 'Sinovac', 'Sputnik V']
    data = [sum_pfizer, sum_moderna, sum_oxford, sum_cnbg, sum_covaxin, sum_sinopharm, sum_sinovac, sum_sputnik]
    fig = plt.figure(figsize=(8, 8))
    plt.pie(data, labels=vaccines, rotatelabels=90)
    piechart = plt.show()
    return piechart
piechart()


# bar graph for country vaccination rate
sum = vac_india["total_vaccinations"].sum()
length = len(vac_india.index)
avg_ind = sum / length

vac_belgium = file_train[file_train["country"].str.contains("Belgium")]
sum = vac_belgium["total_vaccinations"].sum()
length = len(vac_belgium.index)
avg_bel = sum / length

vac_brazil = file_train[file_train["country"].str.contains("Brazil")]
sum = vac_brazil["total_vaccinations"].sum()
length = len(vac_brazil.index)
avg_braz = sum / length

vac_canada = file_train[file_train["country"].str.contains("Canada")]
sum = vac_canada["total_vaccinations"].sum()
length = len(vac_canada.index)
avg_can = sum / length

vac_italy = file_train[file_train["country"].str.contains("Italy")]
sum = vac_italy["total_vaccinations"].sum()
length = len(vac_canada.index)
avg_ita = sum / length

# vac_plot = pd.DataFrame(
#                 {"Average " : [avg_ind , avg_bel , avg_braz , avg_can , avg_ita]} ,
#                 index = ['India' , 'Belgium' , 'Brazil' , 'Canada' , 'Italy' ]
#         )
Average  =  [avg_ind , avg_bel , avg_braz , avg_can , avg_ita]
index = ['India' , 'Belgium' , 'Brazil' , 'Canada' , 'Italy' ]

plt.bar(index , Average )
plt.xlabel('countries', color = 'orange', fontsize='13', horizontalalignment='center')
plt.ylabel('Average vaccination rate', color = 'orange', fontsize='13', horizontalalignment='center')
plt.ylim(0,2000000)
plt.title("  y-axis scale : 0.25 = 500,000 vaccinations per day")
plt.show()
# vac_plot.plot(kind = "bar" )


#creating model for deployment

filename = 'finalmodel.sav'

pickle.dump(India, filename)
pickle.dump(raw_india, filename)
pickle.dump(US, filename)
pickle.dump(raw_us, filename)
pickle.dump(UK, filename)
pickle.dump(raw_uk, filename)
pickle.dump(italy, filename)
pickle.dump(raw_ita, filename)
pickle.dump(spain, filename)
pickle.dump(raw_spa, filename)
pickle.dump(turkey, filename)
pickle.dump(raw_tur, filename)
pickle.dump(srilanka, filename)
pickle.dump(raw_sri, filename)
pickle.dump(avg , filename)
