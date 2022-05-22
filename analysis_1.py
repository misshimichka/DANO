import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = ['Sydney', 'Vienna', 'Baku', 'Algiers', 'Buenos Aires', 'Yerevan', 'Minsk', 'Brussels', 'Sofia', 'Sao Paulo',
     'Rio de Janeiro', 'Porto Alegre', 'Brasilia', 'Fortaleza', 'Salvador', 'London',
     'London', 'Glasgow', 'Budapest', 'Valencia', 'Caracas',
     'Caracas', 'Berlin', 'Hamburg', 'Munich', 'Nuremberg', 'Athens', 'Tbilisi',
     'Copenhagen', 'Santo Domingo', 'Cairo', 'Delhi', 'Bangalore', 'Mumbai', 'Tehran', 'Madrid', 'Barcelona',
     'Valencia', 'Seville', 'Rome', 'Milan',
     'Genoa', 'Naples', 'Catania', 'Turin', 'Toronto', 'Montreal', 'Vancouver', 'Beijing',
     'Hong Kong', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Wuhan', 'Chongqing', 'Shenyang', 'Seoul', 'Busan', 'Daegu',
     'Incheon', 'Gwangju', 'Daejeon', 'Kuala Lumpur', 'Mexico City', 'Monterrey', 'Rotterdam', 'Amsterdam', 'Oslo',
     'Dubai', 'Lima', 'Warsaw', 'Lisbon', 'Moscow', 'Saint Petersburg',
     'Nizhny Novgorod', 'Novosibirsk', 'Samara', 'Bucharest', 'Chicago', 'Boston',
     'New York', 'Philadelphia', 'Cleveland', 'San Francisco', 'Washington', 'Atlanta', 'Baltimore', 'Miami',
     'Los Angeles', 'Singapore', 'Bangkok', 'Istanbul', 'Ankara', 'Tashkent', 'Kiev',
     'Manila', 'Helsinki', 'Paris', 'Lyon', 'Lille', 'Toulouse', 'Prague',
     'Santiago', 'Lausanne', 'Stockholm', 'Tokyo', 'Osaka', 'Hiroshima']
data = pd.read_csv('URAAAAA_right.csv', sep=";")
data1 = pd.read_csv('hack_data.csv')
reservours_and_g = []

mapa = dict()

check = list(data1.iloc[:, 1])
for i in range(len(check)):
    check[i] = check[i][1::]
print(check)
# нулевое значение - инлекс в А, первое - индекс строки в дата 1
for i in a:
    mapa[i] = [a.index(i), check.index(i)]

n_resevours_and_g = []
resevours_and_n_g = []
n_resevours_and_n_g = []
vodnik = data._get_column_array(0)
zemla = data._get_column_array(1)
for i in range(0, len(mapa)):
    if vodnik[i] == 1 and zemla[i] == 1:
        reservours_and_g.append([mapa[a[i]][0], mapa[a[i]][1]])
    elif vodnik[i] == 0 and zemla[i] == 1:
        n_resevours_and_g.append([mapa[a[i]][0], mapa[a[i]][1]])
    elif vodnik[i] == 1 and zemla[i] == 0:
        resevours_and_n_g.append([mapa[a[i]][0], mapa[a[i]][1]])
    elif vodnik[i] == 0 and zemla[i] == 0:
        n_resevours_and_n_g.append([mapa[a[i]][0], mapa[a[i]][1]])
data1 = pd.read_csv('hack_data.csv')
resevours_p, resevours_s, n_resevours_p, n_resevours_s = [], [], [], []
n_resevours_and_g += n_resevours_and_n_g
reservours_and_g += resevours_and_n_g
for i in n_resevours_and_g:
    strnow = str(data1["Population"][i[1]]).replace(".", "")
    strnow2 = str(data1['Stations'][i[1]])
    if strnow.isdigit():
        n_resevours_p.append(data1["Population"][i[1]])
    else:
        n_resevours_p.append(data1["Population"].mean())
    if strnow2.isdigit():
        n_resevours_s.append(data1["Stations"][i[1]])
    else:
        n_resevours_s.append(data1["Stations"].mean())
for i in reservours_and_g:
    strnow = str(data1["Population"][i[1]]).replace(".", "")
    strnow2 = str(data1['Stations'][i[1]])
    if strnow.isdigit():
        if data1["Population"][i[1]] <= 9000000:
            resevours_p.append(data1["Population"][i[1]])
        else:
            resevours_p.append(data1["Population"].mean())
    else:
        resevours_p.append(data1["Population"].mean())
    if strnow2.isdigit():
        if data1['Stations'][i[1]] <= 350:
            resevours_s.append(data1["Stations"][i[1]])
        else:
            resevours_s.append(data1["Stations"].mean())
    else:
        resevours_s.append(data1["Stations"].mean())
x = np.array(resevours_p)
y = np.array(resevours_s)
print(resevours_s)
plt.scatter(x, y)
mean_x = x.mean()
mean_y = y.mean()
SS_xy = np.sum(y * x - mean_y * mean_x * x.size)
SS_xx = np.sum(x * x - mean_x * mean_x * x.size)
b1 = SS_xy / SS_xx
b0 = mean_y - b1 * mean_x
y_pred = b0 + b1 * x
r_om = np.corrcoef(x, y)
plt.plot(x, y_pred, color='g')
plt.show()
print(r_om)