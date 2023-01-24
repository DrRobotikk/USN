from tkinter import *
import mysql.connector

mindatabase=mysql.connector.connect(host='localhost',port=3306,
            user='Eksamenssjef',passwd='oblig2022',db='oblig2022')


vindu=Tk()
vindu.Title('Karakterstatistikk')

