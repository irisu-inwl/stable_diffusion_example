FROM nvidia/cuda:11.6.2-cudnn8-runtime-ubuntu20.04 as builder

RUN apt update \
  && apt upgrade -y
RUN apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev curl
RUN wget https://www.python.org/ftp/python/3.10.6/Python-3.10.6.tgz
RUN tar -xf Python-3.10.6.tgz && rm Python-3.10.6.tgz
RUN cd Python-3.10.6/ && \
  ./configure --enable-optimizations \
  && make \
  && make install 

RUN useradd -m -u 1000 app \
  && mkdir /opt/app \
  && chown app:app /opt/app \
  && mkdir /home/app/.huggingface
RUN --mount=type=secret,id=huggingface_token cp /run/secrets/huggingface_token /home/app/.huggingface/token \
  && chown -R app:app /home/app/.huggingface

USER 1000
WORKDIR /opt/app

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/home/app/.local/bin:$PATH"
RUN poetry self update --preview

COPY pyproject.toml .
COPY poetry.lock .
COPY app/ .

RUN poetry install

RUN poetry run python3 download_model.py

RUN rm /home/app/.huggingface/token

CMD poetry run streamlit run app.py

FROM builder as runner

CMD poetry run streamlit run app.py