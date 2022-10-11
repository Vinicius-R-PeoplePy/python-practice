#29-08-2022, Segunda-feira, exercícios

#from typing import Dict


#x = 5
#y = 7.0
#z = "sim" 
#t = 10>8
#u = ('John, Jen, Ju')
#r = ["1, 2, 3"]
#q = {"1, 2, 3"}
#umatuple = tuple(("maçã, uva, abacate"))

#myDict = {
#  "print(type())": "printa o tipo de variável (str, int, bool, tuple, list, dict...)",
#  "index": "relativo aos caracteres, indica o número, por exemplo: a palavra bolo tem 4 letras, cujo index vai de 0(b) até 4(segundo e último << o >>)",
#  "caractere": "vide unicode (pesquisar!!!!!)"
#}

#print(type(x))
#print(type(y))
#print(type(z))
#print(type(t))
#print(type(u))
#print(type(r))
#print(type(q))
#print(z[1])
#print(z[2], z[1], z[0])
#print(type(umatuple))
#print(myDict)

#for x in "banana":
#    print(x)

#Terça-feira 30-08-2022

# Naive solution to count the total number of set bits in 'n'
#def countSetBits(n):
#
#    count = 0 
#    while n:
#        count += (n & 1)   # check last bit 
#        n >>= 1 
#    return count
#
#if __name__ == '__main__':
#
#  n = 1024
#  print(f'The total number of set bits in {str(n)} ({bin(n)}) is {countSetBits(n)}')

#from os import sep
#from tkinter import END


#a = "Hello, World!"
#print(len(a))

#txt = "The best things in life are free!"
#print("free" in txt)

#txt = "The best things in life are free!"
#if "free" in txt:
#  print("Yes, 'free' is present.")

#print("expensive" not in txt)

#if "expensive" not in txt:
#  print("No, 'expensive' is NOT present.")

#b = "Hello, World!"
#print(b[2:5])
#print(b[:5])
#print(b[:13])

# cool alternative to print HW: 

#b = "Hello World!"
#print(b[:13])

#print(b[2:])
#print(b[0:])
#print(b[-5:-2])
#print(b[-1:])

#print(b.upper())
#print(b[-5:-2].upper())
#print(b[0:9].upper(), b[9:13].lower()) # how to eliminate the space when it prints? #atualização, 09/09/2022: a concatenação neste caso não está funcionando pelo operador ++, mas sim pelo operador +
#segue o exemplo de concatenação apenas com o operador + não-duplicado:
#print(b[0:9].upper()+b[9:13].lower())


#checagem de cálculo que estava resolvendo na mão:

#print(795078+74321-8808*5436) #primeira resposta não confere 

#x = 795078
#y = 743321
#z = 8808
#w = 5436
#m = z*w

#result = x+(y-m)
#print(result) #segunda resposta também não confere



#x = 795078
#y = 743321
#z = 8808
#w = 5436 
#result1 = x + y 
#result2 = -z*w
#a = result1
#b = result2
#result3 = a - b

#result = x+y-z*w #terceira resposta não confere (-46341889); adicionei mais cinco variáveis (res1...b)

#print(result1, result2, result3) 

# provavelmente resultado do cálculo à mão estava errado 

#print("Bem-vindo!")

# guess game forma 1: 

#g = input("Adivinhe o número: ")
#guess = int(g)
#if guess == 5: 
#       print("Você ganhou!", end='\n\n\n' "Parabéns!")
#if guess > 5:
#       print("Você perdeu!")
#       print ("Game over!", end='\n\n\n' "Tente outra vez!...")
#if guess < 5:
#       print("Você perdeu!")
#       print ("Game over!", end='\n\n\n' "Tente outra vez!...")

#x = float(1)
#y = int(2.8)
#z = complex(1)

#print(x)
#print(y)
#print(z)

#print(type(x))
#print(type(y))
#print(type(z))


#import random

