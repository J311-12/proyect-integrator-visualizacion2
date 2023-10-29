import matplotlib.pyplot as plt
import pandas as pd

# Cargando los datos
df = pd.read_csv("datos_limpios.csv")

# Creando un subplots de 2x2
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Graficando las distribuciones de anémicos, diabéticos, fumadores y muertos
axs[0, 0].pie(df["anemia"].value_counts(), labels=["No", "Si"], autopct="%1.1f%%")
axs[0, 1].pie(df["diabetes"].value_counts(), labels=["No", "Si"], autopct="%1.1f%%")
axs[1, 0].pie(df["smoking"].value_counts(), labels=["No", "Si"], autopct="%1.1f%%")
axs[1, 1].pie(df["is_dead"].value_counts(), labels=["No", "Si"], autopct="%1.1f%%")

# Definiendo los títulos de las gráficas
axs[0, 0].set_title("Anémicos")
axs[0, 1].set_title("Diabéticos")
axs[1, 0].set_title("Fumadores")
axs[1, 1].set_title("Muertos")

# Mostrando las gráficas
plt.show()
