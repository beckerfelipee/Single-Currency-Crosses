from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import requests
import keys

class Exchange(App):
    def build(self):
        # front-end
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.5, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # back-end
        # add widgets to window

        # image widget
        self.window.add_widget(Image(source="logo.png"))

        # space widget
        self.space1 = Label(
                     text=" ",
                     )
        self.window.add_widget(self.space1)

        self.space2 = Label(
                     text=" ",
                     )

        # Text input widget 1
        self.firstcoin = TextInput(
                         multiline=False,
                         padding_y=(9, 9),
                         padding_x=20,
                         size_hint=(0.5, 0.6)
                         )
        self.window.add_widget(self.firstcoin)

        # label widget
        self.message = Label(
                       text="to: ",
                       font_size=18,
                       color='#00FCE'
                       )
        self.window.add_widget(self.message)

        # Text input widget 2
        self.secondcoin = TextInput(
                         multiline=False,
                         padding_y=(9, 9),
                         padding_x=20,
                         size_hint=(0.5, 0.6)
                         )
        self.window.add_widget(self.secondcoin)

        # Button
        self.button = Button(
                      text="CONVERT",
                      size_hint=(0.5, 0.5),
                      bold=True,
                      background_color='#00FCE'
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.space2)
        self.window.add_widget(self.button)

        return self.window

    def get_coin(self, firstcoin, secondcoin):
            link = f"https://economia.awesomeapi.com.br/last/{firstcoin}-{secondcoin}"
            request = requests.get(link)
            json_request = request.json()
            try:
                cot = json_request[f"{firstcoin}{secondcoin}"]["bid"]
            except KeyError:
                print("Invalid convertion")
                cot = f"We cannot convert {firstcoin} to {secondcoin}"
            return cot
        # self.space2.text = f"{coindatabase}"

    def callback(self, instance):
        firstcoin = self.choose_coin(self.firstcoin.text)
        secondcoin = self.choose_coin(self.secondcoin.text)
        cot = self.get_coin(firstcoin, secondcoin)
        self.space2.text = cot

    def choose_coin(self, coin):
        if self.set_coin(coin) == "none":
            print("Invalid coin inputed")
        else:
            self.space2.text = " "
            coin = self.set_coin(coin)
            print(f"{coin} selected")
            return coin

    def set_coin(self, coin):
        if coin in keys.dolar:
            coin = "USD"
        elif coin in keys.real:
            coin = "BRL"
        elif coin in keys.euro:
            coin = "EUR"
        elif coin in keys.bitcoin:
            coin = "BTC"
        elif coin in keys.ethereum:
            coin = "ETH"
        else:
            coin = "none"
        return coin


if __name__ == "__main__":
    Exchange().run()

