import streamlit as st

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from spring import spring
st.sidebar.header("Aplicacion realizada como software didactico de apoyo a la Materia Fisica Basica II, por:")
st.sidebar.subheader("D. C. Jose Manuel Napoles Duarte")
st.sidebar.subheader("D. C. Juan Pedro Palomares Baez")
st.sidebar.subheader("M. C. Carlos de la Vega Cobos")
st.sidebar.header("de la Facultad de Ciencias Quimicas de la UACH")
st.sidebar.image("logoFCQ.png")
st.title('Ley de Hooke')
k=st.number_input('Constante de fuerza K [N/m]:',5)
#st.button('click')
#y=st.number_input('give pos y')
masa = st.slider('masa [kg]',0.1,1.0,0.0)
y=-(masa*9.8/k)*100
pe=-4
st.write(round(y,4),round(y+pe,4))
point_a = (0, 0)
point_b = (0, y+pe)

fig, ax = plt.subplots(figsize=(5, 5))
patch = patches.Circle((0, y+pe), radius=1, alpha =1)
ax.add_patch(patch)

ax.plot(*spring(point_a, point_b, 12, 1.2), c="blue")
ax.set_aspect("equal", "box")
ax.axes.set_xlim(-10,10)
ax.axes.set_ylim(-20,0)
ax.annotate('punto de equilibrio', xy=(1, pe), xytext=(3, pe+0.2),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )


#plt.show()
st.pyplot(fig)
