from dask_kubernetes import KubeCluster
from dask.distributed import Client
from operator import add


try:
    print("1")
    cluster = KubeCluster.from_yaml('/pod_config_test.yaml')
    print("2")
    print(cluster)
    print("3")
    cluster.scale_up(1)
    print(cluster)
    print("HERE")
    client = Client(cluster)
    print(client)
    z = client.get({'x': (add, 1, 2)}, 'x')
    print("HERE-----------------------------", z)
    """
    x = client.submit(inc, 10)
    print(x)
    print(4)
    z = client.gather(x)
    print(5)
    """
    print(z)

except(KeyboardInterrupt, SystemExit):
    print("caught********************")

finally:
    client.close()
    cluster.close()