#print(random.randrange(1, 10))
#print(random.randrange(1, 100))
#print(random.randrange(1, 1000))
#print(random.randrange(1, 1)) # -> raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width)) ValueError: empty range for randrange() (1, 1, 0)
#print(random.randrange(1,2))

#random = float # Como gerar random float?

# via https://www.w3schools.com/python/

# Get the first character of the string txt. 
# txt = "Hello World"
# x = txt[0]

# Get the characters from index 2 to index 4 (llo)
# txt = "Hello World"
# x = txt[2:5]

# Return the string without any whitespace at the beginning of the end
# txt = " Hello World "
# x = txt.strip()

# Convert the value of txt to upper case and lower case. 
# txt = "Hello World"
# txt = txt.upper()
# txt = txt.lower()

# Replace the characther H with a J 
# txt = "Hello World"
# txt = txt.replace("H", "J")

#txt = "Números randômicos teste, testando randomicidade."
#txt = txt.replace("Números randômicos teste,", "print(random.randrange()) para gerar números aleatórios...")
#print (txt) 

#import random

#print(random.randrange(1, 100))

# Ideias para dicionário. 
# Texto base https://metrologia.org.br/wpsite/wp-content/uploads/2019/07/Cartilha_O_novo_SI_29.06.2029.pdf
# O dicionário conterá medidas do SI (Sistema Internacional de Unidades), como, por exemplo, a definição de que kilograma é a massa de um dl cúbico de água, ou 1 milésimo de 1 metro cúbico de água. 
# SI -> Sistema Internacional de Medidas, criado após a revolução francesa, pela Convenção do Metro, durante a 11ª Conferência Geral de Pesos e Medidas (CGPM), realizada em 1960.
# CGPM -> Conferência Geral de Pesos e Medidas
# Para a definição de SI: possui sete unidades de base: o metro (comprimento), o kilograma (massa), o segundo (tempo), o ampere (corrente elétrica), o kelvin (temperatura termodinâmica), o mol (quantidade de substância) e a candela (intensidade luminosa)
# www.bipm.org/en/about-us/member-states/.
# Antigo kilograma -> definido a partir de um protótipo internacional, um cilindro de uma liga de platina e irídio e essa era a unidade utilizada para determinar a massa de um próton, de um elétron ou de outras partículas elementares.
# Curiosidade -> Em 1900, Max Planck, ao formular sua lei da radiação, já trazia as ideias de "constantes" e de "unidades naturais de medida" que seriam válidas para "todos os tempos e para todas as civilizações, mesmo extraterrestres e não-humanas"...
# Para a definição de segundo -> é relacionado a um número exato de oscilações na camada eletrônica do átomo de césio (relógio atômico).
# Sobre o relógio atômico -> https://super.abril.com.br/mundo-estranho/como-funciona-o-relogio-atomico/
# Para definição de Césio -> O Césio é um elemento químico de símbolo Cs e número atômico 55, com massa atômica de 132,9 u. É obtido por fissão nuclear de outros radioisótopos de urânio ou plutônio. 
# Para definição de urânio e plutônio...

#txt = "xxx, yyy"
#txt = txt.replace("xxx", "zzz")
#print(txt)

#28-09-2022

#a = "Hello, World!"
#b = "      Hello            World      "
#c = a.split(",")
#d = a.split("e")
#e = "Hello"
#f = "World"
#g = e + f 
#h = e + " " + f 
#i = e + "\n" + f 

#print(a.upper())
#print(a.lower())
#print(b.strip()) #not stripping (?)
#print(c)
#print(d)
#print(g)
#print(h)
#print(i)


# age = 175
#txt = "My name is Abraham, I am" + age 
#print(txt) #-> this will give error, due to the impossibility of combining strings and numbers in such a way. 

#age = 175 
#txt = "My name is Abraham, I am {}"
#print(txt.format(age))

