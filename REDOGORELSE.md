# 

Jag låter funktionerna ta emot listan med servrar som parameter i stället för att använda en global variabel. På så sätt blir det tydligt vilka data funktionen arbetar med och funktionerna blir enklare att återanvända. Detta används bland annat i meny.py där funktioner som visar eller ändrar servrar arbetar mot den lista som skickas in från main.py.