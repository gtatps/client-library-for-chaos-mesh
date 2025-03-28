import time 

from chaosmesh.client import Client, Experiment
from chaosmesh.k8s.selector import Selector

# creating the ChaosMesh client
client = Client(version="v1alpha1")

# target pods selector; by labelSector or by pods in specified namespaces
selector = Selector(labelSelectors={"app": "webrtc-server"}, pods=None, namespaces=['ps-dev'])

# name of the experiment
exp_name = "network-delay-100ms"

# namespace in which to create the NetworkChaos object
ns_name = "ps-dev"

# default latency
latency = "100ms"

# starting up the pod failure experiment
client.start_experiment(Experiment.NETWORK_DELAY, namespace=ns_name, name=exp_name, selector=selector, latency=latency)

# After we're done with the experiment we should delete it
time.sleep(10)
client.delete_experiment(Experiment.NETWORK_DELAY, namespace=ns_name, name=exp_name)

