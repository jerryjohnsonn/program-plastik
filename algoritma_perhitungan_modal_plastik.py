print("Masukkan Kode Barang")
inp = input().split()

total = 0

for items in inp:
  if(items=="dp15"):
    total += 3200
  elif(items=="dp19"):
    total += 4500
  elif(items=="dp24"):
    total += 6000
  elif(items=="dp15 1ikat"):
    total += 32000
  elif(items=="dp19 1ikat"):
    total += 45000
  elif(items=="dp24 1ikat"):
    total += 60000
  elif(items=="dp27"):
    total += 10400
  elif(items=="dp30"):
    total += 15000
  elif(items=="dp35"):
    total += 21400
  elif(items=="s15"):
    total += 12000
  elif(items=="s19"):
    total += 12000
  elif(items=="s24"):
    total += 12000
  elif(items=="s27"):
    total += 12000
  elif(items=="s30"):
    total += 12000
  elif(items=="s35"):
    total += 12000
  
  else:
    print(f"Data {items} tidak ada didalam list harga")

print(total)