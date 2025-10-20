import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_service.settings")
django.setup()

from car_service.repositories.RepositoryManager import RepositoryManager

if __name__ == "__main__":
    import os
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_service.settings")
    django.setup()

    repo = RepositoryManager()

    print("Cars:")
    for car in repo.car.get_all():
        print(car.brand)

    repo.car.update(1, brand="Audi")
    # repo.car.update(1, brand="Toyota")

    '''new_client = repo.client.create(
        firstName="Ivan",
        lastName="Ivanov",
        phoneNumber="+380971234567",
        email="ivan@example.com"
    )
    print("\nNew Client Added:", new_client.idClient, new_client.firstName, new_client.lastName)'''

    id = 5
    rez = repo.client.delete(id)
    if rez:
        print(f"\nClient with id = {id} deleted")
    else:
        print(f"\nClient with id = {id} doesn't exist")

    print("Clients:")
    for car in repo.client.get_all():
        print(car.brand)
    emp = repo.employee.get_by_id(1)
    if emp:
        print("\nEmployee with ID=1:", emp)
