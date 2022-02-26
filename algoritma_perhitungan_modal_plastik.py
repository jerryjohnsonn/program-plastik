print("Kode : DP(UK)_IKAT|DP(UK)|S(UK)|B(UK)|L(UK)|N(UK)|")
print("Kode tanpa Ukuran : KYLO|BL|KMPP|PE_98|PE_SL|HD")

print("="*50)
print("Masukkan Kode Barang")
inp = input().split()

total = 0

for items in inp:
  if(items=="DP15"):
    total += 3200
  elif(items=="DP19"):
    total += 4500
  elif(items=="DP24"):
    total += 6000
  elif(items=="DP15_IKAT"):
    total += 32000
  elif(items=="DP19_IKAT"):
    total += 45000
  elif(items=="DP24_IKAT"):
    total += 60000
  elif(items=="DP27"):
    total += 10400
  elif(items=="DP30"):
    total += 15000
  elif(items=="DP35"):
    total += 21400
  elif(items=="S15"):
    total += 12000
  elif(items=="S19"):
    total += 12000
  elif(items=="S24"):
    total += 12000
  elif(items=="S27"):
    total += 12000
  elif(items=="S30"):
    total += 12000
  elif(items=="S35"):
    total += 12000
  elif(items=="B15"):
    total += 3100
  elif(items=="L19"):
    total += 6200
  elif(items=="L24"):
    total += 6200
  elif(items=="B27"):
    total += 6200
  elif(items=="KYLO"):
    total += 13500
  elif(items=="BL"):
    total += 11000
  elif(items=="N15"):
    total += 7200
  elif(items=="N19"):
    total += 7200
  elif(items=="N24"):
    total += 7200
  elif(items=="N27"):
    total += 14200
  elif(items=="N35"):
    total += 14200
  elif(items=="KMPP"):
    total += 30000
  elif(items=="PE_98"):
    total += 27500
  elif(items=="PE_SL"):
    total += 28500
  else:
    print(f"Kode {items} tidak ada didalam list harga")

print(total)
