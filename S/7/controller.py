import view
import model

def main_function():
    select = view.greeting()
    if select ==1:
        primer = view.get_math_example()
        result = model.calc(primer)
        view.view_result(result)
    elif select == 2:
        