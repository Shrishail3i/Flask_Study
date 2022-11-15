FROM python:3.10
EXPOSE 5000
WORKDIR /app
RUN pip install flask # TODO: Move this to requirements.txt 
COPY . .
CMD ["flask", "run", "--port", "0.0.0.0"] # 👏🏾 for Host. PORT argument is not required, Unless there is a change in Port