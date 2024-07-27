import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from math import *
from kivy import Config





class Botao(Button):
    def test(self):
        print("funcionando")


class Tela(Widget):
    def  __init__(self,**kwargs):
        super(Tela,self).__init__(**kwargs)
        self.ids.mostrar.text = " "


    def fazer(self,elemento):
        antes = self.ids.mostrar.text


        self.ultimo_elemento_operacao = [
            self.ids.mostrar.text[-1] != "+" and self.ids.mostrar.text[-1] != "-" and self.ids.mostrar.text[-1] != "/" and self.ids.mostrar.text[-1] != "*"
        ]

        '''self.o_parenteses_estar_fechado = [
            "(" in self.ids.mostrar.text and ")" in self.ids.mostrar.text
        ]'''

        self.nao_tem_parenteses = [
            "(" not in self.ids.mostrar.text and ")" not in self.ids.mostrar.text or
            "(" in self.ids.mostrar.text and ")" in self.ids.mostrar.text
        ]




        self.o_primeiro_elemeto_e_igual_ou_vezes = [
            self.ids.mostrar.text[0] != "*" and self.ids.mostrar.text[0] != "/"
        ]

        self.um_elemento = [
            len(self.ids.mostrar.text) != 1
        ]

        print(all(self.nao_tem_parenteses))

        if elemento == "=":
            if all(self.ultimo_elemento_operacao) and all(self.o_primeiro_elemeto_e_igual_ou_vezes) and all(self.nao_tem_parenteses):
                self.ids.mostrar.text = str(self.calcular(self.ids.mostrar.text))


        else:self.ids.mostrar.text = self.ids.mostrar.text + str(elemento)

        #impedir que sinais de operação se repitam
        if not all(self.ultimo_elemento_operacao) and self.o_elemento_e_ope(elemento) == True:
            self.ids.mostrar.text = self.ids.mostrar.text.removesuffix(str(elemento))
            ultimo_elemento_e_buxa = True


        self.ids.mostrar.text = self.ids.mostrar.text.removeprefix(" ")

        # para nao deixar um texto feio
        if self.ids.mostrar.text == "None":
            self.ids.mostrar.text = antes

    def o_elemento_e_ope(self,ele):
        operacao = [
            ele == "+" or ele == "-" or ele == "/" or ele == "*"
        ]
        if all(operacao):
            return True
        else: return False


    def calcular(self,str):
        try:
            if str[-1] != "+" :
                if str[-1] != "-":
                    if str[-1] != "/":
                        if str[-1] != "*":
                            if "+" or "-" or "/" or "*" in str:
                                resul = eval(str)
                                return resul
                            else: return str
                    else:return str
                else:return str
            else: return str
        except:pass


    def apagar(self):
        self.ids.mostrar.text = ' '


class MyButton(Button):
    def build(self):
        pass



class Contas(Label):
    def tentar(self):
        print("1")
        self.valor="a"
    def teste(self):
        self.valor = "a"
        return self.valor



class Button1(MyButton):
    pass
class Button2(MyButton):
    pass
class Button3(MyButton):
    pass
class Button4(MyButton):
    pass
class Button5(MyButton):
    pass
class Button6(MyButton):
    pass
class Button7(MyButton):
    pass
class Button8(MyButton):
    pass
class Button9(MyButton):
    pass
class Button10(MyButton):
    pass
class Button11(MyButton):
    pass
class Button12(MyButton):
    pass
class Button13(MyButton):
    pass
class Button14(MyButton):
    pass
class Button15(MyButton):
    pass
class Button16(MyButton):
    pass
class Button17(MyButton):
    pass
class Button18(MyButton):
    pass
class Button19(MyButton):
    pass
class Button20(MyButton):
    pass
class Button21(MyButton):
    pass
class Button22(MyButton):
    pass
class Button23(MyButton):
    pass
class Button24(MyButton):
    pass
class Button25(MyButton):
    pass

class Calculadora(App):
    def build(self):
        return Tela()



Window.clearcolor = (0.118,0.118,0.118,1)
Window.size = (260,420)

if __name__ == '__main__':
    Calculadora().run()
