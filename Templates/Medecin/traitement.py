import cgi
import cgitb

cgitb.enable()
varRecuperation = cgi.FieldStorage()

print(varRecuperation.getvalue("nom"))