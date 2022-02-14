import streamlit as st

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from spring import spring
st.title('some title')
#st.button('click')
#y=st.number_input('give pos y')
y = st.slider('give pos y',4,10,5)
point_a = (0, 0)
point_b = (0, -y)
pe=-4
fig, ax = plt.subplots(figsize=(5, 5))
patch = patches.Circle((0, -y), radius=1, alpha =1)
ax.add_patch(patch)

ax.plot(*spring(point_a, point_b, 12, 1.2), c="blue")
ax.set_aspect("equal", "box")
ax.axes.set_xlim(-10,10)
ax.axes.set_ylim(-10,0)
ax.annotate('punto de equilibrio', xy=(1, pe), xytext=(3, pe+0.2),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )


#plt.show()
st.pyplot(fig)

