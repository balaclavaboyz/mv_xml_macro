from datetime import datetime
import glob
import xmltodict
from pprint import pp
import pyautogui


def main():
    q = []
    price = 0.0
    files = [x for x in glob.glob('*.xml')]
    for u in files:
        with open(u, 'rb') as f:
            file = xmltodict.parse(f)
            # file_date = datetime.fromisoformat(file['nfeProc']['NFe']['infNFe']['ide']['dhEmi'])
            # if file_date.date() != datetime.today().date():
            #     continue
            items = file['nfeProc']['NFe']['infNFe']['det']
            for i in items:
                q.append([i['prod']['cProd'], i['prod']['qCom'].split('.')[0]])
                price += int(i['prod']['vProd'].replace('.', ''))
    # pp(q)
    pp(price / 100)
    if not q:
        exit()

    pyautogui.hotkey('alt', 'tab', 'tab')
    for row in q:
        pyautogui.typewrite(row[0])
        pyautogui.typewrite('\n')
        pyautogui.typewrite(row[1])
        pyautogui.typewrite('\n')


if __name__ == '__main__':
    main()
