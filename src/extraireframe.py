import subprocess
import json
import os

# Chemin de la vidéo
video_path = "/home/serine/datos/Week30_2018-10-04/2018-10-04-11-28-13_Dataset_year-A3.h264"
output_dir = "frames_extracted"

# S'assurer que le dossier existe
os.makedirs(output_dir, exist_ok=True)

# Obtenir des informations détaillées sur le fichier
try:
    cmd = f'ffprobe -v error -show_entries format=duration -show_streams -of json "{video_path}"'
    result = subprocess.check_output(cmd, shell=True)
    info = json.loads(result)
    print("Informations sur le fichier:")
    print(json.dumps(info, indent=2))
    
    # Essayer d'extraire plus de frames avec un intervalle plus court
    cmd = f'ffmpeg -i "{video_path}" -vf "select=not(mod(n\,10))" -vsync vfr "{output_dir}/frame_%04d.jpg"'
    print("Extraction d'une frame toutes les 10 frames...")
    subprocess.call(cmd, shell=True)
    
    # Vérifier le nombre de frames extraites
    frames = [f for f in os.listdir(output_dir) if f.endswith('.jpg')]
    print(f"Nombre de frames extraites: {len(frames)}")
    
except Exception as e:
    print(f"Erreur: {e}")
    
    # Essayons une méthode plus basique si la précédente échoue
    print("Tentative avec une méthode alternative...")
    cmd = f'ffmpeg -i "{video_path}" "{output_dir}/frame_%04d.jpg"'
    subprocess.call(cmd, shell=True)
    
    # Vérifier à nouveau
    frames = [f for f in os.listdir(output_dir) if f.endswith('.jpg')]
    print(f"Nombre de frames extraites avec la méthode alternative: {len(frames)}")
    