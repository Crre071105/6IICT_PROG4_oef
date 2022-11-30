fruit_lijst = ["Appel", "Banaan", "Kers"]

try:
    getal = input( "Geef een getal: " )
    if "." in getal:
        getal = float( getal )
    else:
        getal = int( getal )
    print( fruit_lijst[getal] )
except ValueError:
    print( "schrijf een cijfer" )  
except KeyboardInterrupt:
    print ("druk geen ctrl + c")


print("Programma klaar")  
