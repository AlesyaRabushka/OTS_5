import xml.dom.minidom as md


class FileSystem:
    def __init__(self):
        pass


    def record(self, graphs_list):
        # is called to record pets info into the file
        doc = md.Document()
        graph_info = doc.createElement('Graphs_list')
        doc.appendChild(graph_info)

        for item in graphs_list:
            graphs = doc.createElement('Graph')

            graph_name = doc.createElement('name')
            graph_name.appendChild(doc.createTextNode(item.name))

            matrix = doc.createElement('matrix')
            matrix.appendChild(doc.createTextNode(str(item.matrix)))

            # birth_date = doc.createElement('birth_date')
            # birth_date.appendChild(doc.createTextNode(str(item['birth_date'])))
            #
            # last_appointment = doc.createElement('last_appointment_date')
            # last_appointment.appendChild(doc.createTextNode(str(item['last_appointment_date'])))
            #
            # vet_name = doc.createElement('vet_name')
            # vet_name.appendChild(doc.createTextNode(item['vet_name']))
            #
            # disease = doc.createElement('disease')
            # disease.appendChild(doc.createTextNode(item['disease']))
            #
            # handler = doc.createElement('handler_name')
            # handler.appendChild(doc.createTextNode(item['handler_name']))
            #
            # phone = doc.createElement('phone_number')
            # phone.appendChild(doc.createTextNode(item['phone_number']))
            #
            # mail = doc.createElement('mail')
            # mail.appendChild(doc.createTextNode(item['mail']))
            #
            # address = doc.createElement('handler_address')
            # address.appendChild(doc.createTextNode(item['handler_address']))

            graphs.appendChild(graph_name)
            graphs.appendChild(matrix)
            # pet.appendChild(birth_date)
            # pet.appendChild(last_appointment)
            # pet.appendChild(vet_name)
            # pet.appendChild(disease)
            # pet.appendChild(handler)
            # pet.appendChild(phone)
            # pet.appendChild(mail)
            # pet.appendChild(address)

            graph_info.appendChild(graphs)

        file = open('graphs.xml', 'w')
        doc.writexml(file, encoding='windows-1251')
        file.close()