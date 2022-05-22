import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = ['Sydney', 'Vienna', 'Baku', 'Algeria', 'Buenos Aires', 'Yerevan', 'Minsk', 'Brussels', 'Sofia', 'Sao Paulo',
     'Rio de Janeiro', 'Porto Alegre', 'Recife Belo Horizonte', 'Brasilia', 'Fortaleza', 'El Salvador', 'London',
     'London', 'Glasgow', 'Newcastle upon Tyne', 'Sunderland', 'Budapest', 'Valencia', 'Caracas', 'Los Teces',
     'Caracas', 'Los Teces', 'Maracaibo', 'Hanoi', 'Berlin', 'Hamburg', 'Munich', 'Nuremberg', 'Athens', 'Tbilisi',
     'Copenhagen', 'Santo Domingo', 'Cairo', 'Calcutta', 'Delhi', 'Bangalore', 'Gurgaon', 'Mumbai', 'Jaipur', 'Chennai',
     'Cochin', 'Lucknow', 'Hyderabad', 'Noida', 'Ahmedabad', 'Gandhinagar', 'Nagpur', 'Jakarta', 'Tehran', 'Mashhad',
     'Shiraz', 'Tabriz', 'Isfahan', 'Madrid', 'Barcelona', 'Valencia', 'Bilbao', 'Palm', 'Seville', 'Rome', 'Milan',
     'Genoa', 'Naples', 'Catania', 'Turin', 'Brescia', 'Almaty', 'Toronto', 'Montreal', 'Vancouver', 'Doha', 'Beijing',
     'Hong Kong', 'Tianjin', 'Shanghai', 'Guangzhou', 'Dalian', 'Shenzhen', 'Wuhan', 'Nanking', 'Chongqing', 'Shenyang',
     'Chengdu', 'Foshan', 'Changchun', 'Xian', 'Kunming', 'Suzhou', 'Hangzhou', 'Harbin', 'Zhengzhou', 'Changsha',
     'Ningbo', 'Wuxi', 'Nanchang', 'Qingdao', 'Dongguan', 'Fuzhou', 'Hefei', 'Nanning', 'Guiyang', 'Shijiazhuang',
     'Xiamen', 'Urumqi', 'Wenzhou', 'Jinan', 'Lanzhou', 'Changzhou', 'Xuzhou', 'Macau', 'Hohhot', 'Shaosin', 'Luoyang',
     'Taipei', 'Kaohsiung', 'Taoyuan', 'Taichung', 'Medellin', 'Pyongyang', 'Lahore', 'Seoul', 'Busan', 'Daegu',
     'Incheon', 'Gwangju', 'Daejeon', 'Kuala Lumpur', 'Mexico City', 'Monterrey', 'Rotterdam', 'Amsterdam', 'Oslo',
     'Dubai', 'Panama', 'Lima', 'Callao', 'Warsaw', 'Lisbon', 'San', 'Juan', 'Moscow', 'Saint Petersburg',
     'Nizhny Novgorod', 'Novosibirsk', 'Samara', 'Ekaterinburg', 'Kazan', 'Bucharest', 'Mecca', 'Chicago', 'Boston',
     'New', 'York', 'Philadelphia', 'Cleveland', 'San Francisco', 'Washington', 'Atlanta', 'Baltimore', 'Miami',
     'Los Angeles', 'Singapore', 'Bangkok', 'Istanbul', 'Ankara', 'Izmir', 'Bursa', 'Adana', 'Tashkent', 'Kiev',
     'Kharkov', 'Dnieper', 'Manila', 'Helsinki', 'Paris', 'Topsail', 'Lyon', 'Lille', 'Toulouse', 'Wren', 'Prague',
     'Santiago', 'Lausanne', 'Stockholm', 'Tokyo', 'Osaka', 'Nagoya', 'Sapporo', 'Yokohama', 'Kobe', 'Kyoto', 'Fukuoka',
     'Sendai ', 'Hiroshima']
data = pd.read_csv('URAAAAA_right.csv', sep=";")
reservours_and_g = []
n_resevours_and_g = []
resevours_and_n_g = []
n_resevours_and_n_g = []
vodnik = data._get_column_array(0)
zemla = data._get_column_array(1)
for i in range(0, len(a)):
    if vodnik[i] == 1 and zemla[i] == 1:
        reservours_and_g.append([a[i], i])
    elif vodnik[i] == 0 and zemla[i] == 1:
        n_resevours_and_g.append([a[i], i])
    elif vodnik[i] == 1 and zemla[i] == 0:
        resevours_and_n_g.append([a[i], i])
    elif vodnik[i] == 0 and zemla[i] == 0:
        n_resevours_and_n_g.append([a[i], i])
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
        resevours_p.append(data1["Population"][i[1]])
    else:
        resevours_p.append(data1["Population"].mean())
    if strnow2.isdigit():
        resevours_s.append(data1["Stations"][i[1]])
    else:
        resevours_s.append(data1["Stations"].mean())
x = np.array(resevours_p)
y = np.array(resevours_s)
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