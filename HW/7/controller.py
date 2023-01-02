import view
import model

def main_function():
        select = view.greeting()
        if select ==1:
            expc = view.get_export_c()
            model.expc(expc)
        elif select == 2:
            expt = view.get_export_t()
            model.expt(expt)
        elif select == 3:
            model.impcsv()
        elif select == 4:
            model.imptxt()
           
        