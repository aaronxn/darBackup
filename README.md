# darBackup
Dar incremental backup for Windows and Linux

Instruction:
  - Install Python 3 and Dar (http://dar.linux.free.fr/)
  - For Windows edit sauvegardeComplet.cmd and sauvegardeDiff.cmd files and
  for Linux, edit the files sauvegardeComplet.sh and sauvegardeDiff.sh
  these files contains several calls to Python scripts.
  The scripts have three parameters:
    - First is the source directory to backup (for Window, it must be written in Cygwin notation, under Linux, in normal notation)
    - Second is the target directory where the archive will be saved (in Cygwin notation for Windows, under Linux in normal notation)
    - Third, the target directory in normal notation
    Note, for Linux, Second an Third parameters are the same.
    
About the Cygwin notation:
  Dar is a Linux tool, it executes under Windows thanks to Cygwin which is an emulator of Unix-like system for Windows.
  Usual Windows notation for directories is somethink like: C:\Users\User1\Documents
  The equivalent notation for Cygwin replaces backslash ("\") with slash ("/") and drives like "C:\" with /cygdrive/c/

Configuration for Window:
  Use the Windows task scheduler to planify execution of both cmd files.
  I configure dba
