
try : 
	while(True) :
		print("Sistem Informasi Pasien")
		print("1. Masukkan data pasien")
		print("2. Lihat data pasien")
		print("3. Keluar")
		operasi = input("Pilih operasi : ")
		if operasi == "1" :
			print("Masukkan data pasien")
			nik = input("NIK : ")
			nama = input("Nama : ")
			alamat = input("Alamat : ")
			penyakit = input("Penyakit : ")

		elif operasi == "2" :
			nik = input("NIK Pasien : ") 
			print("Data Pasien dengan NIK "+ nik)
			
		else :
			print("Keluar dari program")
			break
except KeyboardInterrupt :
	print("Keluar dari program")