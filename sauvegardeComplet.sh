#!/bin/bash
mkdir ~/backups/docs/
mkdir ~/backups/Pictures/
mkdir ~/backups/Documents/
mkdir ~/backups/public_html/
python backupComplet.py ~/docs/ ~/backups/docs/ ~/backups/docs/
python backupComplet.py ~/Pictures/ ~/backups/Pictures/ ~/backups/Pictures/
python backupComplet.py ~/Documents/ ~/backups/Documents/ ~/backups/Documents/
python backupComplet.py ~/public_html/ ~/backups/public_html/ ~/backups/public_html/
