FROM python:3.10

WORKDIR /opt/telegram_bot

ENV PYTHONPATH=/opt/telegram_bot

COPY pyproject.toml pyproject.toml
RUN pip install --upgrade pip && \
    pip install 'poetry>=1.4.2' && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-dev


COPY . .

CMD ["python", "-m",  "main"]