#quantity = 3 
#itemno = 555
#price = 77.77
#myorder = "I want {} pieces of item {} for {} dollars"
#print(myorder.format(quantity, itemno, price))

#quantity = 5 
#itemno = 188 
#price = 50 
#myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}"
#print(myorder2.format(quantity, itemno, price))

#txt2 = "We are the so-called \"Vikings\" from the north."
#print(txt2)

#txt3 = 'It\'s alright.' 
#print(txt3)

#txt5 = "This will insert one \\ (backslash)."
#print(txt5)

#txt6 = "Hello\rWorld!"
#print(txt6)

#txt7 = "Hello\tWorld!"
#print(txt7)

#txt8 = "Hello \bWorld!"
#print(txt8)

#txt9 = "\110\145\154\154\157" # A backslash followed by three integers will result in a octal value in this case. 
#print(txt9)

#txt10 = "\x48\x65\x6c\x6c\x6f" # A backslash followed by an 'x' and a hex number represents a hex value.
#print(txt10)

#check-> https://www.sciencebuddies.org/science-fair-projects/references/ascii-table

#k = "diskpart list disk select disk x clean convert gpt create part efi size=500 format fs=fat32 assign letter w create part primary format fs=ntfs quick assign letter c exit"
#l = "UNIVERSAL SERIAL BUS"
#m = "                  cd/d D:\sources"

#print(k.capitalize())
#print(l.casefold())
#print(m.center()) #????
#print(k.count("a"))
#print(k.count("d"))
#print(k.encode(encoding="ascii", errors="replace")) 

#encode not functioning. check-> https://www.w3schools.com/python/ref_string_encode.asp

#print(l.endswith("s"))
#print(l.endswith("S"))

#n = "TRINTA\POR\CENTO\DE\CEM\É\IGUAL\A\TRINTA\DIVIDIDO\POR\CEM\VEZES\CEM\QUE\VAI\DAR\O RESULTADO 30\APÓS OPERAÇÃO\PELA REGRA DE 3\OU POR FRAÇÕES EQUIVALENTES"
#o = n.expandtabs(5)
#print(o) #expandtabs not functioning as in w3schools. Might be due to different python versions?(...)

#print(l.find("BUS"))
#print(l.find("U")) #found just U string in index 0; not also the U in penultimate index 
#print(l.find("L")) 

#txt11 = "For only {price:.2f} dollars!"
#print(txt11.format(price = 49))

#txt12 = "My name is {fname}, I'm {age}".format(fname = "Knuckles", age = 20)
#txt13 = "My name is {0}, I'm {1}".format("Obi-Wan", 35)
#txt14 = "My name is {}, I'm {}".format("Wally", 36)
#print(txt12, txt13, txt14, sep = '\n')

#print("Welcome!")
#guess = 0 
#while guess != 5:
#    g = input("Guess the number: ")
#    guess = int(g)
#    if guess == 5:
#        print("You win! \n Congratulations!")
#    if guess == 4: 
#            print("Hmmmm... it's getting hot...")
#    if guess == 3:
#            print("Hmmmm... not so bad...")
#    if guess == 2:
#            print("Ahhh... not this...")
#    if guess == 1: 
#            print("Try again!")
#    if guess == 0: 
#            print("It's really really cold...")
#    if guess == 6:
#            print("Hmmmm... it's getting hot...")
#    if guess == 7: 
#            print("Hmmmm...not so bad... ")
#    if guess == 8:
#            print("Ahhh... not this...")
#    if guess == 9:
#            print("Try again!")
#    if guess == 10:
#            print("Stratosferic!...")
#else:
#    print("Game over!")

#answer = "no"
#while answer == "no": 
#    answer = input("Are we there?")
#print("We're there!")

#from random import randint 
#secret = randint(1,10)
#print("Welcome!")
#guess = 0 
#while guess!= secret:
#    g = input("Guess the number: ")
#    guess = int(g)
#    if guess == secret: 
#        print("You win!")
#    else:
#        if guess > secret: 
#            print("Too high")
#        else:
#            print("Too low")
#print("Game over!")

