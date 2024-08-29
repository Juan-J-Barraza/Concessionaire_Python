from models import Client, Seller, Concessionaire, Service, Equipment, ExtraEquipment, Car, Document, Sale, Inventory
from datetime import datetime


def main():
    
    # objects Concessionaire
    concessionaire = Concessionaire(name="Concesionario ABC", NIT="NIT123456")
    concessionaire2 = Concessionaire(name="Ford", NIT="144324432432")
  
  
    # objects Seller
    seller = Seller(name="Pedro", last_name="Pérez", NIF="123456789", address="Calle Falsa 123", concessionaire=concessionaire)
    seller2 = Seller(name="Fernando", last_name="Hernandez", NIF="23456778", address="Calle inventada 234433", concessionaire=concessionaire)
   
    # object Client
    client = Client(name="Juan", last_name="Barraza", doc_type="CC", doc_number=12324242344, seller=seller)
    
    seller.add_clients(client)
    concessionaire.add_sellers(seller)
    concessionaire.add_sellers(seller2)
    
    # objects Service
    service = Service(name="Servicio de Mantenimiento", address="Calle Real 456", NIF="NIF654321")
    service2 = Service(name="Servicio de venta", address="CLL troncal 3", NIF="NIF34353454353")
    concessionaire.add_service(service)
    concessionaire.add_service(service2)

    # objects Equipment
    equipment1 = Equipment(name="Aire Acondicionado", type="Climatización", features="Aire frío/calor")
    equipment2 = Equipment(name="Sensor de Estacionamiento", type="Seguridad", features="Sensor trasero")

    # objects ExtraEquipment
    extra1 = ExtraEquipment(name="Alarma", price="150")
    extra2 = ExtraEquipment(name="Cámara de reversa", price="200")

    # objects Car
    car = Car(frame_number="ABC1234", price=20000.0, technical_data="Motor V6", power="200 HP", brand="Toyota", models="Corolla", status="Nuevo", features="red color", concessionaire=concessionaire)
    car.add_equipment(equipment1)
    car.add_equipment(equipment2)
    car.add_extra(extra1)
    car.add_extra(extra2)
    
    car2 = Car(frame_number="ABC1235", price=25000.0, technical_data="Motor V100", power="600 HP", brand="Toyota", models="TXL", status="Nuevo", features="black color", concessionaire=concessionaire2)
    car2.add_equipment(equipment1)
    car2.add_equipment(equipment2)
    car2.add_extra(extra2)
    
    # objects Inventory
    inventory = Inventory(concessionaire=concessionaire)

    # objects Document
    document = Document(pay_method="Tarjeta de Crédito", date=datetime.now(), client=client, car=car, seller=seller)
   
    # objects Sale
    sale = Sale(registration="REG001", origin_car="concessionaire", document=document)
    seller.add_sales(sale)
    seller.add_documents(document)
    concessionaire.add_cars(car)
    
    #sellers = ', '.join([str(seller) for seller in concessionaire.get_list_sellers()])
    #documents = ','.join([str(document) for document in seller.get_list_documennts()])
    #services = ', '.join([str(service) for service in concessionaire.get_list_services()])
    
    

    #print(f"documents: {documents}")
    #print(f"Concessionaire: {type_concessionaire.get_concesionarie()}")
    #print(f"sellers: {sellers}")
    #print(f"car: {car.get_concessionaire()}")
    #print(f"Sale Registration: {sale.registration}")
    #print(f"Client Name: {document.client.name}")
    #print(f"Extra Equipment: {document.car.models}")
    #print(f"Available Extras List: {[extra.name for extra in car.list_available_extras]}")
    #print(f"Extra Equipment: {document.list_extra_equipments[0].name}")
    #print(f"List of Sales for Seller: {[sale.registration for sale in seller.list_sales]}")
    #print("Servicios Disponibles en el Concessionaire:")
    #print(f"Inventory of Cars: {[car.frame_number for car in inventory.list_cars]}")
    #print(f"Location of Inventory: {services}")


if __name__ == "__main__":
    main()
