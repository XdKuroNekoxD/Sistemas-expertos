#from nis import match
from cgitb import text
from tkinter import N
from unittest import case
import mysql.connector
import random as rd
from random import *
import pymysql
def adivina(nombre):
    y=0
    ñ=str(nombre)
    m=list(ñ)
    for m in nombre:
        text = m[0]
    ñ="".join(m)        
    print("¿ Tu campeon es",ñ,'?' )
    rol = input()
    while y==0:
        if rol == "no":
            res=0
            y=1
        elif rol=="si":
            res=1
            y=1
        else:
            print("Por favor ingrese un dato valido, (si tiene dudas lea el manual de uso)")
            print("¿ Tu campeon es",ñ,'?' )
            rol = input()
    return res
    
conexion = mysql.connector.connect(user = 'root', password = 'adivina_lol',
                                    host = 'localhost',
                                    database = 'LOL_Adivina',
                                    port = '3306')
cursor = conexion.cursor()
Rol=['ADC','JG','TOP','SUPP','MID']
Tipo=['Asesino','Luchador','Mago','Tirador','Soporte','Tanque']
Tablas=['tabla1']
Region1=[]
Region=[]
Tipo1=[]
Kind=[]
j=4
v=0
k=0
y=0
t=0
t2=0
print("bienvenido al adivina quien del porofesor, donde el porofesor tratara de adivinar a tu campeon favorito de Leage Of Legends:")
print("                                                                                 .:,.                                         ")                
print("                                            ..',,''..                         .          ,0Nd'                                ")                        
print("                                       .':oxkkxodkkxoc,.                     ,xko;.     .lXWWk. ..                            ")                        
print("                                    .'ldkkxdllcclc:;:looc.                   .dNWNk,   .cKNWWXc.ld,.                          ")                        
print("                                  .;ldl:;,,;cclc:;,,,,,;ox:,;::ccccc:,'....   cXNWWKl..lKNNWWWd'ccll:;;;:cloddollol:;'.       ")                        
print("                                .;odc;;,,,:cccc;,,,,,,,:xKXXNNWWWWWWNNXK00kxdokXNWWWNkxKNNNNNWd.;;.,oxdooodOkoccccccldo,      ")                        
print("              ..              .:xx:;cc,,,;:cc;,,,,,,,,,;dXNNNNWWWWWWNNWWWWWWWWNNNWWWWWNNNWWNWWKxxx;,:,.'';ll;,;,,;;;,,ld:.    ")                        
print("              ,oc,.       ..;lxKx;,cl;,,,,cc,',,,,;oOOOkOXNNXNNNNNNNWWWWWWWWWWWWWWWWWWWWWWWNWWNWWNX0kdlc:::'.',;:;,,,;;:ol.   ")                        
print("              ';;lodlcccllloocokc';c:''..';,....'';ONNWWWWWNNNNNNNNNNWNNNNNWWWWWWWWWWWWNNNWWWWWWWNNWWWWNXX0kdl;,',;lxxxdxkc   ")                        
print("              .,.'odc:okd:,,,,ld;',;'....,::cccc:;:ONNNNWWNNK0OOkkkkO00KXNWWWWWWNNNWWNNNNNNNWWNNNNNWWNNNNWWWNNKl':ddl:;,;co'  ")                        
print("              .,,:l'';oo,,,,,,cl,..''..;x0XXNNNNNKKXNNNKOdc;'''',,''''',:lxk0XWNNNNWNNNNNNNNNNNNNNNNWWNNNNNNX0xc;:,'',,,,,cc. ")                        
print("               ':;,..;oc',,,'',;'......'lx0XXNNNNNWNKxc,.':ldkOKKK000Oxoc,...:d0NWWWNNWWWWWNNNWWWNNNNNWNNNNNN0l;'.....'''';o' ")                        
print("               .;;...'c;....':ccc:;::cclokKNNNNWWWXx;.'cxKNWNKOxdolodxOKXXOkd;.,l0NWWWWWWWWWWWWWWWWNNNWWWWNWWWNXkl;.......'l; ")
print("                .;,...,'....lXWNNNNNNWWWWWWWWWWWNO:.'oKNWNKxlc:cclcc:;;;lxKNNNk:.,dXWWWWWWWWWWWWWWWWWWWWNX0kdoc::;,.......'l,    ")                     
print("                 .;'........cKNNWWWWWWWNNNNNWWWNk,.;ONNWN0ddxO0Odc:::coo:,ckKWWXo..oXWWWWWWWWWWWNWWWWNKkl;'.';clooool'.....'..       ")                 
print("                  .,'........dXNNNWWWWWNNXXK0OOd'.;0WNWWNXKXKKk:'''';cokOxOKXWWWNo..xNWWWWWWWWWWWNWN0o,.'cdOKNWWWWWWNOl'..'......       ")              
print("                   .,:,''....,x0OOkxdolc:;;;;;;'..dNNNNWWNXXX0l,'..;OXkdOKXXNWWWWK;.:KWWWWWWWWWWWWKo'.:xKNX0kxxddxkOKXNKdcc,''....        ")            
print("                     'd000kxdol:;;::clodxkkO0XKc.,ONNNWWWWNXNkc:'...ckxdOXXNNWWNWNo.,0WNWWWWWWWWN0:.'xXW0oc:::;,,;;,;coxKXkkKx. ....       ")           
print("                      ;OXXNNNNXK000KXNWWWWNNNWXl.'ONNWWNNNNNNkox:....lod0XNNNWWWWXl.,OXXNNNWWWWW0:.,OWWN0dkko:,,,,codl:,cKWNWk.  ....       ")          
print("                      .c0XXNNNNWWNNXXKKXNNWWNWNd..oXWWNWWWWNNKddd:',looOXXXNNNNNWO,..,;;:ccloxOOl..xWWNNXKOl''..;ood0KKOOXWNNxcc. ...       ")          
print("                    ..'cOXKXXNNWWWWWWNXXKKXXNNWK:.'xXNNNWWWWNN0dllclldOXNNNNNNNN0:.,dkxxdolc:;,'..:KWNNNXKd;;...lXXxkXXNWNNNNXNXc ...        ")         
print("               .':ldxOKXNXXXXNNNWWWWWWWWNNXKKXNWKc.'oKXXXXXXXXXKOxdxOKXNNWWNNWXk;.,ONWWWWWWWNXKx'.lNWWNNNKoc:....cxdkXXNNNNNNNWXc. ..         ")        
print("              'xKXXXXXXXNNXXXNNNNWWWWWWWWWWNXKXNN0o'.;ok0K00000000KKKKKKXXXXKkl,'l0WWWWWWWWWWNWK:.;KWNNNNKddx,...:ooOXXNNNWNNNNKl....         ")        
print("              .o0KKXXXXXNXNNNNNNNNWWWWWWWWNWNXKK0KKOl,.':ox0KXXNNNXXXXXXXXXK0000KNWWWNNNNNNNNWWNd..oXWNNXXOodo:;colxKXXXNNNNNNNNO;...         ")        
print("               .,lkOKKXXXXNNNNNNNNNWWWWWWNNNWNXK0KKXNKkl;'.';:loodOXNNWWWWWWWWWWWNWWWWNNXXXXXNNNKo;;dXNXXXXOdllclokKKKXXNNNNNNN0:...          ")        
print("                  ,dKXXXXXNNNNNNNNNNNWWWWWNNNNNNXKKKKKXXKOdoc:;;cxKNWWWNNNNNNNNWWNWWWWWWNXXXNNWWWNNK0KXKKKKKK0kkO0KKKKKKKKKXXKd'.',,;;.        ")       
print("                'lOXXXXXXXXXNNNNNNNNNNWWWWWNNXXNNNNXXXKKKKKKKXXNNWNNNNNNNNNNNNNWWWNNNNNNWWNWWWWWWWNWWWNN0OKNNNNNXXXXXXXXXKOdc'.'oKXNKl.        ")       
print("              .l0XXXXXXXXXXXXNNNNNNNNNNNNWWWWNXXXXNNNWNNNNNNNNWWWNNNNNWWWWNNNNXNNNNNNNNNWWNNWWNNNNNNNNWWXx:cdxO00KKK0Okdl;'.':oOXNNO;.         ")       
print("             .xKKKKKXXXXXXXXXXXNNNNNNNNNNWNNWWNXXNNNWWWWWWWWWNWWWWWNNNNNNNNNNNNNNNNWWNWNNNXXNNWNNNNNNNNWWNk:,'''',,,'''',:ldO0KXNNNO;          ")       
print("             .ldx0KKXXXXXXXXXXXXNNNNNNNNNNNNWNNXXNNNNNNNWWWWNNNNNNNNNNNNNNNNNWWNNWNNNNNXXXNNNNNWWNNWNNNNWWWXKOkxxxdxxxkO0KKKKXNNNNNNk'          ")      
print("               'o0XXXXXXXXXXXXXXXXNNNNNNNNWNWWNNNNNNNNNNNNNNNNNNNNNWWWWWWWNNNNNNNNXXXXXXXXNNNNNNNXXNWWNNNNWNNNNNXXXXXXXXXXNNNNNNNNNOc.          ")      
print("               ,d0KKKKKKKKKKXXXXXXXXNNNNXXNNNNNNNNNNNWWNNNNNWWWWWNNWWWNNNNXXXXXXXXXXXXXXXKKXNNNNXXXXNWWWNNNNNNNNNNNNNNNNNNNNNNNXXNNN0l.         ")     
print("                .'cx0000000KKKXXXXXXXXNNNXXXXXXXXXNXXNNNNNNNNNNXXXNNNNNXXXXXXXXXXXXXXXXKOdkKXXXNNNXXXNNNWWNWNNNNNNNNNNNNNNNXXXXXXXNNNXk'         ")     
print("                   .l00000KKKKKKXXXXXXXXXNXXKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK0kdlclkKXXXXXXXXXXXNNNWNNNNNNNNNNNNNNNXXXXXXXXNNXXO,          ")   
print("                    ,OK00000KKKKKKKXXXXXXXXXXXKKKKK00KXXXXXXXKXXXXXXXXXXXXXXXKOO00Oxdolclcclx0KXXXXXXXXXXXNNWNNNNNNNNNNNNNNXXXXXXNXXXXXXx.        ")    
print("                    .oK00000KKKKKKKXXXXXXXXXXXXKKKOoodkkOOkkxxkO0000OOO00Okxxdllolllllllclllldk000KKXXXXXXXXNWNNNNNNNXXXXXXXXKKXXXXXKxdOk;        ")    
print("                     ,kK000000KKKKKKXXXXXXXXXXKKKKxlccllllllllloooolllloollcclllloodddlcloddolloodk0KKKKXXXXXNNNNNXXXXXXXXXXXXXXXXXXXd..'.        ")    
print("                      ;kK00000KKK0KKKXXXXXXXXXKKK0dcclloooooooddoooooooooooooodddddddolcldddddollcloxOOO0KXXXXXNNNNNXXXXXXXXXXXXXXXXXO,           ")    
print("                       ,k00000000KKKKKXKKXXXXXKKK0dccllooooddddxxxxxxddddddxxxxxxxxxdolloddxxxddoollcllldk0KKKXXXXNNNNNNNXXXKKXXXXXXX0;        ")       
print("                        ,x000K0000K00KKKKKKXXXKKK0dclllooooddxxxxxxxxxxxxxxxxxxxxxxxdlloddxxxxxxdddoolllcloOKKKKKKKKKKKXXXXKKXXXXXXXX0,         ")      
print("                         'x00000000000KKKKKKXXKKKKxlllllooodddxxxxxxxxxxxxxxxxxxxxxdolldddxxxxxxxxxddolllclkKKKKKKKKKKKKKKKKXXKKKKKXXk.           ")    
print("                          .lO0000000000KKKKKKKKKKKkoclllloooddxxxxxxxxxxxxxxxxxxxxxdoloddxxxxxxxxxxdoolllcoOKKKKKKKKKKKKKXXXXKK0000KKc              ")  
print("                           .;x0000000K0000KK0KKKKK0dcllllloooddxxxxxxxxxxxxxxxxxxxxdooddxxxxxxxxxxddollllld0KKXKXXXXXXXXXXXXKK000000l.                ")
print("                             .lOK000kx0K00000KKKKKKOoclllllloooddxxxxxxxxxxxxxxxxxxdddxxxxxxxxxxxddollllclkKKXXXXXXXXXXXXXXKK00000k:.                 ")
print("                              .,dO0Ko':O0000000KKKKKOdlcclllllooodddxxxxxxxxxxxxxxxxxxxxxxxxxxxddolllllllx0KXXXXXXXKKKKXXXKK0Kk::l'                   ")
print("                                .,lko. 'd00000000K0KKOdlcllllllllooooddddddxxxxxxxxxxxxxxxxxdddoolllllllx0KKXXXXKKK0K0KKKKK0KO:                       ")
print("                                   ..   .:k000000000000kocclcllllllloooooooddddddddddddddddooollllllllok0KKXXKKKK000000KK000Oc.                       ")
print("                                          .ck00000KK000KOxolcccllllllllllooooooooooooooooolllllllllllxO0KKKKKK0000000000000Oc.                        ")
print("                                            .:d000000K0000OxdllccccclllllllllllllllllllllllllllllloxO000000000000000000000O:.                         ")
print("                                              .'cdO0000000000OkxollccclccclllcclllllllllllccclodxO0K000000000000000K0O000d'                           ")
print("                                                 .':ldO0K00000000OkxddolllcccccccccccclloodxkO00K000000000000000000x;,ld;.                            ")
print("                                                     ..;cdo;,lx00000000OOkkxxxxxxxxkkkkOO00KK000KK0O000000000000Oo;.                                  ")
print("                                                          .   .,cdk00000000000000000000000KK00kxoc;'l000000K0ko:.                                     ")
print("                                                                  .,:coxkOO0000000OOOOkxdoc:;'..    c0KK0Oxl;.                                        ")
print("                                                                       ...''',,,,''.....            .:c:,'.                                           ")
while t==0:
    i = rd.randint (0,j)
    print("¿ Tu campeón es", Rol[i],"?")
    rol = input()
    while y==0:
        if rol == "no" or rol=="si":
            y=1
        else:
            print("Por favor ingrese un dato valido, (si tiene dudas lea el manual de uso)")
            print("¿ Tu campeón es",Rol[i],"?")
            rol = input()
    if rol=="si":
        cursor.execute("CREATE TEMPORARY TABLE tabla1 (Nombre varchar(30),Region varchar(45),Tipo varchar(45), Asesino int,Luchador int,Mago int,Tirador int,Soporte int,Tanque int)")
        sql = "INSERT INTO tabla1 SELECT Nombre, Region,Tipo, Asesino, Luchador, Mago ,Tirador, Soporte, Tanque from campeones a WHERE a.Linea  = '{}'".format(Rol[i])
        cursor.execute(sql)
        cursor.execute("SELECT * FROM tabla1") 
        r = cursor.fetchall()
        t=1
        cursor.execute("SELECT Region FROM tabla1")
        r = cursor.fetchall()
        m=list(r)
        for num in m:
            ñ=str(num)
            m1=list(ñ)
            for m1 in num:
                text = m1[0]
            ñ="".join(m1)
            Region1.append(ñ)
        for item in Region1:
            if item not in Region:
                Region.append(item)
        cursor.execute("SELECT Tipo FROM tabla1")
        r = cursor.fetchall()
        m=list(r)
        for num in m:
            ñ=str(num)
            m1=list(ñ)
            for m1 in num:
                text = m1[0]
            ñ="".join(m1)
            Tipo1.append(ñ)
        for item in Tipo1:
            if item not in Kind:
                Kind.append(item)
    else:
        y=0
    Rol.pop(i)
    j=j-1
    if j<0:
        print("Lea por favor el manual de instrucciones y/o caracteristicas de los personajes")
        t=1
        t2=1
    
