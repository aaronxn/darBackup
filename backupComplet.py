import time
import os, subprocess, sys

if len(sys.argv) < 3:
    print("Usage:")
    print("\t python "+sys.argv[0]+" REP_A_SAUVER_CYG REP_DESTINATION_CYG REP_DESTINATION")
    print("\t /!\\ REP_A_SAUVER_CYG et REP_DESTINATION_CYG doivent etre en notation Cygwin.")
    print("\t REP_DESTINATION est un nom de repertoir windows standard.")
    print("\t La notation Cygwin commencant par /cygdrive/c/ pour le disque C:\\.")
    print("\t La notation standard est C:\\mon_rep\\mon_rep2\\.")
    exit(-1)
    
pathCyg = sys.argv[1]
targetPathCyg = sys.argv[2]
targetPath = sys.argv[3]

date = time.strftime("%Y%m%d")

lastBackup = ""
if len(os.listdir(targetPath)) > 0:
    lastBackupFile = os.listdir(targetPath)[-1]
    lastBackup = lastBackupFile.split(".")[0]


print("Dossier a sauvegarder: "+pathCyg)
print("Dossier cible: "+targetPathCyg)
print("Derniere sauvegarde: " + lastBackup)
print("Date courante: " + date)

cmd="dar -c "+targetPathCyg+date+"_backup -R "+pathCyg+" -z -m200 -Z \"*.zip\" -Z \"*.png\" -s 2G"
print(cmd)

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for line in p.stdout.readlines():
    print(line)
for line in p.stderr.readlines():
    print(line)
retval = p.wait()
