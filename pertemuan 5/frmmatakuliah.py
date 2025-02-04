import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from matakuliah import Matakuliah
import os

class FormMatakuliah:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("380x540")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Kode MK :').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtNIM = Entry(mainFrame) 
        self.txtNIM.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNIM.bind("<Return>",self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='Nama MK :').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='SKS :').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.sks = StringVar()
        Cbo = ttk.Combobox(mainFrame, width = 18, textvariable = self.sks) 
        Cbo.grid(row=2, column=1, padx=5, pady=5)
        Cbo['values'] = ('1','2','3','4','5','6')
        Cbo.current()                                                  

        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        self.btnCari = Button(mainFrame, text='Cari', command=self.onCari, width=10)
        self.btnCari.grid(row=3, column=3, padx=5, pady=5)               

        # define columns
        columns = ('idmhs', 'kodemk', 'namamk','sks')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idmhs', text='ID')
        self.tree.column('idmhs', width="30")
        self.tree.heading('kodemk', text='kode MK')
        self.tree.column('kodemk', width="60")
        self.tree.heading('namamk', text='Nama MK')
        self.tree.column('namamk', width="200")
        self.tree.heading('sks', text='SKS')
        self.tree.column('sks', width="30")
        # set tree position
        self.tree.place(x=0, y=280)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtNIM.delete(0,END)
        self.txtNIM.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")       
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        mhs = Matakuliah()
        result = mhs.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        kodemk = self.txtNIM.get()
        mhs = Matakuliah()
        res = mhs.getByNIM(kodemk)
        rec = mhs.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNama.focus()
        return res
        
    def TampilkanData(self, event=None):
        kodemk = self.txtNIM.get()
        mhs = Matakuliah()
        res = mhs.getByNIM(kodemk)
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, mhs.namamk)
        self.sks.set(mhs.sks)                           
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kodemk = self.txtNIM.get()
        namamk = self.txtNama.get()
        sks = self.sks.get()
        mhs = Matakuliah()
        mhs.kodemk = kodemk
        mhs.namamk = namamk
        mhs.sks = sks
        if(self.ditemukan==True):
            res = mhs.updateByNIM(kodemk)
            ket = 'Diperbarui'
        else:
            res = mhs.simpan()
            ket = 'Disimpan'
            
        rec = mhs.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kodemk = self.txtNIM.get()
        mhs = Matakuliah()
        mhs.kodemk = kodemk
        if(self.ditemukan==True):
            res = mhs.deleteByNIM(kodemk)
            rec = mhs.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    os.system('cls')
    root = tk.Tk()
    aplikasi = FormMatakuliah(root, "Aplikasi Data Mahasiswa")
    root.mainloop() 