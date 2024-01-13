import pandas as pd
import re
import matplotlib.pyplot as plt


def dynamic_by_year():
    year_salary = {}
    year_count = {}
    for year in year_normal:
        if year in years:
            year_salary[int(year)] = round(data_grp.get_group(year)['salary_mean'].mean())
            year_count[int(year)] = len(data_grp.get_group(year))
        else:
            year_salary[int(year)] = 0
            year_count[int(year)] = 0
    return year_salary, year_count


def dynamic_by_vac():
    year_salary_vac = {}
    year_count_vac = {}
    for year in year_normal:
        if year in years:
            year_salary_vac[int(year)] = round(data_vac_grp.get_group(year)['salary_mean'].mean())
            year_count_vac[int(year)] = len(data_vac_grp.get_group(year))
        else:
            year_salary_vac[int(year)] = 0
            year_count_vac[int(year)] = 0
    return year_salary_vac, year_count_vac


def df_area_data():
    percent = len(filtered_df)

    year_area_vac = {}
    year_area_vac_percent = {}
    for area in areas:
        year_area_vac[area] = round(filtered_df_group.get_group(area)['salary_mean'].mean())
        year_area_vac_percent[area] = round(len(filtered_df_group.get_group(area)) / percent * 100, 2)
    return year_area_vac, year_area_vac_percent


def sort_area_data(area_salary, area_count):
    count_vacancies = sum(area_count.values())
    len_area = list(area_count.keys())

    for k in len_area:
        if area_count[k] <= count_vacancies / 100:
            del area_count[k]
            del area_salary[k]

    area_salary = {k: v for k, v in sorted(area_salary.items(), key=lambda kv: (-kv[1], kv[0]))}
    year_area_vac_s = {k: area_salary[k] for k in list(area_salary)[:10]}
    year_area_vac_s = {k: v for k, v in sorted(year_area_vac_s.items(), key=lambda kv: (-kv[1], kv[0]))}

    area_count = {k: v for k, v in sorted(area_count.items(), key=lambda kv: (-kv[1], kv[0]))}
    year_area_vac_per_s = {k: area_count[k] for k in list(area_count)[:10]}
    year_area_vac_per_s = {k: v for k, v in sorted(year_area_vac_per_s.items(), key=lambda kv: (-kv[1], kv[0]))}

    return year_area_vac_s, year_area_vac_per_s


def create_plot():
    fig, sub = plt.subplots(2, 2)
    years = [2007 + i for i in range(16)]
    width = 0.4
    sub[0, 0].bar([x - width / 2 for x in years], year_salary.values(), width, label='средняя з/п')
    sub[0, 0].bar([x + width / 2 for x in years], vacancy_salary.values(), width, label=f'з/п {vac_name}')
    sub[0, 0].set_title('Уровень зарплат по годам')

    sub[0, 0].set_xticks(years)
    sub[0, 0].set_xticklabels(years, rotation=90, size=8)

    sub[0, 0].set_yticks(range(20000, max(max(year_salary.values()), max(vacancy_salary.values())), 20000))
    sub[0, 0].set_yticklabels(range(20000, max(max(year_salary.values()), max(vacancy_salary.values())), 20000),
                              fontsize=8)
    sub[0, 0].set_axisbelow(True)
    sub[0, 0].yaxis.grid(color='gray')

    sub[0, 0].legend(loc=2, fontsize=8)

    width = 0.4
    sub[0, 1].bar([x - width / 2 for x in years], vacancy_all_count.values(), width, label='Количество вакансий')
    sub[0, 1].bar([x + width / 2 for x in years], vacancy_count_choice.values(), width,
                  label=f'Количество вакансий {vac_name}')
    sub[0, 1].set_title('Количество вакансий по годам')

    sub[0, 1].set_xticks(years)
    sub[0, 1].set_xticklabels(years, rotation=90, size=8)

    sub[0, 1].set_yticks(range(200, max(max(vacancy_all_count.values()), max(vacancy_count_choice.values())), 200))
    sub[0, 1].set_yticklabels(range(200, max(max(vacancy_all_count.values()), max(vacancy_count_choice.values())), 200),
                              fontsize=8)
    sub[0, 1].set_axisbelow(True)
    sub[0, 1].yaxis.grid(color='gray')

    sub[0, 1].legend(loc=2, fontsize=8)

    width = 0.4
    cities = [x.replace(' ', '\n') if ' ' in x else x for x in list(area_salary_s.keys())]
    cities = [x.replace('-', '-\n') if '-' in x else x for x in cities]
    sub[1, 0].barh(cities, area_salary_s.values(), width)
    sub[1, 0].invert_yaxis()
    sub[1, 0].set_title('Уровень зарплат по городам')
    sub[1, 0].set_yticks(cities)
    sub[1, 0].set_yticklabels(cities, size=6, ha='right', va='center')

    sub[1, 0].set_xticks(range(20000, max(area_salary_s.values()), 20000))
    sub[1, 0].set_xticklabels(range(20000, max(area_salary_s.values()), 20000), size=8)
    sub[1, 0].set_axisbelow(True)
    sub[1, 0].xaxis.grid(color='gray')

    area_data = list(area_count_s.values())
    area_data = [100 - sum(area_count_s.values())] + area_data
    vals = area_data
    labels = ['Другие'] + list(area_count_s.keys())
    sub[1, 1].pie(vals, labels=labels, textprops={'fontsize': 6})
    sub[1, 1].set_title('Доля вакансий по городам')

    return sub


vacancies = pd.read_csv('vacancies.csv',
                        names=['name', 'salary_from', 'salary_to', 'salary_currency', 'area_name', 'published_at'])
vac_name = input()

count_vacancies = len(vacancies)

df = vacancies
filtered_df = df.loc[df['salary_currency'] == 'RUR']

areas = filtered_df['area_name'].unique()
areas = sorted(areas)

filtered_df.insert(2, "salary_mean", (filtered_df['salary_from'] + filtered_df['salary_to']) / 2, True)
filtered_df.insert(7, "year", filtered_df.apply(lambda row: row.published_at.split('-')[0], axis=1), True)

years = filtered_df['year'].unique()
year_normal = [str(x) for x in range(2007, 2023)]

data_grp = filtered_df.groupby(['year'])
data_grp.first()

year_salary, year_count = dynamic_by_year()
vacancy_all_count = year_count

filtered_df_group = filtered_df.groupby(['area_name'])
year_area_vac, year_area_vac_percent = df_area_data()

year_area_s, year_area_per_s = sort_area_data(year_area_vac, year_area_vac_percent)
area_salary_s = year_area_s
area_count_s = year_area_per_s

df_vac = filtered_df[filtered_df['name'].str.contains(vac_name, flags=re.IGNORECASE, regex=True)]
data_vac_grp = df_vac.groupby(['year'])
years = df_vac['year'].unique()

year_salary_vac, year_count_vac = dynamic_by_vac()
vacancy_salary = year_salary_vac
vacancy_count_choice = year_count_vac

create_plot()
