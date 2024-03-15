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
                #print(response)
        else:
            response = """No tienes api key pero te dejare un Lorem Ipsum de como se veiria Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Pulvinar 
            pellentesque habitant morbi tristique senectus et. 
            1. -
            2. -
            3. -"""
        

        return response
        
    def get_healthy_exercises(self, age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking):
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
            system_message = "Solo contesta con el plan de ejercicios no digas nada mas. Eres un agente experto en dar plan de ejercicios para personas con la sigueinte información: "
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
                #print(response)
        else:
            response = """No tienes api key pero te dejare un Lorem Ipsum de como se veiria Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Pulvinar 
            pellentesque habitant morbi tristique senectus et. 
            1. -
            2. -
            3. -"""
        

        return response


    def make_pdf(self, json_graficas_y_descripciones, healthy_recipes, healthy_exercises):
        """

        Crea un documento PDF con la información de las gráficas, recetas y ejercicios
        y retorna el pdf en base64

        """
        print("IA.make_pdf")
        print(healthy_recipes)
        print(healthy_exercises)
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

        # Incluyendo gráficas y descripcion
        for grafica_desc in json_graficas_y_descripciones:
            # Añadir la gráfica
            flowables.append(Image(grafica_desc['graficas'], width=400, height=200))
            flowables.append(Spacer(1, 12))
            # Añadir la descripción
            flowables.append(Paragraph(grafica_desc['descripciones'], styles['Normal']))
            flowables.append(Spacer(1, 12))
        

        # Incluyendo gráficas e imágenes
        # for grafica in graficas:
        #     # Añadir la gráfica
        #     flowables.append(Image(grafica, width=400, height=200))
        #     flowables.append(Spacer(1, 12))
        #     graph_description = f"<para>Explicación: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>"
        #     flowables.append(Paragraph(graph_description, styles['Normal']))
        #     flowables.append(Spacer(1, 12))


        # Página nueva
        flowables.append(PageBreak())

        # Título de la segunda página
        title_plan_alimentacion = "<h1>Plan de alimentación</h1>"
        flowables.append(Paragraph(title_plan_alimentacion, styles['Title']))

        # Descripción del plan de alimentación
        paragraphs_plan_alimentacion = healthy_recipes.split('\n')
        for paragraph in paragraphs_plan_alimentacion:
            flowables.append(Paragraph(paragraph, styles['Normal']))
            flowables.append(Spacer(1, 12))

        # Pagina nueva
        flowables.append(PageBreak())

        # Título de la sección de ejercicio
        title_plan_ejercicio = "<h1>Plan de ejercicios</h1>"
        flowables.append(Paragraph(title_plan_ejercicio, styles['Title']))

        # Descripcion de la sección de ejercicio
        paragraphs_plan_ejercicios = healthy_exercises.split('\n')
        for paragraph in paragraphs_plan_ejercicios:
            flowables.append(Paragraph(paragraph, styles['Normal']))
            flowables.append(Spacer(1, 12))



        # Construir el PDF
        document.build(flowables)

        with open(pdf_name, "rb") as pdf_file:
            encoded_string = base64.b64encode(pdf_file.read()).decode('utf-8')

        # Elimina el PDF
        os.remove(pdf_name)
        return encoded_string