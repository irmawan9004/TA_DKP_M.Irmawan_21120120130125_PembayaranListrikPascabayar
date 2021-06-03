from tkinter import * 
from tkinter import ttk
import tkinter.messagebox as m


class Tagihanlis():
    def __init__(self, email, password,daya,golongan,harga,kmawal,kmakhir,totalm,tagihan,uang,close):
        self.email = email
        self.password = password
        self.daya = daya
        self.golongan = golongan
        self.harga = harga
        self.kmawal = kmawal
        self.kmakhir = kmakhir
        self.totalm = totalm
        self.tagihan = tagihan
        self.uang = uang
        
    
    def getDaya(self):
        return self.daya
    def getKmawal(self):
        return self.kmawal
    def getKmakhir(self):
        return self.kmakhir
    def getUang(self):
        return self.uang
    def getHarga(self):
        return self.harga
    def getGolongan(self):
        return self.golongan
        

Listrik1 = Tagihanlis("","",0,0,0,0,0,0,0,0,0,)
def masuk():

    nomorid = inomor.get()
    namapelanggan = inama.get()
    if(nomorid == "21120120130125" and namapelanggan == "irmawan"):
        m.showinfo('Sukses', 'Nomor Id dan Password yang anda masukkan benar!')
        return
    else:
        m.showwarning('Failed','Nomor Id dan Password yang anda masukkan salah!')
        return

def daya():
    global totaltagihan
    km_awal = Listrik1.getKmawal()
    km_akhir = Listrik1.getKmakhir()
    km_awal = iawal.get()
    km_akhir = iakhir.get()
    harga = Listrik1.getHarga()
    golongan = Listrik1.getGolongan()
    dikali = 0
    totalmeter = 0
    totaltagihan = 0
    if dayalistrik.get() == '450V':
        harga = "\t\tRp.196"
        golongan = "\t\tR1/TR"
        dikali = 196
    elif dayalistrik.get() == '900V':
        harga = "\t\tRp.274"
        golongan = "\t\tR1M/TR"
        dikali = 274
    elif dayalistrik.get() == '1300V':
        harga = "\t\tRp.1352"
        golongan = "\t\tR1/M"
        dikali = 1352
    elif dayalistrik.get() == '3500V':
        harga = "\t\tRp.1444"
        golongan = "\t\tR2/TR"
        dikali = 1444
    if(km_awal == "" and km_akhir == ""):
        m.showinfo('Info', 'KM AWAL dan KM AKHIR harap Diisi!')
    elif(km_awal >= km_akhir):
        m.showinfo('Info,KM Akhir harus lebih besar')
    elif(km_akhir > km_awal):
        totalmeter = (int(km_akhir) - int(km_awal))
        totaltagihan = totalmeter * dikali
    print(totalmeter)
    print(totaltagihan)
    print(harga)
    print(golongan)
    lbkk = Label(text = "Harga per Kwh\t:"+str(harga),background = "darkgrey")
    lbkk.place(x=30,y=310)
    lbgl = Label(text = "Golongan\t:"+str(golongan),background = "darkgrey")
    lbgl.place(x=30,y=350)
    lbtt = Label(text = "Total Meter\t:\t\t"+str(totalmeter),background = "darkgrey")
    lbtt.place(x=30,y=390)
    ltag = Label(text = "Total Tagihan\t:\t\tRp."+str(totaltagihan),background = "darkgrey")
    ltag.place(x=30,y=430)
    lbkk = Label(text = "Harga per Kwh\t:",background = "yellow")
    lbkk.place(x=30,y=310)
    lbgl = Label(text = "Golongan\t:",background = "yellow")
    lbgl.place(x=30,y=350)
    lbtt = Label(text = "Total Meter\t:",background = "yellow")
    lbtt.place(x=30,y=390)
    ltag = Label(text = "Total Tagihan\t:",background = "yellow")
    ltag.place(x=30,y=430)


    

     
    
 
def membayar():
    
    nominal = Listrik1.getUang()
    nominal = inom.get()
    if(nominal == "" ):
        m.showinfo('Info','Anda Belum mengisi Uang ')
    elif(int(nominal) < int(totaltagihan)):
        m.showinfo('Info','Uang Anda Kurang')
    elif(int(nominal) >= int(totaltagihan)):
        kembali = (int(nominal) - int(totaltagihan))
        pesan = "Kembali = Rp." + str(kembali)
        m.showinfo("Info",pesan)

def close():
    main_window.destroy()
    m.showinfo('Info', 'Terima Kasih')


main_window = Tk()  
main_window.geometry("800x600")
main_window.title("Masukkan Data")
main_window['bg'] = 'darkgrey'


#creating label  
lbnama = Label(main_window, text = "Nama Pelanggan\t:",background = "yellow")
lbnama.place(x = 30,y = 20)    
lbjk = Label(text = "NomorID\t:",background = "yellow")
lbjk.place(x = 30, y=60)
lbbb = Label(text = "Pilih Daya Listrik\t:",background = "yellow")
lbbb.place(x=30,y=130)
lbgl = Label(text = "Golongan\t:",background = "yellow")
lbgl.place(x=30,y=350)
lbkk = Label(text = "Harga per Kwh\t:",background = "yellow")
lbkk.place(x=30,y=310)
lbjm = Label(text = "Kwh Awal\t:",background = "yellow")
lbjm.place(x=30,y=170)
lbmb = Label(text = "Kwh Akhir\t:",background = "yellow")
lbmb.place(x=30,y=210)
lbtt = Label(text = "Total Meter\t:",background = "yellow")
lbtt.place(x=30,y=390)
ltag = Label(text = "Total Tagihan\t:",background = "yellow")
ltag.place(x=30,y=430)
lnom = Label(text = "Uang Anda\t:",background = "yellow")
lnom.place(x = 30, y=500)

#create input  
inama = StringVar()
inama = Entry(main_window,width = 40,)
inama.place(x = 200, y = 20, ) 
inomor = IntVar()
inomor = Entry(main_window,width = 40,)
inomor.place(x = 200, y = 60)  
km_awal=IntVar()
iawal = Entry(main_window,width = 40, )
iawal.place(x = 200, y = 170)
Km_akhir =IntVar()
iakhir = Entry(main_window,width = 40, )
iakhir.place(x = 200, y = 210)
nominal = DoubleVar()
inom = Entry(main_window,width = 40, )
inom.place(x = 200,y = 500)


#create combobox
dayalistrik = StringVar(value='450V') 
Cb1 = ttk.Combobox(main_window, width = 17, textvariable = dayalistrik, state="readonly")
Cb1.place(x=200, y=130)

# Adding combobox drop down list 
Cb1['values'] = ('450V' ,
                 '900V',
                 '1300V',
                 '3500V' ) 

#create button
btn = Button(main_window,text = 'Check',command = masuk)
btn.place(x = 400 , y = 85)
btn1 = Button(main_window, command = daya, text="Hitung")
btn1.place(x=400,y=235)
btn2 = Button(main_window, command = membayar, text = "Bayar")
btn2.place(x = 400, y = 525)
btn3 = Button(main_window,command = close,text = "Keluar")
btn3.place(x = 740, y = 560)


main_window.mainloop()    

