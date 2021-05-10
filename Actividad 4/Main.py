from FechaHora import FechaHora

if __name__ == '__main__':

    print(" ")
    d=int(input("Ingrese Dia: "))
    mes=int(input("Ingrese Mes: "))
    a=int(input("Ingrese Año: "))
    h=int(input("Ingrese Hora: "))
    m=int(input("Ingrese Minutos: "))
    s=int(input("Ingrese Segundos: "))
    print(" ")
    r = FechaHora () 

    r1 = FechaHora(d,m,a); 

    r2= FechaHora(d,mes,a,h, m, s)

    r.Mostrar()

    r1.Mostrar()

    r2.Mostrar()

    input()

    r.PonerEnHora(5) 

    r.Mostrar()

    input()

    r2.PonerEnHora(13,30) 

    r2.Mostrar()

    input()

    r.PonerEnHora(14, 30, 25) 

    r.Mostrar()

    input()

    r.AdelantarHora(3) 

    r.Mostrar()

    input()

    r1.AdelantarHora(1,15) 

    r1.Mostrar()

    input()