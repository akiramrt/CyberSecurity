from customtkinter import CTk, CTkEntry as Entry, CTkLabel as Label, CTkButton as Button, set_default_color_theme, set_appearance_mode, TOP, BOTTOM, LEFT

class Program(CTk):

    def __init__(self) -> None:
        super().__init__()
        set_appearance_mode('dark')
        set_default_color_theme('green')
        self.geometry('300x300')
        self.title('Calculadora')
        self.resizable(False, False)

        cartao = ''

        Label(self, text='Meu Texto').pack(pady = 5)
        Entry(self, 300, placeholder_text = 'Insira a senha do seu cartão: ', textvariable = cartao).pack(pady = 20)
        Button(self, 100, text = 'Clique aqui', command = self.printar).pack(pady = 50)
        
        self.mainloop()

    def printar(self) : print(self.cartao)


Program()