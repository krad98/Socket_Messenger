
import socket
import select

host = "127.0.0.1"
port = 65432

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((host, port))
connexion_principale.listen(5)

print(f"le serveur écoute sur le port {port}")

serveur_lance = True
clients_connectes = []

while serveur_lance:
	connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)
	
	for connexion in connexions_demandees:
		connexions_avec_client, infos_connexion = connexion.accept()
		clients_connectes.append(connexions_avec_client)


	try:
		clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
	except select.error:
		pass

	sup = ""
	for client in clients_a_lire:
		
		msg_recu = client.recv(1024).decode()

		print(f"reçu: {msg_recu}")
		for clie in clients_connectes:
		
			clie.send(msg_recu.encode())

"""		if msg_recu == "!FIN":
			sup = client
			clients_connectes.remove(sup)
			clients_a_lire.remove(sup)
"""
	

	

			
for client in clients_connectes:
	client.close()

connexion_principale.close()

