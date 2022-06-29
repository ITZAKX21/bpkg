import os, sys, time
from time import sleep
rst="\033[0m"
b="\033[1;30m"
r="\033[1;31m"
g="\033[1;32m"
yl="\033[1;33m"
bl="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
w="\033[1;37m"
def ani(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)
def logo ():
  os.system("clear")
  os.system("""echo '  ░█████╗░██╗░░██╗██╗░░██╗██╗░░░██╗░█████╗░██╗░░░██╗
  ██╔══██╗██║░██╔╝╚██╗██╔╝██║░░░██║██╔══██╗██║░░░██║
  ███████║█████═╝░░╚███╔╝░╚██╗░██╔╝███████║██║░░░██║
  ██╔══██║██╔═██╗░░██╔██╗░░╚████╔╝░██╔══██║██║░░░██║
  ██║░░██║██║░╚██╗██╔╝╚██╗░░╚██╔╝░░██║░░██║╚██████╔╝
  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░
----------------------------------------------------
  ╔════════════════════════════════════════════════╗
  ║            [✓] TOOL NAME : BPKG                ║
  ║            [✓] GITHUB : AKXVAU                 ║
  ║            [✓] FACEBOOK : AKX.THE.PSYCHO       ║
  ║            [✓] TELEGRAM : AKXVAU               ║
  ║            [✓] INSTAGRAM : AKXVAU              ║
  ║            [✓] EMAIL : ADMIN@ITZAKX.ML         ║
  ╚════════════════════════════════════════════════╝\n----------------------------------------------------'|lolcat""")
  ani(r+"\t<"+bl+"p"+r+">"+g+" MAKE GOOGLE YOUR BEST FRIEND :) "+r+"<"+bl+"/p"+r+">")
  os.system("echo '----------------------------------------------------'| lolcat")
  
logo ()
def main ():
  
  x = input("\t\033[1;30;40m[\033[1;34;40m+\033[1;30;40m]\033[1;32;40m PRESS ANY KEY FOR START\033[1;0;40m")
  logo ()
  os.system('''termux-setup-storage
yse | pkg update 
yes | yse | pkg upgrade 
yes | yse | pkg install python 
yse | pkg install python2 
pip3 install pip requests mechanize beautifulsoup4 infocircle myspeed 
pip2 install pip requests mechanize beautifulsoup4
pip install --upgrade pip
yse | pkg install fish 
yse | pkg i zsh 
yse | pkg install ruby 
yse | pkg install git 
yse | pkg install php 
yse | pkg install perl 
yse | pkg install nmap 
yse | pkg install bash 
yse | pkg install clang 
yse | pkg install nano 
yse | pkg install w3m 
yse | pkg install figlet 
yse | pkg install cowsay 
yse | pkg install curl 
yse | pkg install tar 
yse | pkg install zip 
yse | pkg install unzip 
yse | pkg install tor 
yse | pkg install wget 
yse | pkg install wireshark 
yse | pkg install wgetrc 
yse | pkg install wcalc 
yse | pkg install bmon 
yse | pkg install unrar 
yse | pkg install toilet 
yse | pkg install proot 
yse | pkg install net-tools 
yse | pkg install golang 
yse | pkg install chroot 
yse | pkg install macchanger 
yse | pkg install openssl 
yse | pkg install cmatrix 
yse | pkg install openssh 
yse | pkg install wireshark 
yse | pkg install macchanger 
yse | pkg install nano
yse | pkg install nmap
yse | pkg install clang
yse | pkg install bash
yse | pkg install proot
yes | pkg install vim
yse | pkg install net-tools''')
  print("\t\033[1;30;40m[\033[1;34 ;40m+\033[1;30;40m]\033[1;32;40m INSTALLED PKG SUCCESSFUL \033[1;0;40m")
  logo ()
  pkg = input("\t\033[1;30;40m[\033[1;34;40m+\033[1;30;40m]\033[1;32;40m SEE INSTALLED PKG [Y/N] : \033[1;39;40m")
  if pkg == "y" or pkg == "Y":
    os.system("pkg list-installed")
  else:
    sys.exit ()
if __name__=='__main__':
  main ()