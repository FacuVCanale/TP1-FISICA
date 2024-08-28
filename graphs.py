import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


DISTANCIA_INICIAL = 56

# Create a DataFrame from the CSV data
datos_calibracion = {
    "Distancia (cm)": [50.0, 45.0, 40.0, 35.0, 30.0, 25.0, 20.0, 15.0, 13.2],
    "Valor del sensor": [365, 697, 987, 1227, 1718, 1763, 2087, 2300, 2473],
    "Error": [0, 1, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(datos_calibracion)

# datos_calibrados = pd.read_csv('calibracion.csv')
# datos_calibrados['Distancia (cm)'] = 56 - datos_calibrados['Distancia (cm)']
# Asegurarse de que 'Distancia (cm)' sea una serie de pandas
if isinstance(datos_calibracion['Distancia (cm)'], list):
    datos_calibracion['Distancia (cm)'] = pd.Series(datos_calibracion['Distancia (cm)'])

# Realizar la operación de resta
datos_calibracion['Distancia (cm)'] = DISTANCIA_INICIAL - datos_calibracion['Distancia (cm)']
fitted_lines_for_data = stats.linregress(datos_calibracion['Distancia (cm)'], datos_calibracion['Valor del sensor'])


plt.errorbar(datos_calibracion['Distancia (cm)'], datos_calibracion["Valor del sensor"], yerr=datos_calibracion["Error"], fmt='o', ecolor='r', capsize=5)
plt.plot(datos_calibracion['Distancia (cm)'], datos_calibracion['Distancia (cm)']*fitted_lines_for_data.slope + fitted_lines_for_data.intercept, 'r')
plt.xlabel('Distancia (cm)')
plt.ylabel('Valor del sensor')
plt.title('Calibración del sensor')
plt.show()