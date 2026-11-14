FROM resilience-api:v1
COPY resilience_v2.py .
ENTRYPOINT ["python", "-m", "uvicorn"]
CMD ["resilience_v2:app", "--host", "0.0.0.0", "--port", "8000"]
