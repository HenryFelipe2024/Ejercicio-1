nombre=input("nombre completo del trabajador")
ventas_generadas_en_el_mes=float(input("cuanto han vendido en el mes"))
resultado=porcentaje_comision=ventas_generadas_en_el_mes*0.13
redondeo=round(resultado,2)
print(f"las comisiones serian {resultado}")