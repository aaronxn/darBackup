# darBackup (Français)
Dar incremental backup for Windows and Linux

Instructions:
  - Installez Python 3 et Dar (http://dar.linux.free.fr/)
  - Pour Windows, editez sauvegardeComplet.cmd et sauvegardeDiff.cmd.
  Pour Linux, éditez les fichiers sauvegardeComplet.sh et sauvegardeDiff.sh
  Ces scriptes contiennent plusieurs appels à des script Python.
  Les scripts ont 3 paramètres:
    - Le premier est la répertoire source à sauvegarder (Pour Window, il doit être en notation Cygwin, pour Linux en notation normale, ex : /home/user/Documents/)
    - Le second est le dossier cible de la sauvegarde, où les archives vont être créées (Pour Window, il doit être en notation Cygwin, pour Linux en notation normale)
    - Troisième, le répertoire cible de la sauvegarde en notation normale
    Note, pour Linux, les deux derniers paramètres sont les mêmes
    
Concernant la notation Cygwin:
  Dar (Disk ARchiver) est un outils pour Linux. Il existe une version Windows qui s'exécute grâce à Cygwin, un émulateur de systèmes Unix pour Windows.
  La notation normale pour un dossier Windows est la suivante: C:\Users\User1\Documents
  Son équivalent en notation Cygwin remplaces les backslash ("\") with slash ("/") and drives like "C:\" with /cygdrive/c/

Configuration for Window:
  Use the Windows task scheduler to planify execution of both cmd files.
  I configure Windows to execute sauvegardeComplet.cmd every two monthes and sauvegardeDiff.cmd every week.
  Make sure sauvegardeComplet has been executed at least once before launching the differencial backup.
  
Configuration for Linux:
  About the same except, you use cron to planify execution.
  *.sh files are for Linux.


# darBackup (English)
Dar incremental backup for Windows and Linux

Instruction:
  - Install Python 3 and Dar (http://dar.linux.free.fr/)
  - For Windows edit sauvegardeComplet.cmd and sauvegardeDiff.cmd files and
  for Linux, edit the files sauvegardeComplet.sh and sauvegardeDiff.sh
  these files contains several calls to Python scripts.
  The scripts have three parameters:
    - First is the source directory to backup (for Window, it must be written in Cygwin notation, under Linux, in normal notation, ex : /home/user/Documents/)
    - Second is the target directory where the archive will be saved (in Cygwin notation for Windows, under Linux in normal notation)
    - Third, the target directory in normal notation
    Note, for Linux, Second an Third parameters are the same.
    
About the Cygwin notation:
  Dar (Disk ARchiver) is a Linux tool, it executes under Windows thanks to Cygwin which is an emulator of Unix-like system for Windows.
  Usual Windows notation for directories is somethink like: C:\Users\User1\Documents
  The equivalent notation for Cygwin replaces backslash ("\") with slash ("/") and drives like "C:\" with /cygdrive/c/

Configuration for Window:
  Use the Windows task scheduler to planify execution of both cmd files.
  I configure Windows to execute sauvegardeComplet.cmd every two monthes and sauvegardeDiff.cmd every week.
  Make sure sauvegardeComplet has been executed at least once before launching the differencial backup.
  
Configuration for Linux:
  About the same except, you use cron to planify execution.
  *.sh files are for Linux.
