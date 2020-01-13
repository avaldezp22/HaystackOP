# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import smtplib,ssl
import os, re
import sys
#python3
# habilitar el correo de envio
# https://www.google.com/settings/security/lesssecureapps

def sendemail():
    """
    Este método envia un correo electronico,
    indicando la altura en caso ocurre un huayco
    y la foto proporcionada por la camara
    instalada en el buzon
    """
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT   = 465
    sender      = 'xxxxxx@gmail.com'
    password    = '********' # aqui va la contraseña de mi correo
    recipient   = 'avaldez@igp.gob.pe','luisvilcatoma.08@gmail.com'
    subject     = 'S.A.T.H.-ROJ-Alerta'
    message     = 'roj- LUCHITO YA ESTAMOS REPORTE '+'\n'

    #context = ssl.create_default_context()

    msg= message

    session = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
    #session.ehlo()
    #session.starttls()
    #session.ehlo
    session.login(sender, password)
    session.sendmail(sender, recipient,msg)
    #print "something went wrong"
    session.quit()
    print ("Email S.A.T.H. Finish")


sendemail()
