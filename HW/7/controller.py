import view
import model

def main_function():
        select = view.greeting()
        if select ==1:
            exp = view.get_export()
            res_exp = model.exp(exp)
            view.view_res_exp(res_exp)
        elif select == 2:
            imp = view.get_import()
            res_imp = model.imp(imp)
            view.view_res_imp(res_imp)
        