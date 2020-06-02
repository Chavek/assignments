#setup
import sqlite3

conn = sqlite3.connect('keyclub.sqlite')
c = conn.cursor()

#main course
    c.execute('.mode csv ')
    c.excecute('.import roster.cvs students')

#shutdown
conn.commit()
conn.close()

#ez pz lmn squez z
