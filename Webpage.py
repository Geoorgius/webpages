import streamlit
import functions


def agregar():
    palabra = streamlit.session_state["textodelcuadro"]
    documento.append(palabra + "\n")
    functions.write(documento)


documento = functions.readline()

streamlit.set_page_config(layout="wide")

streamlit.title("Web app") #titulo
streamlit.subheader("This is a test for the subheader")#subheader

for index, item in enumerate(documento):
    checkbox = streamlit.checkbox(item,key=item) #lista
    if checkbox:
        documento.pop(index)
        functions.write(documento)
        del streamlit.session_state[item]
        streamlit._rerun()


streamlit.text_input(label="Enter what you want to add", placeholder="Enter what you want to add in the list",
                     on_change=agregar, key="textodelcuadro") #espacio de abajo


