from qrtest import QrCreate

q = QrCreate(raw_input().decode('gbk'),'test002.png')
q.create()