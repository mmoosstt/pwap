from . import get_path
import openpyxl as opx
#To change an existing wookbook we located it by referencing its path

class DB:
    wb = opx.load_workbook("{}\\{}".format(get_path(),"db02.xlsx"))
