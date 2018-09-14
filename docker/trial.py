from dask_kubernetes import KubeCluster
from dask.distributed import Client
from operator import add


try:
    cluster = KubeCluster.from_yaml('/pod_config_test.yaml')
    cluster.adapt(minimum=1, maximum=2)
    print(cluster)
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

except:
    print("DIFFERENT------------------")
    rollback()

finally:
    client.close()
    cluster.close()
