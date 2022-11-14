## ACADEMIC RECORDS

## RECORD NILAI MATEMATIKA SMA NEGERI 007

list_murid = [
    {
        'nama': 'Agus',
        'nilai': 85
    },
    {
        'nama': 'Bagus',
        'nilai': 90
    },
    {
        'nama': 'Cecep',
        'nilai': 65
    }
]

## KONFIRMASI TAMBAH MURID BARU

def konfirmasi_murid_baru():
    while True:
        user_input = input('\nKetik Y jika anda yakin, dan N untuk membatalkan penambahan murid: ').upper()

        if user_input == 'Y':
            print(f'Murid berhasil ditambahkan ke database.')
            daftar_murid()
            break
        elif user_input == 'N':
            print('Murid tidak berhasil ditambahkan ke database.')
            break
        else:
            user_input
            break

## MENAMPILKAN MENU DAFTAR MURID

def daftar_murid():
    print('\n----- Daftar Nilai Matematika SMAN 007 -----')
    print('No. Index Murid\t|Nama\t\t\t|Nilai Ujian')

    for index, item in enumerate(list_murid):
        print(f"{index}\t\t|{item['nama']}\t\t\t|{item['nilai']}\t")


## MENAMPILKAN MENU TAMBAH MURID
def tambah_data_murid():

    while True:
        user_input = input('Masukkan nama murid: ').capitalize()
        for name in list_murid:
            if (name['nama'] == user_input):
                break

        while name['nama'] != user_input:
            math_score = int(input('Masukkan nilai ujian Matematika (0-100): '))
            if math_score > 100:
                print('Masukkan nilai yang sesuai')
                math_score
                continue
            else:
                break         
        break

    for item in list_murid:
        if item['nama'] == user_input:
            break
        else:
            konfirmasi_murid_baru()
            list_murid.append({
                'nama': user_input,
                'nilai': math_score
            })
        break

    daftar_murid()
    menu_utama()


## MENGHAPUS DATA MURID DARI DATABSE 

def hapus_data_murid():
    daftar_murid()

    while True:
        no_absen = input('Masukkan nomor index murid yang akan dihapus: ')
        if no_absen.isdigit() == False:
            print('Masukkan nomor index murid yang sesuai: ')
            no_absen
        else:
            no_absen = int(no_absen)
            if no_absen not in range(len(list_murid)+1):
                print(f'Nomor index {no_absen} tidak ada pada database. Silahkan masukkan nomor absen yang sesuai.')
                no_absen
                break
            else:
                print(f'\nHapus data murid absen {no_absen}? (Y/N)')

                while True:
                    user_input = input('\nKetik Y jika anda yakin, dan N untuk membatalkan: ').upper()
                    if user_input == 'Y':
                        break
                    elif user_input == 'N':
                        menu_utama()
                    else:
                        print('Input tidak sesuai. Silahkan masukkan kembali input yang sesuai')
                        user_input
                    break
    
        del list_murid[no_absen] 

        daftar_murid()
        menu_utama()

## MENGUPDATE NILAI DI DATABASE

def update_nilai():
    daftar_murid()
    x = True
    while x ==  True: 
        user_input = input('Masukkan nama murid yang mau diupdate nilainya: ').capitalize()
        for i in range(len(list_murid)):
            if list_murid[i]['nama'] == user_input:
                user_input2 = int(input('Masukkan nilai remedial: '))
                if user_input2 > 100:
                    print('Input tidak sesuai, silahkan masukkan input yang valid')
                    break
                    x = False
                else:
                    list_murid[i]['nilai'] = user_input2
                    daftar_murid()
                    break
                    x = False
            else:
                continue
        print('Tidak ada murid dalam databse, Silahkan input nama murid yang ada pada daftar.')
        user_input2 = input('Apakah anda ingin tetap mengupdate data murid? (Ya/Tidak): ').capitalize()
        user_input
        x = False


def menu_utama():

    while True:
        pilih_menu = input('''
        Selamat datang di database nilai Matematika SMA Negeri 007
        
        List Menu:
        1. Melihat Daftar Murid
        2. Menambahkan Murid Baru
        3. Menghapus Data Murid
        4. Memasukkan Nilai Remedial
        5. Exit Program
        
        Silahkan pilih nomor menu: ''')

        print()
        if pilih_menu == '1':
            daftar_murid()
        elif pilih_menu == '2':
            tambah_data_murid()
        elif pilih_menu == '3':
            hapus_data_murid()
        elif pilih_menu== '4':
            update_nilai()
        elif pilih_menu == '5':
            break
        else:
            print('Masukkan kembali nomor menu yang akan diakses.')
            pilih_menu

menu_utama()

        