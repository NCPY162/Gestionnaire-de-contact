"""GESTION DE CONTACT"""


import json


class Contact:
    def __init__(self, id, nom, prenom, telephone, email, adresse, codePostal, ville, pays) -> None:
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email
        self.adresse = adresse
        self.codePostal = codePostal
        self.ville = ville
        self.pays = pays
    
    def __repr__(self):
        return f"id: {self.id} \nnom: {self.nom} \nprenom: {self.prenom} \ntelephone: {self.telephone} \nemail: {self.email} \nadresse: {self.adresse} \ncode_postal: {self.codePostal} \nville: {self.ville} \npays: {self.pays} \n\n------------"
    
class GestionnaireDeContact:   
    def __init__(self) -> None:
        self.contacts = []
        self.id_count = 0
        self.initialisation()
             
    def initialisation(self) : 
        print("Bonjour et bienvenue dans votre gestionnaire de contact !")
        while True:
            try:
                value = int(input("Que souhaitez-vous faire ? \n"
                            "1- Afficher la liste des contacts,\n"
                            "2- Créer un contact,\n"
                            "3- Modifier un contact, \n" 
                            "4- Supprimer un contact,\n" 
                            "0- Annuler \n"
                            "Votre choix : "))
                if(value == 1):
                    self.afficherContacts()

                elif(value == 2): 
                    self.creerContact()
             
                elif(value == 3):
                    self.modifierContact()

                elif(value == 4):
                    self.supprimerContact()

                elif(value==0):
                    print("Merci et à la prochaine ! ")

                else:
                    print("Choix invalide ! veuillez reessayer")

            except ValueError:
                print("Merci de choisir un numero valide")
    
    def creerContact(self):
        self.id = self.id_count + 1
        nom = str(input("Entrez votre nom : "))
        prenom = str(input("Entrez votre prenom : "))
        telephone = int(input("Entrez votre numero de telephone : "))
        email = str(input("Entrez votre adresse mail : "))
        adresse = str(input("Entrez votre adresse : "))
        codePostal = int(input("Entrez votre code postal : "))
        ville = str(input("Entrez votre ville : "))
        pays = str(input("Entrez votre pays : "))
        
        contact = Contact(self.id, 
                          nom, 
                          prenom, 
                          telephone, 
                          email, 
                          adresse, 
                          codePostal, 
                          ville, 
                          pays)
        self.contacts.append(contact.__dict__)
        self.saveInFile()
        print("Contact créé avec succès!")
    

    def saveInFile(self):
        with open("contact.txt", "w") as file:
            file.seek(0)
            for contact in self.contacts:
                formatted_contact = f"nom: {contact['nom']}\
                \nprenom: {contact['prenom']}\
                \ntelephone: {contact['telephone']}\
                \nemail: {contact['email']}\
                \nadresse: {contact['adresse']}\
                \ncode postal: {contact['codePostal']}\
                \nville: {contact['ville']}\
                \npays: {contact['pays']}\n\n"
                
                file.write(formatted_contact + "\n\n")
            
    def readFile(self):
        file_path = "contact.txt"
        if(file_path):
            with open(file_path, "r") as file: 
                content = file.read().strip().split("\n\n")       
                for line in content:
                    contact_json = {}
                    lines = line.split("\n")
                    for data in lines : 
                        if ": " in data:
                            key, value = data.split(": ", 1)
                            contact_json[key.strip()] = value.strip()
                        
                self.contacts.append(contact_json)
                print(self.contacts)
           
    def afficherContacts(self):
        try:
            print("Liste des contacts : ")
            self.readFile()
        except:
            print("Aucun contact trouvé !")
            
    def modifierContact(self):
        tel = int(input("Quel est le numero de téléphone du contact à modifier : "))
        self.readFile()
        try:
            for contact in self.contacts:
                if int(contact['telephone']) == tel:
                    value = int(input("Que voulez-vous modifier ? \n"
                          "1- votre nom,\n 2- votre prenom, \n 3- votre telephone, \n"
                          "4- votre email, \n 5- votre adresse,\n"
                          "6- votre code postal, \n 7- votre ville,\n"
                          "8- votre pays,\n 0- pour annuler : "))

                    if(value == 1):
                        nouveau_nom = str(input("Saisir le nouveau nom : "))
                        contact["nom"] = nouveau_nom

                    if(value == 2):
                        nouveau_prenom = str(input("Saisir le nouveau prenom : "))
                        contact["prenom"] = nouveau_prenom

                    if(value == 3):
                        nouveau_telephone = str(input("Saisir le nouveau telephone : "))
                        contact["telephone"] = nouveau_telephone

                    if(value == 4):
                        nouveau_mail = str(input("Saisir le nouveau mail : "))
                        contact["email"] = nouveau_mail
    
                    if(value == 5):
                        nouvelle_adresse = str(input("Saisir la nouvelle adresse : "))
                        contact["adresse"] = nouvelle_adresse

                    if(value == 6):
                        nouveau_codePostal = str(input("Saisir le nouveau code postal : "))
                        contact["code postal"] = nouveau_codePostal

                    if(value == 7):
                        nouvelle_ville = str(input("Saisir le nouvelle ville : "))
                        contact["ville"] = nouvelle_ville

                    if(value == 8):
                        nouveau_pays = str(input("Saisir le nouveau pays : "))
                        contact["pays"] = nouveau_pays

                    if (value == 0):
                        print("Merci et à la prochaine !")
                else:
                    print("Le numero saisi n'existe pas!")     
            # self.saveInFile()
            print("Modification réussie !")                
        except:
            print("Choix invalide! Merci de saisir un numero valide")

    def supprimerContact(self):
        value = int(input("Quel est le numéro de téléphone du contact à supprimer ? : "))
        self.readFile()
        try:
            for contact in self.contacts:
                if(int(contact["telephone"]) == value):
                    self.contacts.remove(contact)
                    print("Suppression réussie !", self.contacts)
            self.saveInFile()
        except:
            print("Numéro est introuvable!")

contact = GestionnaireDeContact()