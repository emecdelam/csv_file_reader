import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import e, sin, pi, cos, tan

class PlotWindow:
    #==============
    # Names and var
    #==============
    __xlabel = " Temps [ s ] "
    __ylabel = " Tension [ V ] "
    __name = " Signal data "
    def __init__(self, master):
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
        button_zoomplus.place(x=500,y=50)
        button_zoommoins = tk.Button(master, text="Zoom +", command=self.zoommoins)
        button_zoommoins.pack(side=tk.TOP)
        button_zoommoins.place(x=500,y=75)
        button_load = tk.Button(master, text="Load File", command=self.load_file)
        button_load.pack(side=tk.TOP)
        button_load.place(x=350, y=50)
        button_line1 = tk.Button(master, text="Highlight", command=self.highlighting)
        button_line1.pack(side=tk.TOP)
        button_line1.place(x=700,y=50)
        button_line2 = tk.Button(master, text="Highlight2", command=self.highlighting2)
        button_line2.pack(side=tk.TOP)
        button_line2.place(x=700,y=75)
        self.entry = tk.Entry(master)
        self.entry.pack(side=tk.TOP)
        self.entry.place(x=775,y=50)
        self.entry2 = tk.Entry(master)
        self.entry2.pack(side=tk.TOP)
        self.entry2.place(x=775,y=75)
        button_draw_func = tk.Button(master, text="Draw", command=self.get_function)
        button_draw_func.pack(side=tk.TOP)
        button_draw_func.place(x=1100, y=50)
        self.func = tk.Entry(master)
        self.func.pack(side=tk.TOP)
        self.func.place(x=1140, y=50)
        """
        button_offset = tk.Button(master, text="Offset", command=self.offset)
        button_offset.pack(side=tk.TOP)
        button_offset.place(x=1400,y=75)
        self.entry_offset = tk.Entry(master)
        self.entry_offset.pack(side=tk.TOP)
        self.entry_offset.place(x=1450,y=75)"""

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
        self.canvas.draw()

        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    def offset(self):
        pass

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
    def zoomplus(self):
        plt.cla()
        for i in range(len(self.file_path)):
            self.draw(file_path=self.file_path[i],zoomplus=True)
    def zoommoins(self):
        plt.cla()
        for i in range(len(self.file_path)):
            self.draw(file_path=self.file_path[i],zoommoins=True)
    def erase(self):
        plt.cla()
        self.file_path = []
        self.highlight = None
        self.highlight2 = None
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
            self.file_path.append(entry)
            for i in range(len(self.file_path)):
                self.draw(file_path=self.file_path[i])

            plt.clf()
            if not self.unvalid:
                print('\033[92mSuccessfully loaded the file \t\t\t\t\t{',f"{entry}",'}\033[0m')
        except:
            pass
    def draw(self,file_path,zoomplus=False,zoommoins=False,pad_haut=False,pad_bas=False,pad_droit=False,pad_gauche=False):

        try:
            with open(file_path, 'r') as file_in:
                file = [line.replace(',', '.').strip() for line in file_in.readlines()[3:]]
                data = np.array([list(map(float, line.split(';'))) for line in file])
            number_of_graphs = len(data[0])-1
            if number_of_graphs < 2:
                time, signal1 = data[0:len(data) - 1, 0], data[0:len(data) - 1, 1]
                if max(signal1) > 50:
                    data[:][1] = data[:][1] / 100
                    time = time/100
                plt.plot(time, signal1, label=" V_output ", color='g')

            else:
                time, signal1, signal2 = data[0:len(data) - 1, 0], data[0:len(data) - 1, 1], data[0:len(data) - 1,2]
                if max(signal1) > 50 or max(signal2) > 50:
                    time = time/100
                    signal1 = signal1 / 100
                    signal2 = signal2 /100
                plt.plot(time, signal2, label=" V_input ", color='r')
                plt.plot(time, signal1, label=" V_output ", color='b')


            if self.highlight != None:
                jonction_x = (time[0],time[len(time)-1])
                jonction_y = (self.highlight,self.highlight)
                plt.plot(jonction_x, jonction_y, label='Jonction', color='y')
            if self.highlight2 != None:
                jonction_x = (time[0],time[len(time)-1])
                jonction_y = (self.highlight2,self.highlight2)
                plt.plot(jonction_x,jonction_y,label='Jonction2',color='c')

            if zoomplus:
                scale = abs(self.ylim[0] - self.ylim[1]) / abs(self.xlim[0] - self.xlim[1])
                scale = 2*scale
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



            plt.xlim(x_0,x_1)
            plt.ylim(y_0,y_1)
            plt.xlabel(self.__xlabel)
            plt.ylabel(self.__ylabel)
            self.xlim = (x_0,x_1)
            self.ylim = (y_0,y_1)
            self.canvas.draw()
        except FileNotFound:
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