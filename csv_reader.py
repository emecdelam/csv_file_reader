import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import e, sin, pi, cos, tan
from matplotlib.font_manager import FontProperties
import random
import traceback as tr
import os

font = FontProperties()
font.set_family('serif')
font.set_size('20')
colors = ['r', 'g', 'b', 'k','c','m','y']


class PlotWindow:
    #==============
    # Names and var
    #==============

    __xlabel = " Temps [ us ]"
    __ylabel = " Tension [ V ] "
    __name = " Signal data "
    def __init__(self, master):
        self.offset_1 = 0
        self.offset_2 = 0
        self.file_path = []
        self.highlight = None
        self.highlight2 = None
        self.unvalid = False
        self.function = []
        self.func_check = False
        fig,self.ax = plt.subplots()
        fig.suptitle(self.__name)
        master.title("Matplotlib plot")
        self.canvas = FigureCanvasTkAgg(fig, master=master)

        button_erase = tk.Button(master, text="Erase", command=self.erase)
        button_erase.pack(side=tk.TOP)
        button_erase.place(x=250, y=50)
        button_zoomplus = tk.Button(master, text="Zoom - ", command=self.zoomplus)
        button_zoomplus.pack(side=tk.TOP)
        button_zoomplus.place(x=550,y=50)
        button_zoommoins = tk.Button(master, text="Zoom +", command=self.zoommoins)
        button_zoommoins.pack(side=tk.TOP)
        button_zoommoins.place(x=550,y=75)
        button_load = tk.Button(master, text="Load File", command=self.load_file)
        button_load.pack(side=tk.TOP)
        button_load.place(x=350, y=50)
        button_line1 = tk.Button(master, text="Highlight", command=self.highlighting)
        button_line1.pack(side=tk.TOP)
        button_line1.place(x=700,y=50)
        button_line2 = tk.Button(master, text="Highlight2", command=self.highlighting2)
        button_line2.pack(side=tk.TOP)
        button_line2.place(x=700,y=75)
        button_zoom_droit = tk.Button(master, text="zoom x",command=self.zoom_droit)
        button_zoom_droit.pack(side=tk.TOP)
        button_zoom_droit.place(x=600, y=50)
        button_zoom_gauche = tk.Button(master, text="zoom y", command=self.zoom_gauche)
        button_zoom_gauche.pack(side=tk.TOP)
        button_zoom_gauche.place(x=600, y=75)
        self.entry = tk.Entry(master)
        self.entry.pack(side=tk.TOP)
        self.entry.place(x=775,y=50)
        self.entry2 = tk.Entry(master)
        self.entry2.pack(side=tk.TOP)
        self.entry2.place(x=775,y=75)
        button_draw_func = tk.Button(master, text="Draw", command=self.get_function)
        button_draw_func.pack(side=tk.TOP)
        button_draw_func.place(x=350, y=75)
        self.scale_b = tk.Entry(master)
        self.scale_b.pack(side=tk.TOP)
        self.scale_b.place(x=1600,y=50)
        self.scale_g = tk.Entry(master)
        self.scale_g.pack(side=tk.TOP)
        self.scale_g.place(x=1600,y=75)
        self.func = tk.Entry(master)
        self.func.pack(side=tk.TOP)
        self.func.place(x=390, y=75)
        button_pad_haut = tk.Button(master,text='↑',command=self.pad_haut)
        button_pad_haut.pack(side=tk.TOP)
        button_pad_haut.place(x=1300,y=25)
        button_pad_bas = tk.Button(master, text='↓', command=self.pad_bas)
        button_pad_bas.pack(side=tk.TOP)
        button_pad_bas.place(x=1300, y=75)
        button_pad_droite = tk.Button(master, text='→', command=self.pad_droite)
        button_pad_droite.pack(side=tk.TOP)
        button_pad_droite.place(x=1315, y=50)
        button_pad_gauche = tk.Button(master, text='←', command=self.pad_gauche)
        button_pad_gauche.pack(side=tk.TOP)
        button_pad_gauche.place(x=1280, y=50)
        button_scale_bas = tk.Button(master,text='Time scale',command=self.scale_bas)
        button_scale_bas.pack(side=tk.TOP)
        button_scale_bas.place(x=1500, y=50)
        button_scale_gauche = tk.Button(master,text='Unit scale',command=self.scale_gauche)
        button_scale_gauche.pack(side=tk.TOP)
        button_scale_gauche.place(x=1500, y=75)
        button_text_offset_1 = tk.Button(master, text="Offset 1", command=self.offset)
        button_text_offset_1.pack(side=tk.TOP)
        button_text_offset_1.place(x=950, y=50)
        button_text_offset_1 = tk.Button(master, text="Offset 2", command=self.offset)
        button_text_offset_1.pack(side=tk.TOP)
        button_text_offset_1.place(x=950, y=75)
        self.offset_1_entry = tk.Entry(master)
        self.offset_1_entry.pack(side=tk.TOP)
        self.offset_1_entry.place(x=1000, y=50)
        self.offset_2_entry = tk.Entry(master)
        self.offset_2_entry.pack(side=tk.TOP)
        self.offset_2_entry.place(x=1000, y=75)



        self.canvas.draw()

        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    def offset(self):
        if self.offset_1_entry.get() != '':
            self.offset_1 = float(self.offset_1_entry.get())
        if self.offset_2_entry.get() != '' :
            self.offset_2 = float(self.offset_2_entry.get())
        plt.cla()
        for i in range(len(self.file_path)):
            self.draw(file_path=self.file_path[i])
    def get_function(self):
        entry = self.func.get()
        self.function.append(entry)
        for i in range(len(self.file_path)):
            self.draw(file_path=self.file_path[i])
        if self.func_check:
            print('\033[92mSuccessfully drawn the function y= \t{',str(entry),'}\033[0m')
    def pad_haut(self):
        plt.cla()
        for i in range(len(self.file_path)):
            self.draw(file_path=self.file_path[i],pad_haut=True)
    def pad_bas(self):
        plt.cla()
        for i in range(len(self.file_path)):
            self.draw(file_path=self.file_path[i],pad_bas=True)
    def pad_droite(self):
        plt.cla()
        for i in range(len(self.file_path)):
            self.draw(file_path=self.file_path[i],pad_droit=True)
    def pad_gauche(self):
        plt.cla()
        for i in range(len(self.file_path)):
            self.draw(file_path=self.file_path[i],pad_gauche=True)
    def zoom_gauche(self):
        plt.cla()
        for i in range(len(self.file_path)):
            self.draw(file_path=self.file_path[i],zoomgauche=True)
    def zoom_droit(self) :
        plt.cla()
        for i in range(len(self.file_path)):
            self.draw(file_path=self.file_path[i],zoomdroit=True)
    def zoomplus(self):
        plt.cla()
        for i in range(len(self.file_path)):
            self.draw(file_path=self.file_path[i],zoomplus=True)
    def zoommoins(self):
        plt.cla()
        for i in range(len(self.file_path)):
            self.draw(file_path=self.file_path[i],zoommoins=True)
    def scale_bas(self):
        plt.cla()
        entry = float(self.scale_b.get())
        for i in range(len(self.file_path)):
            self.draw(file_path=self.file_path[i],scale_bas=entry)
    def scale_gauche(self):
        plt.cla()
        entry = float(self.scale_g.get())
        for i in range(len(self.file_path)):
            self.draw(file_path=self.file_path[i],scale_gauche=entry)
    def erase(self):
        plt.cla()
        self.file_path = []
        self.highlight = None
        self.highlight2 = None
        self.offset_1 = 0
        self.offset_2 = 0
        self.unvalid = False
        self.function = []
        self.canvas.draw()
        self.ax.set_xlabel(self.__xlabel)
        self.ax.set_ylabel(self.__ylabel)
        print('\033[92mSuccessfully erased the plot\033[0m\n')
    def highlighting(self):
        entry = self.entry.get()
        try:
            self.highlight = float(entry)
            plt.clf()
            for i in range(len(self.file_path)):
                self.draw(file_path=self.file_path[i])
            print('\033[92mSuccessfully drawn the highlight y = \t\t\t{', f"{entry}", '}\033[0m')
        except:
            print('\033[91mUnvalid input, your input was' ,f'{entry!r}','\033[0m')
    def highlighting2(self):
        entry = self.entry2.get()
        try:
            self.highlight2= float(entry)
            plt.clf()
            for i in range(len(self.file_path)):
                self.draw(self.file_path[i])
            print('\033[92mSuccessfully drawn the second highlight y = \t{',f'{entry}','}\033[0m')
        except:
            print('\033[91mUnvalid input, your input was' ,f'{entry!r}','\033[0m')
    def load_file(self):
        entry = filedialog.askopenfilename(parent=root, title='Choose a file')
        try:
            color1 = random.choice(colors)
            colorbis = colors.copy()
            colorbis.remove(color1)
            self.file_path.append([entry,color1,random.choice(colorbis)])
            plt.cla()
            for i in range(len(self.file_path)):
                self.draw(file_path=self.file_path[i])
            if not self.unvalid:
                print('\033[92mSuccessfully loaded the file \t\t\t\t\t{',f"{entry}",'}\033[0m')
        except:
            print(tr.format_exc())
    def draw(self,file_path,zoomplus=False,zoommoins=False,pad_haut=False,pad_bas=False,pad_droit=False,pad_gauche=False,zoomdroit=False,zoomgauche=False,scale_bas=1.0,scale_gauche=1.0):

        try:
            with open(file_path[0], 'r') as file_in :
                file = file_in.readlines()
                data=[]
                for line in file[3:]:
                    line = line.replace('\n','')
                    #line = line.replace(',','.')
                    line = line.split('.')
                    data.append(line)
            file_name = os.path.basename(file_path[0])


            data_arr = np.array(data, dtype=np.float32)

            number_of_graphs = len(data[0])-1
            if number_of_graphs < 2:
                time, signal1 = data[0:len(data) - 1, 0], data[0:len(data) - 1, 1]
                signal1 /= scale_gauche
                time /= scale_bas
                if len(self.file_path) > 1:
                    if file_path == self.file_path[1]:
                        time += self.offset_1
                elif len(self.file_path) > 2:
                    if file_path == self.file_path[2]:
                        time += self.offset_2

                self.ax.plot(time, signal1, label=file_name, color=file_path[1])

            else:
                time, signal1, signal2 = data_arr[:-1, 0], data_arr[:-1, 1], data_arr[:-1, 2]
                time=time/scale_bas

                signal1 = signal1/scale_gauche
                signal2 = signal2/scale_gauche
                if len(self.file_path) > 1:
                    if file_path == self.file_path[1]:

                        time += self.offset_1

                elif len(self.file_path) > 2:
                    if file_path == self.file_path[2]:
                        time += self.offset_2

                self.ax.plot(time, signal2, label=file_name, color=file_path[1])
                self.ax.plot(time, signal1, label=file_name, color=file_path[2])


            if self.highlight != None:
                jonction_x = (time[0],time[len(time)-1])
                jonction_y = (self.highlight,self.highlight)
                plt.plot(jonction_x, jonction_y, label='Jonction', color='y')
            if self.highlight2 != None:
                jonction_x = (time[0],time[len(time)-1])
                jonction_y = (self.highlight2,self.highlight2)
                plt.plot(jonction_x,jonction_y,label='Jonction2',color='c')
            if zoomdroit:
                scale = abs(self.ylim[0] - self.ylim[1]) / abs(self.xlim[0] - self.xlim[1])
                scale = 2 * scale
                plt.xlim(self.xlim[0] * scale, self.xlim[1] * scale)
            if zoomgauche:
                scale = abs(self.ylim[0] - self.ylim[1]) / abs(self.xlim[0] - self.xlim[1])
                scale = 2 * scale
                plt.ylim(self.ylim[0] * scale, self.ylim[1] * scale)
            if zoomplus:
                scale = abs(self.ylim[0] - self.ylim[1]) / abs(self.xlim[0] - self.xlim[1])
                scale = 2 * scale
                plt.xlim(self.xlim[0] * scale, self.xlim[1] * scale)
                plt.ylim(self.ylim[0] * scale, self.ylim[1] * scale)
            if zoommoins:
                scale = abs(self.ylim[0] - self.ylim[1]) / abs(self.xlim[0] - self.xlim[1])
                scale = 2*scale
                plt.xlim(self.xlim[0] / scale, self.xlim[1] / scale)
                plt.ylim(self.ylim[0] / scale, self.ylim[1] / scale)
            if pad_haut:
                scale = abs(self.ylim[0] - self.ylim[1])
                plt.xlim(self.xlim[0],self.xlim[1])
                plt.ylim(self.ylim[0] + scale/10, self.ylim[1] + scale/10)
            if pad_bas:
                scale = abs(self.ylim[0] - self.ylim[1])
                plt.xlim(self.xlim[0],self.xlim[1])
                plt.ylim(self.ylim[0] - scale/10, self.ylim[1] - scale/10)
            if pad_droit:
                scale = abs(self.xlim[0] - self.xlim[1])
                plt.ylim(self.ylim[0],self.ylim[1])
                plt.xlim(self.xlim[0] + scale/10, self.xlim[1] + scale/10)
            if pad_gauche:
                scale = abs(self.xlim[0] - self.xlim[1])
                plt.ylim(self.ylim[0],self.ylim[1])
                plt.xlim(self.xlim[0] - scale/10, self.xlim[1] - scale/10)
            x_0,x_1 = plt.xlim()
            y_0,y_1 = plt.ylim()
            if len(self.function)>0:
                for function in self.function:
                    born_x_0,born_x_1 = plt.xlim()

                    x = np.linspace(born_x_0,born_x_1,int(abs(born_x_0-born_x_1)*10))
                    universe = {'x': x,'e':e,'pi':pi}
                    try:
                        if function == 'e' or function == 'pi':
                            func = universe[function]
                        else:
                            func = float(function)
                        y = np.zeros(len(x))
                        for i in range(len(y)):
                            y[i] = func
                        plt.plot(x,y,color='m')
                        self.func_check=True
                    except RuntimeWarning:
                        self.function.remove(function)
                        self.func_check = False
                    except :
                        y_ = 'y = '+function
                        exec(y_,globals(),universe)
                        plt.plot(x,universe['y'],color='m')
                        self.func_check=False



            self.ax.set_xlim(x_0,x_1)
            self.ax.set_ylim(y_0,y_1)
            legend = self.ax.legend(loc='upper right', shadow=True, fontsize='x-large')
            self.xlim = (x_0,x_1)
            self.ylim = (y_0,y_1)
            self.canvas.draw()

        except FileNotFoundError:
            if file_path == '':
                file_path = None
                self.file_path.remove('')
            print("\033[91mCheck the file you used, the given file location is {",f'{file_path!r}',"}\033[0m")
            self.unvalid = True

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('2000x1500')
    app = PlotWindow(root)
    root.mainloop()