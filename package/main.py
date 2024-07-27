from application.salary import calculate_salary
from application.db.people import get_employees
from PIL import Image


image_ = Image.open("/Users/anastasiaklimanova/Desktop/kitty.jpeg")



if __name__ == '__main__':
    calculate_salary(40000, 23, 10)
    get_employees()
    image_.show() #показывает пикчу с рабочего стола
    # положу вам эту пикчу в директорию
