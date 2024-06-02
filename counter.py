from puepy import Application, Page, t

app = Application()


@app.page()
class CounterPage(Page):
    def initial(self):
        return {"current_value": 0}

    def populate(self):
        with t.div(classes="inc-box"):
            t.button("-", classes="button", on_click=self.on_decr)
            t.span(str(self.state["current_value"]))
            t.button("+", classes="button", on_click=self.on_incr)

    def on_decr(self, event):
        self.state["current_value"] -= 1

    def on_incr(self, event):
        self.state["current_value"] += 1


app.mount("#app")
