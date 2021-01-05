import ASK
import LZW
import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal


filename = input("Entrez le nom du fichier à analyser (avec l'extension)\n>>> ")
bps = int(input("\nEntrez la vitesse de l'information (nombre de bits transmis par seconde)\n>>> "))

print("\nFiltrage du signal ...")
data, Fe = sf.read(filename)   # on enregistre les données du fichier dans 'data' et la fréquence d'échantillonnage du fichier dans 'Fe'


# ----- Création du graphique de l'enregistrement d'origine -----

plt.plot(data)
plt.grid()
plt.xlabel("Nombre d'echantillons du signal")
plt.ylabel("Amplitude $x(t)$")
plt.title("Signal d'origine", fontsize = 14)
plt.show()

# -----------------------------------------------------------------


f1 = 19000   # limite basse du filtre
f2 = 21000   # limite haute du filtre


# -------------------------------------------------------------------- Application du filtre passe bande ----------------------------------------------------------------------------------

filtrePasseBande = signal.firwin(101, cutoff = [f1, f2], fs = Fe, pass_zero = False)   # création du filtre passe bande entre 'f1' et 'f2' pour une fréquence d'échantillonnage 'Fe'
data = signal.lfilter(filtrePasseBande, [1.0], data)   # Application du filtre 'filtrePasseBande' sur les données 'data' du fichier

sf.write("filtré.wav", data, Fe)   # Création d'un nouveau fichier audio .wav avec les nouvelles données filtrées 'data' et la fréquence d'échantillonnage 'Fe'

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


filename = "filtré.wav"   # nom de fichier audio filtré
data, Fe = sf.read(filename)   # on enregistre les données du fichier dans 'data' et la fréquence d'échantillonnage du fichier dans 'Fe'


# ----- Création du graphique de l'enregistrement filtré -----

plt.plot(data)
plt.grid()
plt.xlabel("Nombre d'échantillons du signal")
plt.ylabel("Amplitude $x(t)$")
plt.title("Signal filtré", fontsize = 14)
plt.show()

# ------------------------------------------------------------

print("Démodulation des données ...")
data = ASK.Demodulation(filename, bps)

print("Décompression des données ...")
decodedData = LZW.decompression(data)

print("\nDonées du fichier :\n\n{}".format(decodedData))

input("\n\nPour quitter, appuyez sur entré.")