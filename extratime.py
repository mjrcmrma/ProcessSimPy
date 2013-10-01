__author__="Manuel"
__date__ ="$Sep 17, 2013 7:45:42 AM$"

from Tkinter import *
from collections import deque

if __name__ == "__main__":

    master = Tk()
    master.title("Simulador de ordenes")
    master.geometry("300x300")
    aviso = 0
    num_orden = 0
    en_cola = 0
    en_sistema = 0
    t_cola = 0
    posY = 100
    atendiendo = deque(maxlen = 4)
    cola = deque()
    h_out = []
    h_extra = 0
    
    def options():
        b = Button(master, text="Agregar", width = 10, command = agregar_orden)
        b.pack()
        mainloop()
    
    def agregar_orden():
        global child 
        child = Tk()
        child.title("Simulador de ordenes")
        child.geometry("250x200")
        global hora
        global varh
        varh = StringVar(child)
        varh.set("09:00 hrs")
        hora = OptionMenu(child, varh , "10:00 hrs", "11:00 hrs", "12:00 hrs", "13:00 hrs")
        hora.pack()
        LHora = Label(child, text = "Hora de Llegada")
        LHora.pack()
        global var
        var = StringVar(child)
        var.set("Seleccione tipo de Orden")
        tipo = OptionMenu(child, var ,"Ordinaria", "Prioritaria")
        tipo.pack()
        LTipo = Label(child, text = "Tipo de orden")
        LTipo.pack()
        Ok = Button(child, text="Ok", width = 10, command = recibir_orden).pack()
        #hora.get()
    
    def recibir_orden():
        global h
        h = varh.get()
        global t
        global aviso
        t = var.get()
        if(t == "Seleccione tipo de Orden"):
            LAviso = Label(child, text = "Es necesario seleccionar tipo de orden")
            LAviso.pack()
            aviso = aviso + 1
            if (aviso > 1):
                LAviso.destroy()
        else:
            child.destroy()
            procesar_orden(h, t)
    
    def procesar_orden(hora, tipo):
        global trab_disp
        global num_orden
        global h_salida
        global t_sistema
        global t_cola
        global en_cola
        global en_sistema
        global horas_tipo
        global atendiendo
        global cola
        global h_out
        global h_extra 
        num_orden = num_orden + 1
        ordinaria = 2
        prioritaria = 4
        i = 0
        while (i < len(h_out)):
            if(h_out[i] == int(hora[:-7])):
                del h_out[i]
                atendiendo.pop()
                if len(cola) > 0:
                    cola.popleft()
            i = i + 1
        j = 0
        while (j < len(h_out)):
            if(h_out[j] == int(hora[:-7])):
                del h_out[j]
                atendiendo.pop()
                if len(cola) > 0:
                    cola.popleft()
            j = j + 1
        if (len(atendiendo) != atendiendo.maxlen):
            atendiendo.append(num_orden)
            print atendiendo
            if (tipo == "Ordinaria"):
                h_salida = int(hora[:-7]) + ordinaria
                t_sistema = ordinaria
            else: 
                h_salida = int(hora[:-7]) + prioritaria
                t_sistema = prioritaria
        else:
            cola.append(num_orden)
            t_cola = t_cola + 1
            if (tipo == "Ordinaria"):
                h_salida = int(hora[:-7]) + ordinaria + len(cola)
                t_sistema = ordinaria + t_cola
            else: 
                h_salida = int(hora[:-7]) + prioritaria + len(cola)
                t_sistema = prioritaria + t_cola
        if (h_salida > 17):
            h_extra = h_extra + (h_salida - 17)
        h_out.append(h_salida)
        print h_out
        print h_extra
        print cola
        en_sistema = len(atendiendo) + len(cola)  
        en_cola = len(cola)
        imprimir_lista(num_orden, en_cola, en_sistema, tipo, h_salida, hora, t_sistema, t_cola)
    
    def add_header():
        master.geometry("1200x500")
        Label(master, text="Hora de Llegada").place(bordermode = OUTSIDE, x = 20, y = 80)
        Label(master, text="Numero de Orden").place(bordermode = OUTSIDE, x = 150, y = 80)
        Label(master, text="Tipo de Orden").place(bordermode = OUTSIDE, x = 280, y = 80)
        Label(master, text="Numero en Cola").place(bordermode = OUTSIDE, x = 400, y = 80)
        Label(master, text="Numero en Sistema").place(bordermode = OUTSIDE, x = 520, y = 80)
        Label(master, text="Tiempo en Cola").place(bordermode = OUTSIDE, x = 660, y = 80)
        Label(master, text="Tiempo en Sistema").place(bordermode = OUTSIDE, x = 780, y = 80)
        Label(master, text="Hora de Salida").place(bordermode = OUTSIDE, x = 910, y = 80)
    
    def imprimir_lista(num_orden, en_cola, en_sistema, tipo, h_salida, hora, t_sistema, t_cola):
        add_header()
        global posY
        master.config(height = (int(posY) + 20))
        Label(master,text = hora).place(bordermode = OUTSIDE, x = 40, y = posY)
        Label(master,text = num_orden).place(bordermode = OUTSIDE, x = 190, y = posY)
        Label(master,text = tipo).place(bordermode = OUTSIDE, x = 290, y = posY)
        Label(master,text = en_cola).place(bordermode = OUTSIDE, x = 440, y = posY)
        Label(master,text = en_sistema).place(bordermode = OUTSIDE, x = 570, y = posY)
        Label(master,text = t_cola).place(bordermode = OUTSIDE, x = 700, y = posY)
        Label(master,text = t_sistema).place(bordermode = OUTSIDE, x = 840, y = posY)
        Label(master,text = h_salida).place(bordermode = OUTSIDE, x = 950, y = posY)
        posY = posY + 20
    
    options()

        
    

