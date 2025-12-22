@echo off
title Git Commit Retrodate - LaFormePasLesFormes
color 0A
cls

echo ========================================
echo  GIT COMMIT RETRODATE - STREAK FIX
echo ========================================
echo.
echo Ce script cree un commit retrodater 
echo et NETTOIE les variables apres usage.
echo.
echo Ton repo: %CD%
echo.

:ask_date
set /p DATE="Date du commit (ex: 2025-12-21 12:00:00 +0100) ? > "
if "%DATE%"=="" goto ask_date

:ask_message
set /p MSG="Message du commit ? > "
if "%MSG%"=="" set MSG="Commit retrodater: %DATE%"

echo.
echo ========================================
echo  VERIFICATION AVANT COMMIT
echo ========================================
echo Date forcee : %DATE%
echo Message     : %MSG%
echo.
echo Continuer ? (O/N)
choice /c ON /m " "
if errorlevel 2 goto end

echo.
echo [1/5] git status
git status
echo.

echo [2/5] git add .
git add .
echo.

echo [3/5] Definition dates: %DATE%
set GIT_AUTHOR_DATE=%DATE%
set GIT_COMMITTER_DATE=%DATE%
echo.

echo [4/5] git commit -m "%MSG%"
git commit -m "%MSG%"
echo.

echo [5/5] git push origin main
git push origin main
echo.

echo ========================================
echo  SUCCES ! Commit pousse sur GitHub
echo ========================================
echo.
echo VERIFICATION DATES:
git log -1 --pretty=fuller
echo.
echo NETTOYAGE VARIABLES (prochains commits = date normale):
set GIT_AUTHOR_DATE=
set GIT_COMMITTER_DATE=
echo Variables supprimees ! ^ OK
echo.
echo Ton streak GitHub se mettra a jour dans 5min.
echo Rafraichis https://github.com/Punkyherisson
echo.

:end
pause