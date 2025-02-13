FROM python:3.10

# create directory
WORKDIR  /app

#copy content to directory
COPY . /app

#install dependancies
RUN pip install --no-cache-dir -r requirements.txt

#expose server
EXPOSE 8000
#run uvivorn
#uvicorn, run, host,'extranl access".port,port_code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port","8000"]