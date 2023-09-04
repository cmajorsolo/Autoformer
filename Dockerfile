# Because Sagemaker is tasking care of building the docker image, it will install the dependencies using the requirements.txt automatically. 
FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

RUN apt-get update && apt-get install gcc -y

RUN pip install sagemaker-pytorch-training