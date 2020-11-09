FROM python:3.9.0-slim-buster
ARG USER_ID
ARG GROUP_ID
ENV INPUT_FOLDER=/workspace/input
ENV OUTPUT_FOLDER=/workspace/output
ENV CURL_CA_BUNDLE=
RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
RUN mkdir -p ${INPUT_FOLDER}
RUN mkdir -p ${OUTPUT_FOLDER}
USER user
WORKDIR /workspace
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY lib/main.py .
CMD  python main.py -i /workspace/input -o /workspace/output