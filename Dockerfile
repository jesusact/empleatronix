FROM python:3.12
WORKDIR /app
COPY ./* /app/
RUN pip install numpy pandas streamlit matplotlib
# EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "streamlit_app.py"]