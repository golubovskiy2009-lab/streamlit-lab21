import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.set_page_config(page_title="Data Analysis App")
    st.title("Streamlit Data Visualizer")
    
    with st.sidebar:
        st.header("Settings")
        chart_type = st.selectbox("Select Function", ["Sine", "Cosine"])
        frequency = st.slider("Frequency", 1, 20, 10)
        line_color = st.color_picker("Pick a color", "#00f900")
    
    x = np.linspace(0, 10, 1000)
    if chart_type == "Sine":
        y = np.sin(x * frequency * 0.1)
    else:
        y = np.cos(x * frequency * 0.1)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, color=line_color)
    ax.set_title(f"{chart_type} Wave")
    ax.grid(True, alpha=0.3)
    
    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig)
    with col2:
        st.write("Statistics:")
        st.metric("Maximum", round(float(np.max(y)), 2))
        st.metric("Minimum", round(float(np.min(y)), 2))

    user_note = st.text_input("Enter your note:")
    if st.button("Save"):
        st.write(f"Note saved: {user_note}")

if __name__ == "__main__":
    main()