#import urllib.request

#page = urllib.request.urlopen("https://www.programiz.com/python-programming/for-loop")
#text = page.read().decode("utf8")


#print(text.find("Loop continues until we reach the last item in the sequence. The body of for loop is separated from the rest of the code using indentation."))
#loopinfo = text[76886:77025]
#print(loopinfo)

#O último index de uma substring é excluído numa contagem, embora o primeiro index seja incluído. 

#where = text.find("Loop continues until we reach the last item in the sequence. The body of for loop is separated from the rest of the code using indentation.")

#start_of_loop_info =  where + 0
#end_of_loop_info = start_of_loop_info + 138


#loopinfo = text[start_of_loop_info:end_of_loop_info]

#print(loopinfo)  

#Reuse code with functions 

#def make_smoothie():
#    juice = input("What juice would you like?\n ")
#    fruit = input("Ok - and how about the fruit?\n ")
#    print("Thanks. Let's go!")
#    print("Crushing the ice...")
#    print("Blending the " + fruit)
#    print("Now adding in the " + juice + " juice")
#    print("Finished! There's your " + fruit + " and " + juice + "smoothie!")

#print("Welcome to smoothie-matic 2.0")
#another = "Y" 
#while another == "Y":
#        make_smoothie() 
#        another = input("How about another(Y/N)?\n ")

#thislist =	["0) Antigo kilograma -> definido a partir de um protótipo internacional, um cilindro de uma liga de platina e irídio e essa era a unidade utilizada para determinar a massa de um próton, de um elétron ou de outras partículas elementares.",
#"1) SI -> Sistema Internacional de Medidas, criado após a revolução francesa, pela Convenção do Metro, durante a 11ª Conferência Geral de Pesos e Medidas (CGPM), realizada em 1960.",
#"2) Para a definição de SI: possui sete unidades de base: o metro (comprimento), o kilograma (massa), o segundo (tempo), o ampere (corrente elétrica), o kelvin (temperatura termodinâmica), o mol (quantidade de substância) e a candela (intensidade luminosa)",
#"3) Para a definição de segundo -> é relacionado a um número exato de oscilações na camada eletrônica do átomo de césio (relógio atômico)."]

#sort = int(input("Digite um número de [0] a [3] para informações diversas acerca de medidas: "))

#if sort == 0:
#   print(thislist[0])
#if sort == 1:
#    print(thislist[1])
#if sort == 2:
#    print(thislist[2])
#if sort == 3:
#    print(thislist[3])

# append items to the list, everyday

# guess-game com sequência de if's corrigida para elif's:

#print("Welcome!")
#guess = 0 
#while guess != 5:
#    g = input("Guess the number: ")
#    guess = int(g)
#    if guess == 5:
#        print("You win! \n Congratulations!")
#    elif guess == 4: 
#            print("Hmmmm... it's getting hot...")
#    elif guess == 3:
#            print("Hmmmm... not so bad...")
#    elif guess == 2:
#            print("Ahhh... not this...")
#    elif guess == 1: 
#            print("Try again!")
#    elif guess == 0: 
#            print("It's really really cold...")
#    elif guess == 6:
#            print("Hmmmm... it's getting hot...")
#    elif guess == 7: 
#            print("Hmmmm...not so bad... ")
#    elif guess == 8:
#            print("Ahhh... not this...")
#    elif guess == 9:
#            print("Try again!")
#    elif guess == 10:
#            print("Stratosferic!...")
#else:
#    print("Game over!")

# -> linux command list (via https://ss64.com/bash/)

