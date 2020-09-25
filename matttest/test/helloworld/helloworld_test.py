from os import path

import yaml

from matttest.framework.harness import DeploymentHarness

class HelloworldHarness(DeploymentHarness):
    """A harness for the helloworld application."""

    def __init__(self):
        self.conf_file = path.abspath(path.join(
            file_dir, '..', 'k8s', 'helloworld-deployment.yaml'
        ))
        super(HelloworldHarness, self).__init__()

class TestHelloworld:
    def test_basic(self):
        assert True


def main():
    print(__file__)
    file_dir = path.dirname(__file__)

    with open(conf_filename) as conf_file:
        deployment = yaml.safe_load(conf_file)
        k8s_apps_v1 = client.AppsV1Api()
        try:
            response = k8s_apps_v1.create_namespaced_deployment(
                body=deployment, namespace="helloworld"
            )
        except client.rest.ApiException as e:
            print(e)
        print("Deployment created.  status={0}".format(response.metadata.name))