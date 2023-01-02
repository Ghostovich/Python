import view
import model

def main_function():
        select = view.greeting()
        if select ==1:
            exp = view.get_export()
            model.exp(exp)
        elif select == 2:
            model.imp()
            
        