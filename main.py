from tkinter import *

app = Tk()


class Application:

    def __init__(self: object) -> None:
        self.app: object = app
        self.window()
        self.textw1()
        self.buttons()
        self.app.mainloop()

    def window(self: object) -> None:
        self.app.title("Jogo Gourmet")
        self.app.geometry("270x95")
        self.app.resizable(True, True)
        self.app.eval('tk::PlaceWindow . center')

    def buttons(self: object) -> None:
        self.bt_ok = Button(text="OK", bg='#EBF5FB', command=self.massa)
        self.bt_ok.place(relx='0.43', y='60', height='', width='50')

    def textw1(self: object) -> None:
        self.text = Label(text='Pense em um prato que gosta', font='Helvetica 9 bold')
        self.text.pack()

    def massa(self: object) -> None:
        self.segunda_janela = Tk()
        self.segunda_janela.title("Confirm")
        self.segunda_janela.geometry("280x100")
        self.segunda_janela.resizable(False, False)
        self.segunda_janela.eval('tk::PlaceWindow . center')
        self.lb: Label = Label(self.segunda_janela, text="O prato que você pensou é massa? ", font='Helvetica 9 bold')
        self.lb.pack()
        self.bt_sim: Button = Button(self.segunda_janela, text="Sim", bg="#EBF5FB", command=lambda: [self.lasanha(), self.fecha_massa()])
        self.bt_sim.place(relx=0.30, y='60', height='', width='50')
        self.bt_nao: Button = Button(self.segunda_janela, text="Não", bg="#EBF5FB", command=lambda: [self.bolo_de_chocolate(), self.fecha_massa()])
        self.bt_nao.place(relx=0.50, y='60', height='', width='50')

    def lasanha(self: object) -> None:
        self.terceira_janela = Tk()
        self.terceira_janela.title("Confirm")
        self.terceira_janela.geometry("285x105")
        self.terceira_janela.resizable(False, False)
        self.terceira_janela.eval('tk::PlaceWindow . center')
        self.lb: Label = Label(self.terceira_janela, text="O prato que você pensou é lasanha?", font='Helvetica 9 bold')
        self.lb.pack()
        self.bt_sim: Button = Button(self.terceira_janela, text="Sim", bg="#EBF5FB", command=lambda: [self.acertei(), self.fecha_lasanha()])
        self.bt_sim.place(relx=0.30, y='60', height='', width='50')
        self.bt_nao: Button = Button(self.terceira_janela, text="Não", bg="#EBF5FB", command=lambda: [self.qual_prato(), self.fecha_lasanha()])
        self.bt_nao.place(relx=0.50, y='60', height='', width='50')

    def bolo_de_chocolate(self: object) -> None:
        self.quarta_janela = Tk()
        self.quarta_janela.title("Confirm")
        self.quarta_janela.geometry("285x105")
        self.quarta_janela.resizable(False, False)
        self.quarta_janela.eval('tk::PlaceWindow . center')
        self.lb: Label = Label(self.quarta_janela, text="O prato que você pensou é Bolo de Chocolate?", font='Helvetica 9 bold')
        self.lb.pack()
        self.bt_sim: Button = Button(self.quarta_janela, text='Sim', bg="#EBF5FB", command=lambda: [self.acertei(), self.fecha_bolo()])
        self.bt_sim.place(relx=0.30, y='60', height='', width='50')
        self.bt_nao: Button = Button(self.quarta_janela, text='Não', bg="#EBF5FB", command=lambda: [self.qual_prato(), self.fecha_bolo()])
        self.bt_nao.place(relx=0.50, y='60', height='', width='50')

    def acertei(self: object) -> None:
        self.quinta_janela = Tk()
        self.quinta_janela.title("Jogo Gourmet")
        self.quinta_janela.geometry("285x105")
        self.quinta_janela.resizable(False, False)
        self.quinta_janela.eval('tk::PlaceWindow . center')
        self.lb: Label = Label(self.quinta_janela, text="Acertei de novo!", font='Helvetica 9 bold')
        self.lb.place(relx=0.30, y='32', height='', width='')
        self.bt_ok: Button = Button(self.quinta_janela, text='OK', bg="#EBF5FB", command=exit)
        self.bt_ok.place(relx=0.40, y='60', height='', width='50')

    def qual_prato(self: object) -> None:
        self.sexta_tela: object = Tk()
        self.sexta_tela.title("Desisto")
        self.sexta_tela.geometry("285x105")
        self.sexta_tela.resizable(False, False)
        self.sexta_tela.eval('tk::PlaceWindow . center')
        self.lb: Label = Label(self.sexta_tela, text="Qual prato você pensou?", font='Helvetica 8 bold')
        self.lb.place(x=45, y=10)
        self.etst = self.entrada(self.sexta_tela)
        self.bt_ok: Button = Button(self.sexta_tela, text='OK', bg="#EBF5FB", command=lambda: [self.tela_final(), self.fecha_prato()])
        self.bt_ok.place(relx=0.25, y='60', height='', width='70')
        self.bt_cancelar: Button = Button(self.sexta_tela, text='Cancelar', bg="#EBF5FB", command=exit)
        self.bt_cancelar.place(relx=0.55, y='60', height='', width='70')

    def tela_final(self: object) -> None:
        self.set_tela: object = Tk()
        self.set_tela.title("Complete")
        self.set_tela.geometry("300x105")
        self.set_tela.resizable(False, False)
        self.set_tela.eval('tk::PlaceWindow . center')
        self.retorno(self.set_tela)
        self.et: Entry = Entry(self.set_tela)
        self.et.place(x=50, y=35, height='', width='225')
        self.bt_sim: Button = Button(self.set_tela, text='OK', bg="#EBF5FB", command=exit)
        self.bt_sim.place(relx=0.25, y='60', height='', width='70')
        self.bt_nao: Button = Button(self.set_tela, text='Cancelar', bg="#EBF5FB", command=exit)
        self.bt_nao.place(relx=0.55, y='60', height='', width='70')

    def entrada(self: object, x: object) -> Entry:
        self.et: Entry = Entry(x)
        self.et.place(relx=0.15, y='35', width=225)
        return self.et

    def retorno(self: object, x: object) -> Label:
        self.ret = self.etst.get()
        self.print_ret: Label = Label(x, text=f"{self.ret} é _____ mas Bolo de Chocolate não.", font='Helvetica 8 bold')
        self.print_ret.place(x=45, y=10)
        return self.print_ret

    def fecha_massa(self: object) -> None:
        self.segunda_janela.destroy()

    def fecha_lasanha(self: object) -> None:
        self.terceira_janela.destroy()

    def fecha_bolo(self: object) -> None:
        self.quarta_janela.destroy()

    def fecha_prato(self: object) -> None:
        self.sexta_tela.destroy()

Application()
