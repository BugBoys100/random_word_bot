def log(message: list):
    '''Fait un log dans un encadré'''


    resultat = f' _______________________________________\n|{" "* 39}|\n'
    for indice in range(len(message)):
        msg = message[indice]
        if len(msg) > 37 : return ('log trop long.\n\n(', msg, ')')
        resultat = resultat + f'|  {msg}{" "*(37-len(msg))}|\n'
    resultat = resultat + '|_______________________________________|'
    return(resultat)
