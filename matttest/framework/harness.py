"""Contains a set of classes for manipulating test applications."""

import yaml

from kubernetes import client, config

class KubernetesHarness(object):
    """A harness for a kubernetes container."""

    def __init__(self):
        config.load_kube_config()


class DeploymentHarness(KubernetesHarness):
    """A harness for operating with a deployment."""

    def __init__(self):
        with open(self.conf_file) as this_conf_file:
            self.dep_conf = yaml.safe_load(this_conf_file)
