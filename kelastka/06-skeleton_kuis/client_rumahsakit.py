
try : 
	while(True) :
		print ""
		print "Sistem Informasi Pasien"
		print "1. Masukkan data pasien"
		print "2. Lihat data pasien"
		print "3. Keluar"
		operasi = input("Pilih operasi : ")
		if operasi == "1" :
			print ""
			print "Masukkan data pasien"
			nik = raw_input("NIK : ")
			nama = raw_input("Nama : ")
			alamat = raw_input("Alamat : ")
			penyakit = raw_input("Penyakit : ")
			poli = input("Pilihan poli : 1) Umum, 2) Jantung, 3) Paru : ")

		elif operasi == "2" :
			print ""
			nik = input("NIK Pasien : ") 
			print "Data Pasien dengan NIK "+ nik
			
		else :
			print ""
			print "Keluar dari program"
			break
except KeyboardInterrupt :
	print("Keluar dari program")