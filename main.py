import csv

csv_filename = 'mahasiswa.csv'



loopmaster=True
while loopmaster:
    print ("MENU")
    print ("1. Melihat Data 2. Menambah Data")
    pilihan = int (input ("Masukkan pilihan: "))

    if pilihan == 1 :
        # tentukan lokasi file, nama file, dan inisialisasi csv

        f = open('mahasiswa.csv', 'r')
        reader = csv.reader(f)

        # membaca baris per baris
        for row in reader:
            print (row)        
        
    elif pilihan == 2 :
        print ("MENU TAMBAH DATA \n ==========================")

        loop = True
        while loop:
            data1 = input ("Masukkan Nama: ")
            data2 = input ("Masukkan NIM: ")
         
          
            with open(csv_filename, mode='a') as csv_file:
                fieldnames = ['Nama', 'Nim']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
          
                writer.writerow({'Nama' : data1, 'Nim' : data2})
              
            ulangi = input ("Mau menambah data lagi ? (y/n) :" )
            if ulangi == 'n' :
                loop = False
    
          
      
    print ("")
    lagi = input ("Mau kembali ke menu ? (y/n) : ")
    if lagi == 'n' :
        loopmaster = False





