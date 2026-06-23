value=float(input("Enter a value for unit conversion(meters, km, cm, inches, miles, feet): "))
km_meter=value*1000
meter_km=value/1000
inches_cm=value*2.54
cm_inches=value/2.54
feet_meter=value*0.3084
meter_feet=value/0.3084
mile_km=value*1.60934
km_mile=value/1.60934
print("Kilometers -> Meters(km*1000):", km_meter)
print("Meters -> Kilometers(meters/1000):", meter_km)
print("Inches -> Centieters(inches*2.54):", inches_cm)
print("Centimeters -> Inches:(cm/2.54)", cm_inches)
print("Feet -> Meters(feet*0.3804):", feet_meter)
print("Meters -> Feet(meter/0.3804):", meter_feet)
print("Miles -> Kilometers(miles*1.60934):", mile_km)
print("Kilometers -> Miles(km/1.60934):", km_mile)