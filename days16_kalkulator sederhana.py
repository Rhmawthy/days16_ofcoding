#kalkulator sederhana menggunakan percabangan dan 7 operator aritmatika
angka_1 = int(input("masukkan angka pertama :"))
operator = input(" + , -, * , /, **, //, %, : ")
angka_2 = int(input("masukkan angka kedua :"))

#operator penjumlahan
if operator == "+":
    print ("hasil = ",angka_1 + angka_2)
    
#operator pengurangan
elif operator == "-":
    print ("hasil = ",angka_1 _ angka_2)
    
#operator perkalian
elif operator == "*":
    print ("hasil = ",angka_1 * angka_2)
    
#operator pembagian
elif operator == "/":
    print ("hasil = ",angka_1 / angka_2)
    
#operator pangkat
elif operator == "**":
    print ("hasil = ",angka_1 ** angka_2)

#operator pembagian bulat
elif operator == "//":
    print ("hasil = ",angka_1// angka_2)

#operator sisah bagi
elif operator == "%":
    print ("hasil = ",angka_1 % angka_2)

else:
    print("data yang anda masukkan salah")





