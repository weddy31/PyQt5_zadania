from PyQt5.QtWidgets import(
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QLineEdit,
    QWidget,
    

) 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random as rd
import sys
from datetime import datetime
import folium
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
     


class MyTabWidget(QWidget):
    def __init__(self):
        super().__init__()
    

        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(200, 200)

        self.tabs.addTab(self.tab1, "Zapis danych")
        self.tabs.addTab(self.tab2, "Wyswietlenie danych")
        self.tabs.addTab(self.tab3, "Mapa")

        self.tab1.layout = QVBoxLayout(self)
        self.line1 = QLineEdit(self)
        self.line1.move(10,20)
        self.line1.resize(50,50)
        self.savebutton = QPushButton("Zapisz", self)
        self.savebutton.clicked.connect(self.save1)
        self.savebutton.resize(200,32)
        self.savebutton.move(100,200)
        self.nameLabel1 = QLabel(self)
        self.nameLabel1.setText("Wprowadź tekst: ")
        self.nameLabel1.resize(200,32)
        self.nameLabel1.move(100,10)
        self.tab1.layout.addWidget(self.nameLabel1)
        self.tab1.layout.addWidget(self.line1)
        self.tab1.layout.addWidget(self.savebutton)
        self.tab1.setLayout(self.tab1.layout)

        self.tab2.layout = QVBoxLayout(self)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText("Wynik z pliku: ")
        self.nameLabel2.move(100,200)
        self.nameLabel2.resize(200,32)

        self.savebutton1 = QPushButton("Wyswietl", self)
        self.savebutton1.clicked.connect(self.getfile)
        self.savebutton1.resize(200,32)
        self.savebutton1.move(100,200)
         
        self.tab2.layout.addWidget(self.savebutton1)
        self.tab2.layout.addWidget(self.nameLabel2)
        self.tab2.setLayout(self.tab2.layout)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
        self.tab3.layout = QVBoxLayout(self)

        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText("Dane dla mapy: ")
        self.savebutton1.resize(200,32)
        self.savebutton1.move(100,200)

        self.savebutton2 = QPushButton("Wyszukaj dane dla mapy", self)
        self.savebutton2.clicked.connect(self.getfile_map)
        self.savebutton2.resize(200,32)
        self.savebutton2.move(100,200)
         

        self.tab3.layout.addWidget(self.nameLabel3)
        self.tab3.layout.addWidget(self.savebutton2)
        self.tab3.setLayout(self.tab3.layout)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    #funkcja wpisujaca dane do pliku - dlugosc,szerokosc geograficzna, data i notatka
    def save1(self):
        dt = datetime.now()
        time = dt.strftime("%H-%M-%S")
        lat = rd.uniform(1,100) #szerokosc generowana losowo w zakresie od 1 do 100
        lng = rd.uniform(1,100) #dlugosc generowana losowo w zakresie od 1 do 100
        
        with open (str(time) + '.txt', 'w') as f:
            f.write(self.line1.text() + ' ' + time + ' lat: ' + str(lat) + ' lng: ' + str(lng)  )
     
    #file explorer i wyswietlenie danych 
    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "Image Files (*.txt)")
        ffile = fname[0]
        try:
            with open(ffile, 'r') as file:
                self.nameLabel2.setText("Wynik z pliku: " + str(file.readline()) )
        except:
            self.nameLabel2.setText("Nie wybrano zadnego pliku!")
        
                
            #print(str(file.readline()))
            
    #file explorer i dane dla mapy        
    def getfile_map(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "Image Files (*.txt)")
        ffile = fname[0]
        try:
            with open(ffile, 'r') as file:
                read = file.readline()
                split_text = read.split()
                lng = split_text[3]
                lat = split_text[5]
                self.nameLabel3.setText("Dane dla mapy: " + str(lng) + ' ' + str(lat))              
        except:
            self.nameLabel3.setText("Nie wybrano zadnego pliku!")
    #Mapa     
        map = folium.Map(location=[lng, lat])
        folium.Marker(location=[lng, lat], popup=str(split_text[0])).add_to(map)
        
        
        map.save("mapa.html")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window1 = MyTabWidget()

    window1.show()
    app.exec_()