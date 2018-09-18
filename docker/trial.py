from operator import add
from dask_kubernetes import KubeCluster
from dask.distributed import Client
from kubernetes.client.rest import ApiException


try:
    cluster = KubeCluster.from_yaml('/pod_config_test.yaml')
    cluster.scale_up(1)
    client = Client(cluster)
    answer = client.get({'x': (add, 1, 2)}, 'x')
    print("the answer is:", answer)

except(KeyboardInterrupt, SystemExit):
    pass

except ApiException:
    print("Caught API Exception")

finally:
    client.close()
    cluster.close()
