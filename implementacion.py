# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 15:03:25 2023

@author: Est01
"""

from Script_Adelantar import *

BD = {}

while True:
    
    menu = input("0- Vernombre paciente \n1- Enfermera\n2-Paciente\n3-Medico\n4-Salir")
    
    if menu == "1":
        e = Enfermera()
        e.asignarNombre(input(" Ingrese el nombre enfemero/a: "))
        e.asignarCedula(int(input(" Ingrese el cedula enfemero/a: ")))
        e.asignarGenero(input(" Ingrese el género enfemero/a: "))
        e.asignarRango(input(" Ingrese el Rango enfemero/a: "))
        e.asignarTurno(input(" Ingrese el turno enfemero/a: "))
        BD[e.verCedula()] = e
    elif menu == "2":
        p = Paciente()
        p.asignarNombre(input(" Ingrese el nombre paciente: "))
        p.asignarCedula(int(input(" Ingrese el cedula paciente: ")))
        p.asignarGenero(input(" Ingrese el género paciente: "))
        p.asignarServicio(input(" Ingrese el servicio paciente: "))
        BD[p.verCedula()] = p
        
        
    elif menu == "0":
        cc= int(input(" Ingrese la cédula del paciente que desea buscar: "))
        print(BD[cc].verNombre())
        
    elif menu == "3":
        pass
    elif menu == "4":
        break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    