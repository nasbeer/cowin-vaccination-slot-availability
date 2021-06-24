FROM python:3.8
EXPOSE 8085
RUN pip install streamlit requests pandas
COPY app.py /var/dashboard/app.py
CMD streamlit run /var/dashboard/app.py