'''

linux_list_commands_A_to_Z = (" & 	Start a new process in the background",
  	"alias 	Create an alias •",
  	"apropos 	Search Help manual pages (man -k)",
  	"apt 	Search for and install software packages (Debian/Ubuntu)",
  	"apt-get 	Search for and install software packages (Debian/Ubuntu)",
  	"aptitude 	Search for and install software packages (Debian/Ubuntu)",
  	"aspell 	Spell Checker",
  	"at 	Schedule a command to run once at a particular time",
  	"awk 	Find and Replace text, database sort/validate/index", 	  	 
  	"basename 	Strip directory and suffix from filenames",
  	"base32 	Base32 encode/decode data and print to standard output",
  	"base64 	Base64 encode/decode data and print to standard output",
  	"bash 	GNU Bourne-Again SHell",
  	"bc 	Arbitrary precision calculator language",
  	"bg 	Send to background",
  	"bind 	Set or display readline key and function bindings •",
  	"break 	Exit from a loop •",
  	"builtin 	Run a shell builtin",
  	"bzip2 	Compress or decompress named file(s)",  	 
  	"cal 	Display a calendar",
  	"caller 	Return the context of any active subroutine call •",
  	"case 	Conditionally perform a command",
  	"cat 	Concatenate and print (display) the content of files",
  	"cd 	Change Directory",
  	"cfdisk 	Partition table manipulator for Linux",
  	"chattr 	Change file attributes on a Linux file system",
  	"chgrp 	Change group ownership",
  	"chmod 	Change access permissions",
  	"chown 	Change file owner and group",
  	"chpasswd 	Update passwords in batch mode",
  	"chroot 	Run a command with a different root directory",
  	"chkconfig 	System services (runlevel)",
  	"cksum 	Print CRC checksum and byte counts",
  	"clear 	Clear terminal screen",
  	"cmp 	Compare two files",
  	"comm 	Compare two sorted files line by line",
  	"command 	Run a command - ignoring shell functions •",
  	"continue 	Resume the next iteration of a loop •",
  	"cp 	Copy one or more files to another location",
  	"cpio 	Copy files to and from archives",
  	"cron 	Daemon to execute scheduled commands",
  	"crontab 	Schedule a command to run at a later time",
  	"csplit 	Split a file into context-determined pieces",
  	"curl 	Transfer data from or to a server",
  	"cut 	Divide a file into several parts", 	  	 
  	"date 	Display or change the date & time",
  	"dc 	Desk Calculator",
  	"dd 	Data Duplicator - convert and copy a file, write disk headers, boot records",
  	"ddrescue 	Data recovery tool",
  	"declare 	Declare variables and give them attributes •",
  	"df 	Display free disk space",
  	"diff 	Display the differences between two files",
  	"diff3 	Show differences among three files",
  	"dig 	DNS lookup",
  	"dir 	Briefly list directory contents",
  	"dircolors 	Colour setup for 'ls'",
  	"dirname 	Convert a full pathname to just a path",
  	"dirs 	Display list of remembered directories",
  	"dos2unix 	Windows/MAC to UNIX text file format converter",
  	"dmesg 	Print kernel & driver messages",
  	"dpkg 	Package manager (Debian/Ubuntu).",
  	"du 	Estimate file space usage",
	"echo	Display message on screen",
	"egrep 	Search file (s) ",
	"eject 	removable media",
    "enable Enable and disable builtin shell commands",
	"env	Environment variables",
	"ethtool Ethernet card settings",
	"eval 	Evaluate several commands/arguments",
	"exec	Execute a command",
	"exit	Exit the shell",
	"expand	Convert tabs to spaces",
	"export	Set an environment variable",
	"expr	Evaluate expressions",
	"false Do nothing, unsuccesfully",
	"fdformat	Low-level format a floppy disk",
	"fdisk	Partition table manipulator for Linux",
	"fg		Send job to foreground",
	"fgrep	Search file(s) for lines that match a fixed string",
	"file	Determine file type",
	"find	Search for files that meet a desired criteria",
	"fmt	Reformat paragraph text",
	"fold	Wrap text to fit a specified width",
	"for	Expand words, and execute commands",
	"format	Format disk or tapes",
	"free	Display memory usage",
	"fsck	File system consistency check and repair",
	"ftp	File Transfer Protocol",
	"function Define Function Macros",
	"fuser	Identify/kill the process that is accessing a file",
	"gawk	Find and Replace text within file(s)",
	"getopts	Parse positional parameters",
	"getfacl	Get file access control lists",
	"grep	Search file(s) for lines that match a given pattern",
	"groupadd	Add a user security group",
	"groupdel	Delete a group",
	"groupmod	Modify a group",
	"groups		Print group names a user is in",
	"gzip	Compress or decompress named file(s)",
	"hash	Remember the full pathname of a name argument",
	"head	Output the first part of file(s)",
	"help	Display help for a built-in command",
	"history Command History",
	"hostname Print or set system name",
	"htop	Interactive process viewer",
	"iconv Convert the character set of a file",
	"id		Print user and group id's",
	"if		Conditionally perform a command",
	"ifconfig	Configure a network interface",
	"ifdown		Stop a network interface",
	"ifup	Start a network interface",
	"import		Capture an X server screen and save the image to file",
	"install	Copy files and set attributes",
	"iostat		Report CPU and i/o statistics",
	"ip		Routing, devices and tunnels",
	"jobs 	List active jobs",
	"join	Join lines on a common field",
	"kill	Kill a process by specifying its PID",
	"killal		Kill processes by name",
	"less	Disply output one screen at a time",
	"let	Perform arithmetic on shell variables",
	"link	Create a link to a file",
	"In		Create a symbolic link to a file",
	"local	Create a function variable",
	"locate	Find files",
	"logname	Print current login name",
	"logout		Exit a login shell",
	"look	Display lines beginning with a given string",
	"lpc	LIne printer control program",
	"lpr	Print files",
	"lprint		Print a file",
	"lprintd	Delete a file print job",
	"lprintq	List the print queue",
	"lprm	Remove jobs from the print queue",
	"lsattr		List file attributes on a Linux second extended file system",
	"lsblk	List block devices",
	"ls		List information about file(s)",
	"lsof	List open files",
	"lspci	List al PCI devices",
	"make	Recompile a group of programs",
	"man	Help manual",
	"mapfile	Read lines from standard input into a indexed array variable",
	"mkdir	Make a file",
	"mkisofs	Create a hybrid ISO9660/JOLIET/HFS filesystem",
	"mknod		Make block or characther special files",
	"mktemp		Make a temporary file",
	"more		Display output one screen at a time",
	"most		Browse or page through a text file",
	"mount		Mount a file system",
	"mtools		Manipulate MS-DOS files",
	"mtr		Network diagnostics (traceroute/ping)",
	"mv			Move or rename files or directories",
	"mnv 		Mass Move and rename (files)",
	"nc			Netcat, read and write data across networks"
	"netstat	Networking connections/stats",
	"nft		nftables for packet filtering and classification",
	"nice		Set the priority of a command or job",
	"nl			Number lines and write files",
	"nohup		Run a command immune to hangups",
	"notify-send	Send desktop notifications",
	"nslookup	Query Internet name servers interactively",
	"open		Open a file in its default application",
	"op			Operator access",
	"passwd		Modify a user passwd",
	"paste		Merge lines of files",
	"patchchk	Check file name portability",
	"Perf		Performance analysis tools for Linux",
	"ping		Test a network connection",
	"pgrep		List processes by name",
	"pkill		Kill processes by name",
	"popd		Restore the previous value of the current directory",
	"pr			Prepare files for printing",
	"printcap	Printer capability database",
	"printenv	Print environment variables",
	"printf		Format and print data",
	"ps			Process status",
	"pushd		Save and then change the current directory",
	"pv			Monitor the progress of data thorugh a pipe",
	"pwd 		Print Working Directory",
	"quota		Display disk usage and limits",
	"quotacheck		Scan a file system for disk usage",
	"ram		ram disk device",
	"rar		Arquive files with compression",
	"rcp		Copy files between two machines",
	"read		Read a line from standard input",
	"readarray	Read from stdin into an array variable",
	"readonly	Mark variables/functions as readonly",
	"reboot 	Reboot the system",
	"rename		Rename files",
	"renice		Alter priority of running processes",
	"remsync	Synchronize remote files via email",
	"return 	Exit a shel function",
	"rev		Reverse lines of a file",
	"rm			Remove files",
	"rmdir		Remove folder(s)",
	"rsync		Remote file copy (Synchronize file trees)",
	"screen 	Multiplex terminal, run remote shells via ssh",
	"scp		Secure copy (remote file copy)",
	"sdiff		Merge two files interactively",
	"sed		Stream Editor",
	"select 	Accept user choices via keyboard input",
	"seq		Print numeric sequences",
	"set		Manipulate shell variables and functions",
	"setfacl	Set file access control lists.",
	"sftp 		Secure FIle Transfer Program",
	"shift		Shift positional parameters",
	"shopt 		Shell Options",
	"shuf		Generate random permutations",
	"shutdown	Shutdown or restart linux",
	"sleep		Delay for a specified time",
	"slocate	Find files",
	"sort		Sort text files",
	"source		Run commands from a fle '.' ",
	"split		Split a file into fixed-size pieces",
	"ss			Socket Statistics",
	"ssh		Secure Shell client (remote login program)",
	"stat		Display file or file system status",
	"strace		Trace system calls and signals",
	"su			Substitute user identity",
	"sudo		Execute a command as another user",
	"sum		Print a checksum for a file",
	"suspend	Suspend execution of this shell",
	"sync		Synchorinze data on disk with memory",
	"tail 		Output the last part of a file",
	"tar		Store, list or extract files in an archive",
	"tee		Redirect output to multiple files",
	"test		Evaluate a conditional expression",
	"time		Measure Program running time"
	"timeout 	Run a command with a time limit",
	"times		User and system times",
	"tmux 		Terminal multiplexer",
	"touch		Change ofile timstamps",
	"top 		List processes running on the system",
	"tput		Set terminal-dependent capabilities, color, position",
	"traceroute		Trace Route to Host",
	"trap		Execute a command when the shell receives a signal",
	"tr			Translate, squeee, and/or delete characters",
	"true		Do nothing, successfully",
	"tsort		Topological sort",
	"tty 		Print filename of terminal on stdin",
	"type 		Describe a command",
	"ulimit		Limit user resources",
	"umask		Users file creation mask",
	"umount		Unmount a device",
	"unalias	Remove an alias",
	"uname		Print system information",
	"unexpand	Convert spaces to tabs",
	"uniq		Uniquify files",
	"units		Convert junits from one scale to another",
	"unix2dos	UNIX to Windows or MAC text file format converter",
	"unrar		Extract files from a rar archive",
	"unset		Remove variable or function names",
	"unshar		Unpack shell archive scripts",
	"until		Execute commands (until error)",
	"uptime		Show uptime",
	"useradd	Create new user account",
	"userdel	Delete a user account",
	"usermod	Modify user account",
	"users		List users currently",
	"uuencode 	Encode a binary file",
	"uudecode	Decode a file created by uuencode",
	"v			Verbosely list directory contents ('ls -l -b)",
	"vdir		Verbosely list directory contents ('ls -l -b)",
	"vi			Text Editor",
	"vmstat		Report virtual memory statistics",
	"w			Show who is logged on and what they are doing",
	"wait		Wait for a process to complete",
	"watch		Execute/display periodically",
	"wc			Print byte, word, and line counts",
	"whereis	Search the user's $path, man pages and source files for a program",
	"which		Execute commands",
	"who		Print all usernames currently logged in",
	"whoami		Print the current user id and name ('id un')",
	"wget		Retrieve web pages or files via HTTP, HTTPS or FTP",
	"write		Send a messager to another user",
	"xargs		Execute utility, passing constructed argument list(s)",
	"xdg-open	Open a file o URL in the user's preferred application",
	"xxd		Make a hexdump or do the reverse",
	"xz			Compress or decompress .xz and .lzma files",
	"yes		Print a string until interrupted",
	"zip		Package and compress (archive) files",
	".			Run a command script in the current shell",
	"!!			Run the last command again",
	"###		Comment / Remark")



print(len(linux_list_commands_A_to_Z))
i = 0
while i < len(linux_list_commands_A_to_Z):
  print(linux_list_commands_A_to_Z[i])
  i = i + 1
'''
'''
# List is a collection which is ordered and changeable. Allows duplicate members. 
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members. 
# Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members. 
# Dictionary is a collection which is ordered and changeable. No duplicate members. 
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

#via https://www.w3schools.com/python/python_lists_methods.asp : 

#List Methods 

#Python has a set of built-in methods that you can use on lists. 

#append(). Adds an element at the end of the list
#clear(). Removes all the elements from the list 
#copy(). Returns a copy of the list 
#count() Returns the number of elements with the speciefied value
#extend(). Add the elements of a list (or any iterable), to the end of the current list
#index(). Returns the index of the first element with the specified value
#insert(). Adds an element at the specified position
#pop(). Removes the element at the specified position 
#remove(). Removes the item with the specified value 
#reverse(). Reverses the order of the list 
#sort(). Sorts the list
# fruits = ["apple, "banana", "cherry"]
# fruits.insert(1, "lemon)") -> to add "lemon" as the second item in the fruits list.
'''
#import random

