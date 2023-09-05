from django.test import TestCase
from .models import Laboratorio

# Create your tests here.
class LaboratorioTests(TestCase):
    def setUp(self):
        lab1 = Laboratorio()
        lab1.nombre = "Labo 1"
        lab1.ciudad = "Santiago"
        lab1.pais = "Chile"
        lab1.save()
        
        lab2 = Laboratorio()
        lab2.nombre = "Labo 2"
        lab2.ciudad = "Concepción"
        lab2.pais = "Chile"
        lab2.save()
        
        lab3 = Laboratorio()
        lab3.nombre = "Labo 3"
        lab3.ciudad = "Puerto Varas"
        lab3.pais = "Chile"
        lab3.save()

    def test_index(self):
        response = self.client.get("/")
        labs = response.context["labs"]
        self.assertEqual(3, labs.count())

        numvisitas = response.context["numvisitas"]
        self.assertEqual(1, numvisitas)
    
    def test_create(self):
        response = self.client.post("/add",{
            "nombre": "lab 4",
            "ciudad": "Panguipulli",
            "pais": "Chile",
        }, follow=True)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "index.html")
        
        self.assertEqual(4, Laboratorio.objects.all().count())