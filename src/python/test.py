import uuid

import time

from src.python.client import ChaosMeshClient, Experiment
from src.python.selector import Selector

client = ChaosMeshClient()
selector = Selector(labelSelectors={"app": "filebeat"})

# name of the experiment
exp_name = str(uuid.uuid4())

# starting up the pod failure experiment
client.start(Experiment.K8S_POD_FAILURE, namespace="default", name=exp_name, selector=selector)
time.sleep(10)

# pausing the experiment
client.pause(Experiment.K8S_POD_FAILURE, namespace="default", name=exp_name)

exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start(Experiment.K8S_POD_KILL, namespace="default", name=exp_name, selector=selector)
time.sleep(10)

# pausing the experiment
client.pause(Experiment.K8S_POD_KILL, namespace="default", name=exp_name)
