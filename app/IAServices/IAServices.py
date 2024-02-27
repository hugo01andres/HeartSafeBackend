from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
import base64
import os

class IAServices:
    def __init__(self):
        print("IA.__init__")
    
    def get_healthy_recipes(self, age, anaemia, creatine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum):
        print("IA.get_healthy_recipes")
        return "Receta 1, Receta 2, Receta 3"
        
    def get_healthy_exercises(self, age, anaemia, creatine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine):
        print("IA.get_healthy_exercises")
        return "Ejercicio 1, Ejercicio 2, Ejercicio 3"


    def make_pdf(self, graficas, healthy_recipes, healthy_exercises):
        """

        Crea un documento PDF con la información de las gráficas, recetas y ejercicios
        y retorna el pdf en base64

        """
        print("IA.make_pdf")
        # Define el documento PDF y el nombre del archivo
        pdf_name = "Analisis_de_paro_cardiaco.pdf"
        document = SimpleDocTemplate(pdf_name, pagesize=letter)
        flowables = []
        styles = getSampleStyleSheet()

        # Título del documento
        title = "<h1>Análisis de paro cardíaco</h1>"
        flowables.append(Paragraph(title, styles['Title']))

        # Descripción
        description = "<para>Basándonos en la siguiente información fue como obtuvimos la predicción de que te tienes que cuidar</para>"
        flowables.append(Paragraph(description, styles['Normal']))
        flowables.append(Spacer(1, 12))

        # Incluyendo gráficas e imágenes
        for i in range(1, 6):
            # Añadir la gráfica
            grafica = f"<para>Gráfica {i}</para>"
            # graph = f"grafica_{i}.png"  # Reemplaza esto con la ruta a tus archivos de imagen
            # flowables.append(Image(graph, width=400, height=200))
            # flowables.append(Spacer(1, 12))
            flowables.append(Paragraph(grafica, styles['Normal']))

            # Añadir la descripción de la gráfica
            graph_description = f"<para>Explicación: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>"
            flowables.append(Paragraph(graph_description, styles['Normal']))
            flowables.append(Spacer(1, 12))

        # Añadir una página de separación si es necesario
        flowables.append(PageBreak())

        # Título de la segunda página
        title_plan_alimentacion = "<h1>Plan de alimentación</h1>"
        flowables.append(Paragraph(title_plan_alimentacion, styles['Title']))

        # Descripción del plan de alimentación
        description_plan_alimentacion = "<para>De acuerdo a lo analizado te damos este plan de alimentación:</para>"
        flowables.append(Paragraph(description_plan_alimentacion, styles['Normal']))
        flowables.append(Spacer(1, 12))

        # Contenido del plan de alimentación
        for i in range(5):  # Asumiendo que hay 5 párrafos de contenido
            paragraph_plan_alimentacion = "<para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Pulvinar pellentesque habitant morbi tristique senectus et.</para>"
            flowables.append(Paragraph(paragraph_plan_alimentacion, styles['Normal']))
            flowables.append(Spacer(1, 12))

        # Título de la sección de ejercicio
        title_plan_ejercicio = "<h1>Plan de ejercicios</h1>"
        flowables.append(Paragraph(title_plan_ejercicio, styles['Title']))

        # Descripción del plan de ejercicios
        description_plan_ejercicio = "<para>De acuerdo a lo analizado te damos este plan de alimentación:</para>"  # Aquí parece haber un error en la imagen, probablemente debería decir 'plan de ejercicios'
        flowables.append(Paragraph(description_plan_ejercicio, styles['Normal']))
        flowables.append(Spacer(1, 12))

        # Contenido del plan de ejercicios
        for i in range(5):  # Asumiendo que hay 5 párrafos de contenido
            paragraph_plan_ejercicio = "<para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Pulvinar pellentesque habitant morbi tristique senectus et.</para>"
            flowables.append(Paragraph(paragraph_plan_ejercicio, styles['Normal']))
            flowables.append(Spacer(1, 12))

            # Construir el PDF
        document.build(flowables)

        with open(pdf_name, "rb") as pdf_file:
            encoded_string = base64.b64encode(pdf_file.read()).decode('utf-8')

        # Elimina el PDF
        os.remove(pdf_name)

        return encoded_string