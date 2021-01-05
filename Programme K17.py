# ----- Importation des modules -----

import LZW
import ASK
import matplotlib.pyplot as plt
import soundfile as sf

# -----------------------------------

filename = input("Entrez le nom du fichier à convertir (avec l'extension)\n>>> ")
file = open(filename, "r")     # on ouvre le fichier dans file
content = file.read()      # on récupère le contenu du fichier dans content

print("\nCompression des données ...")
encodedData = LZW.compression(content)

f = int(input("\nEntrez la fréquence de la porteuse\n>>> "))
bps = int(input("\nEntrez la vitesse de l'information (nombre de bits transmis par seconde)\n>>> "))

print("\nModulation des données ...")
signal = ASK.Modulation(encodedData, f, bps)

plt.plot(signal)
plt.xlabel("Nombre d'echantillons du signal")
plt.ylabel("Amplitude $x(t)$")
plt.title("Apercu du signal", fontsize = 14)
plt.show()

print("Création du fichier audio 'signal.wav' ...")
sf.write("signal.wav", signal, 44100)

input("Fichier audio créé.\n\nPour quitter, appuyez sur entré.")