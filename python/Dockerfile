FROM public.ecr.aws/lambda/python:3.9

COPY ca-chain.pem client-cert.pem client-key.pem ${LAMBDA_TASK_ROOT}
COPY app.py ${LAMBDA_TASK_ROOT}

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

CMD [ "app.lambda_handler" ]
