import json
import os

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
        self.loadContacts()
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
                    break

                else:
                    print("Choix invalide ! veuillez réessayer")

            except ValueError:
                print("Merci de choisir un numéro valide")
    
    def creerContact(self):
        self.id_count += 1
        nom = str(input("Entrez votre nom : "))
        prenom = str(input("Entrez votre prénom : "))
        telephone = int(input("Entrez votre numéro de téléphone : "))
        email = str(input("Entrez votre adresse mail : "))
        adresse = str(input("Entrez votre adresse : "))
        codePostal = int(input("Entrez votre code postal : "))
        ville = str(input("Entrez votre ville : "))
        pays = str(input("Entrez votre pays : "))
        
        contact = Contact(self.id_count, 
                          nom, 
                          prenom, 
                          telephone, 
                          email, 
                          adresse, 
                          codePostal, 
                          ville, 
                          pays)
        self.contacts.append(contact)
        self.saveInFile()
        print("Contact créé avec succès!")
    

    def saveInFile(self):
        with open("contacts.json", "w") as file:
            json.dump([contact.__dict__ for contact in self.contacts], file)
            
    def loadContacts(self):
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as file:
                contacts_data = json.load(file)
                self.contacts = [Contact(**data) for data in contacts_data]
                if self.contacts:
                    self.id_count = max(contact.id for contact in self.contacts)
           
    def afficherContacts(self):
        if self.contacts:
            print("Liste des contacts : ")
            for contact in self.contacts:
                print(contact)
        else:
            print("Aucun contact trouvé !")
            
    def modifierContact(self):
        tel = int(input("Quel est le numéro de téléphone du contact à modifier : "))
        contact = next((contact for contact in self.contacts if contact.telephone == tel), None)
        
        if contact:
            value = int(input("Que voulez-vous modifier ? \n"
                              "1- votre nom,\n 2- votre prénom, \n 3- votre téléphone, \n"
                              "4- votre email, \n 5- votre adresse,\n"
                              "6- votre code postal, \n 7- votre ville,\n"
                              "8- votre pays,\n 0- pour annuler : "))

            if value == 1:
                nouveau_nom = str(input("Saisir le nouveau nom : "))
                contact.nom = nouveau_nom

            elif value == 2:
                nouveau_prenom = str(input("Saisir le nouveau prénom : "))
                contact.prenom = nouveau_prenom

            elif value == 3:
                nouveau_telephone = int(input("Saisir le nouveau téléphone : "))
                contact.telephone = nouveau_telephone

            elif value == 4:
                nouveau_mail = str(input("Saisir le nouveau mail : "))
                contact.email = nouveau_mail

            elif value == 5:
                nouvelle_adresse = str(input("Saisir la nouvelle adresse : "))
                contact.adresse = nouvelle_adresse

            elif value == 6:
                nouveau_codePostal = int(input("Saisir le nouveau code postal : "))
                contact.codePostal = nouveau_codePostal

            elif value == 7:
                nouvelle_ville = str(input("Saisir la nouvelle ville : "))
                contact.ville = nouvelle_ville

            elif value == 8:
                nouveau_pays = str(input("Saisir le nouveau pays : "))
                contact.pays = nouveau_pays

            elif value == 0:
                print("Merci et à la prochaine !")
                return

            else:
                print("Choix invalide! Merci de saisir un numéro valide")
                return
                
            self.saveInFile()
            print("Modification réussie !")
        else:
            print("Le numéro saisi n'existe pas!")     

    def supprimerContact(self):
        tel = int(input("Quel est le numéro de téléphone du contact à supprimer ? : "))
        contact = next((contact for contact in self.contacts if contact.telephone == tel), None)
        
        if contact:
            self.contacts.remove(contact)
            self.saveInFile()
            print("Suppression réussie !")
        else:
            print("Numéro introuvable!")

contact = GestionnaireDeContact()
