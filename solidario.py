#Este programa calcula el impuesto solidario segun hacienda 2019 Costa Rica
t0 = 817000
t10 = 1199000
t15 = 2103000
t20 = 4205000

#metodo para obtener salario
def getSalario():
    try:
        return int(input('''Favor ingrese su salario
->'''))
    except ValueError:
        print('''Favor no ingresar texto, solo numeros''')
        return getSalario()

def getImpuestoT10(salario):
    return ( salario - t0) * 0.1

def mostrarResultado( impuesto, salario):
    print("su salario es "+ str(salario)+
          " colones,y el impuesto a pagar es: "+ str(impuesto) + " colones")

    
salario = getSalario()

if salario <= t0:
    print("su salario es "+ str(salario)+ " y no esta sujeto a impuesto solidario")
elif salario > t0 and salario <= t10:
    mostrarResultado(getImpuestoT10(salario), salario)
elif salario > t10 and salario <= t15:
    impuesto = (( t10 - t0) * 0.1  )+ ((salario - t10) * 0.15)
    print("su salario es "+ str(salario)+
          " colones,y el impuesto a pagar es: "+ str(impuesto) + " colones")
elif salario > t15 and salario <= t20:
    impuesto = (( t10 - t0) * 0.1  )+ ((t15 - t10) * 0.15 ) + ((salario - t15) * 0.20)
    print("su salario es "+ str(salario)+
          " colones,y el impuesto a pagar es: "+ str(impuesto) + " colones")
else:
    impuesto = (( t10 - t0) * 0.1  )+ ((t15 - t10) * 0.15 ) + ((t20 - t15) * 0.20) + ((salario - t20) * 0.25)
    print("su salario es "+ str(salario)+
          " colones,y el impuesto a pagar es: "+ str(impuesto) + " colones")
