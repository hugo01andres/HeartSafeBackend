from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
import base64
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain import PromptTemplate
from langchain.callbacks import get_openai_callback
from langchain_openai import OpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

class IAServices:
    load_dotenv()
    def __init__(self):
        print("IA.__init__")

    def get_healthy_recipes(self, age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking):
        print(age)
        print(anaemia)
        if anaemia == False:
            anaemia = "No tiene anaemia"
        print(creatinine_phosphokinase)
        print(diabetes)
        if diabetes == False:
            diabetes = "No tiene diabetes"
        print(ejection_fraction)
        print(high_blood_pressure)
        if high_blood_pressure == False:
            high_blood_pressure = "No tiene presión alta"
        print(platelets)
        print(serum_creatinine)
        print(serum_sodium)
        print(sex)
        if sex == 0:
            sex = "Es Mujer"
        else:
            sex = "Es Hombre"
        print(smoking)
        if smoking == False:
            smoking = "No fuma"
        else:
            smoking = "Si Fuma"

        if os.environ.get("OPENAI_API_KEY"):
            llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5, max_tokens=500)
            system_message = "Solo contesta con la receta no digas nada mas. Eres un agente experto en dar recetas de cocina saludable para personas con la sigueinte información: "
            human_message = f"""
            Age: {age}
            Anaemia: {anaemia}
            Creatinine Phosphokinase: {creatinine_phosphokinase}
            Diabetes: {diabetes} 
            Ejection Fraction: {ejection_fraction}
            High Blood Pressure: {high_blood_pressure}
            Platelets: {platelets}
            Serum Creatinine: {serum_creatinine}
            Serum Sodium: {serum_sodium}
            Sex: {sex}
            Smoker: {smoking}
            """
            messages = [SystemMessage(content=system_message), 
                        HumanMessage(content=human_message)]
            print(messages[0].content)
            with get_openai_callback() as cb:
                response_content = llm.invoke(messages)
                response = response_content.content
                print(cb)
                print(response)
        else:
            response = """No tienes api key pero te dejare un Lorem Ipsum de como se veiria Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Pulvinar 
            pellentesque habitant morbi tristique senectus et. 
            1. -
            2. -
            3. -"""
        

        return response
        
    def get_healthy_exercises(self, age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking):
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
        paragraph_plan_alimentacion = f"<para>{healthy_recipes}</para>"
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