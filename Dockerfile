FROM ubuntu:22.04

ENV TZ=UTC
RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    apt update && \
    apt install -y tzdata && \
    dpkg-reconfigure -f noninteractive tzdata

RUN apt update && apt install -y \
    libgl1-mesa-glx \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    iputils-ping \
    jq \
    python3.10 \
    python3-pip \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos '' --shell /bin/bash user \
 && mkdir -p /app \
 && chown -R user:user /app

ENV HOME=/home/user
ENV PYTHONPATH "/app:${PYTHONPATH}"
ENV PATH "/home/user/.local/bin:${PATH}"

RUN pip install --upgrade pip setuptools

WORKDIR /app

COPY requirements.txt setup.py MANIFEST.in ./
RUN mkdir -p /app/family_accounting && \
    chown -R user:user /app

COPY family_accounting/__init__.py ./family_accounting

USER user

RUN pip install -e .

CMD ["/bin/bash"]