t1=0
numero = 1
reg=0
kin=0
tip=0
while t1==0 and t2==0:
    i = randrange (3)
    if i==0 and tip==0:
        numero=numero+1
        tabla = 'tabla'+ str(numero)
        Tablas.append(tabla)
        y=0
        j=len(Tipo)
        x = randrange(j)
        print("¿ Tu campeón es", Tipo[x],"?")
        rol = input()
        while y==0:
            if rol == "no":
                res=0
                y=1
            elif rol=="si":
                res=1
                y=1
            else:
                print("Por favor ingrese un dato valido, (si tiene dudas lea el manual de uso)")
                print("¿ Tu campeón es",Tipo[x],"?")
                rol = input()
        if rol == "no" or rol == "si":
            print(Tablas,tabla,Tablas[len(Tablas)-2])
            cursor.execute("CREATE TEMPORARY TABLE {}  (Nombre varchar(30),Region varchar(45),Tipo varchar(45), Asesino int,Luchador int,Mago int,Tirador int,Soporte int,Tanque int)".format(tabla))
            cursor.execute("INSERT INTO {} SELECT Nombre,Region,Tipo, Asesino, Luchador, Mago ,Tirador, Soporte, Tanque from {} a WHERE a.{} = {}".format(tabla,Tablas[len(Tablas)-2],Tipo[x], res))
            cursor.execute("SELECT * FROM {}".format(tabla)) 
            r = cursor.fetchall()
            if len(r)==1:
                cursor.execute("SELECT Nombre FROM {}".format(tabla))
                n = cursor.fetchall()
                fin = adivina(n)
                if (fin != 1):
                    print("Lo sentimos tu campeon no ha sido encontrado en nuestra base de datos")
                t1=1
                break
            elif len(r)==0:
                print("LO sentimos Tu campeon no ha sido encontrado en nuestra base de datos")
                t1=1
                break
        Tipo.pop(x)
        if j==1:
            tip=1

    
    elif i==1 and reg==0:
        y=0
        j=len(Region)
        x = randrange (j)
        print("¿ Tu campeón es de", Region[x],"?")
        rol1 = input()
        while y==0:
            if rol1 == "no" or rol1=="si":
                y=1
            else:
                print("Por favor ingrese un dato valido, (si tiene dudas lea el manual de uso)")
                print("¿ Tu campeón es de",Region[x],"?")
                rol1 = input()
        if rol1=="si":
            numero=numero+1
            tabla = 'tabla'+ str(numero)
            Tablas.append(tabla)
            cursor.execute("CREATE TEMPORARY TABLE {}  (Nombre varchar(30),Region varchar(45),Tipo varchar(45), Asesino int,Luchador int,Mago int,Tirador int,Soporte int,Tanque int)".format(tabla))
            cursor.execute("INSERT INTO {} SELECT Nombre, Region,Tipo, Asesino, Luchador, Mago ,Tirador, Soporte, Tanque from {} a WHERE a.Region = '{}'".format(tabla,Tablas[len(Tablas)-2],Region[x]))
            cursor.execute("SELECT * FROM {}".format(tabla)) 
            r = cursor.fetchall()
            reg=1
            if len(r)==1:
                cursor.execute("SELECT Nombre FROM {}".format(tabla))
                n = cursor.fetchall()
                fin = adivina(n)
                if (fin != 1):
                    print("Lo sentimos tu campeon no ha sido encontrado en nuestra base de datos")
                t1=1
                break
            j=j-1
        Region.pop(x)
        if j<0:
            print("Lea por favor el manual de instrucciones y/o caracteristicas de los personajes")
            t1=1
            break
    elif i==2 and kin==0:
        y=0
        j=len(Kind)
        x = randrange (j)
        print("¿ Tu campeón es", Kind[x],"?")
        rol1 = input()
        while y==0:
            if rol1 == "no" or rol1=="si":
                y=1
            else:
                print("Por favor ingrese un dato valido, (si tiene dudas lea el manual de uso)")
                print("¿ Tu campeón es",Kind[x],"?")
                rol1 = input()
        j=j-1
        if rol1=="si":
            kin=1
            numero=numero+1
            tabla = 'tabla'+ str(numero)
            Tablas.append(tabla)
            cursor.execute("CREATE TEMPORARY TABLE {}  (Nombre varchar(30),Region varchar(45),Tipo varchar(45), Asesino int,Luchador int,Mago int,Tirador int,Soporte int,Tanque int)".format(tabla))
            cursor.execute("INSERT INTO {} SELECT Nombre, Region,Tipo, Asesino, Luchador, Mago ,Tirador, Soporte, Tanque from {} a WHERE a.Tipo = '{}'".format(tabla,Tablas[len(Tablas)-2],Kind[x]))
            cursor.execute("SELECT * FROM {}".format(tabla)) 
            r = cursor.fetchall()
            if len(r)==1:
                cursor.execute("SELECT Nombre FROM {}".format(tabla))
                n = cursor.fetchall()
                fin = adivina(n)
                if (fin != 1):
                    print("Lo sentimos tu campeon no ha sido encontrado en nuestra base de datos")
                t1=1
                break
        Kind.pop(x)
        if j<0:
            print("Lea por favor el manual de instrucciones y/o caracteristicas de los personajes")
            t1=1
            break
    else:
        print("Lo sentimos tu campeon no ha sido encontrado en nuestra base de datos")
        t1=1
        break 
    