#print = input(input1)
#if input == Character1:
#	print(Character1)
#elif input == Character2:
#	print(Character2); 

#thislist =	["0) Antigo kilograma -> definido a partir de um protótipo internacional, um cilindro de uma liga de platina e irídio e essa era a unidade utilizada para determinar a massa de um próton, de um elétron ou de outras partículas elementares.",
#"1) SI -> Sistema Internacional de Medidas, criado após a revolução francesa, pela Convenção do Metro, durante a 11ª Conferência Geral de Pesos e Medidas (CGPM), realizada em 1960.",
#"2) Para a definição de SI: possui sete unidades de base: o metro (comprimento), o kilograma (massa), o segundo (tempo), o ampere (corrente elétrica), o kelvin (temperatura termodinâmica), o mol (quantidade de substância) e a candela (intensidade luminosa)",
#"3) Para a definição de segundo -> é relacionado a um número exato de oscilações na camada eletrônica do átomo de césio (relógio atômico)."]

#sort = int(input("Digite um número de [0] a [3] para informações diversas acerca de medidas: "))

#if sort == 0:
#   print(thislist[0])
#if sort == 1:
#    print(thislist[1])
#if sort == 2:
#    print(thislist[2])
#if sort == 3:
#    print(thislist[3])



#input_Arnold = Select_name(1)
#input_Ana = Select_name(2)
#input_characther1 = input_Arnold
#input_characther2 = input_Ana
#print = input1 
#print = input2



#print = input 
#print = input 
#Age = random.randrange(1,100)
#if input == [0]:
#	print("Arnold")
#elif input == [1]:
#	print("Ana")

#age = 36 
#name = ("John")
#txt = print("My name is {}, and I am {}".format(name, age))
#
#a = ["x", "y", "z"]
#b = ["a", "b", "c"]
#
#a.append(b)
#
#print (a)
#print(a.copy())
#a.extend(b)
#print(a)
#
#print(a.count("z"))
#
#a.clear()
#print(a)

#print(a.copy())


'''a = ["x", "y", "z"]
a.append("yyy")
print(a)

a.insert(0, "aaaaa")
print(a)

a.remove("aaaaa")
print(a) '''