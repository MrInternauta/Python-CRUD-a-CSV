# -*- coding: utf-8 -*-
import csv
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()
        print('Contacto añadido')

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def _print_contact(self,contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                print('Contacto eliminado')
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.upper() == name.upper():
                self._print_contact(contact)
                break


    def not_found(self):

        print('*******')
        print('¡No encontrado!')
        print('*******')
    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone','email'))
            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))


    def update(self, name, que, data):
        for idx, contact in enumerate(self._contacts):
            if contact.name.upper() == name.upper():
                if que == 'n':
                    self._contacts[idx].name = data
                    self._print_contact(contact)
                    self._save()
                    break
                elif que == 't':
                    self._contacts[idx].phone = data
                    self._print_contact(contact)
                    self._save()
                    break
                elif que == 'e':
                    self._contacts[idx].email = data
                    self._print_contact(contact)
                    self._save()
                    break
                else:
                    print('El campo que quieres actualizar no existe')
                    break


def run():
    contact_book = ContactBook()
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            else:
                contact_book.add(row[0], row[1], row[2])


    while True:
        comando = str(raw_input('''
        ...:::CONTACTOS:::...
        -Teclea una opción-
        [a]ñadir contacto
        [ac]tualizar contacto
        [b]uscar contacto
        [e]liminar contacto
        [l]istar contactos
        [s]alir
        '''))
        print(comando)
        if comando == 'a':
            print('...:::Añadir contacto:::...')
            name = str(raw_input('Ingresar nombre de contacto: '))
            phone = str(raw_input('Ingresar telefono de contacto: '))
            email = str(raw_input('Ingresar Email de contacto: '))
            contact_book.add(name, phone, email)

        elif comando == 'ac':
            print('Actualizar contacto')
            name = str(raw_input('Ingresar nombre de contacto: '))
            que = str(raw_input('''
            ¿Que desea actualizar?
            [n]ombre
            [t]elefono
            [e]mail
            '''))
            data = str(raw_input('Ingresar el nuevo dato del contacto: '))


            contact_book.update( name, que, data)

        elif comando == 'b':
            print('Buscar contacto')
            name = str(raw_input('Ingresar nombre de contacto: '))
            contact_book.search(name)


        elif comando == 'e':
            print('Eliminar contacto')
            name = str(raw_input('Ingresar nombre de contacto: '))
            contact_book.delete(name)


        elif comando == 'l':
            print('Listar contactos')
            contact_book.show_all()

        elif comando == 's':
            break

        else:
            print('Error de comando')

if __name__ == '__main__':
    run()
