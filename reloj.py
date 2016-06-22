import time
for x in range(0,60):
    t=time.localtime()
    horas=t[3]
    minutos=t[4]
    segundos=t[5]
    print("Hora: "+str(horas)+": "+str(minutos)+": "+str(segundos))
    time.sleep(1)