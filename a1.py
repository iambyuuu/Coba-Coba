class alamat:
          def __init__(self, desa, kec, kab):
                    self.desa=desa
                    self.kec=kec
                    self.kab=kab

          def tampilAlamat (self):
                    return ("Desa: "+self.desa+", Kecamatan: "+self.kec+", Kabupaten: "+self.kab)