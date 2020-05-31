###################################################
###
### Hecho el 2010 para bajarse todo la biblioteca de paper de Taylor
### Ya esta obsoleto 
###
####################################################

import string
import urllib2
import os
import sys
import subprocess
 
def coma(cad):
        try:
            retcode = subprocess.call(cad, shell=True)
            print retcode
            if retcode < 0:
                print >>sys.stderr, "Proceso Hijo Fallo", -retcode
            else:
                print >>sys.stderr, "Proceso Hijo enviado", retcode
        except OSError, e:
            print >>sys.stderr, "Ejecucion Fallida:", e
 
s0="http://www.tandf.co.uk/journals/JanMathMadness/"
ur1="http://www.informaworld.com/smpp/"
jur="JanMathMadness"
coma("mkdir "+jur+" && cd "+jur+"/")
 
r0=urllib2.urlopen(s0)
h0=r0.read()
 
for i in range(1,len(h0.split("<p class=\"crop\"><a href=\""))):
        d=h0.split("<p class=\"crop\"><a href=\"")[i].split("\"><img")[0].split("\" title=\"")[0][-4:]
        n=h0.split("<p class=\"crop\"><a href=\"")[i].split("\"><img")[0].split("\" title=\"")[1]
        s1=h0.split("<p class=\"crop\"><a href=\"")[i].split("\"><img")[0].split("\" title=\"")[0]
        coma("mkdir "+jur+"/"+d+" && cd "+jur+"/"+d+"/")       
        coma("echo "+n+" > "+jur+"/"+d+"/Journal.txt")
        r1=urllib2.urlopen(s1)
        h1=r1.read()
 
        for j in range(1,len(h1.split("<td nowrap=\"nowrap\" style=\"text-indent: 5px;\">"))):
                s2=ur1+h1.split("<td nowrap=\"nowrap\" style=\"text-indent: 5px;\">")[j][12:43]
                coma("mkdir "+jur+"/"+d+"/"+str(j)+" && cd "+jur+"/"+d+"/"+str(j)+"/")         
                r2=urllib2.urlopen(s2)
                h2=r2.read()
 
                p=len(h2.split("title=\"Click to view the PDF fulltext\">Full Text PDF</a> | <a href=\"./"))-1
 
                for k in range(0,p):
 
                        print ur1+h2.split("title=\"Click to view the PDF fulltext\">Full Text PDF</a> | <a href=\"./")[k][-58:-2]
                        coma("wget "+ur1+h2.split("title=\"Click to view the PDF fulltext\">Full Text PDF</a> | <a href=\"./")[k][-58:-2])
                        coma("mv *.pdf "+jur+"/"+d+"/"+str(j)+"/")                     
 
                coma("cd .. ")
 
        coma ("cd .. ")
 
coma(" cd ..")
