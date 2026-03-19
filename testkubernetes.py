from kubernetes import client, config

# Load config from kubeconfig
config.load_kube_config()

# Create API client
v1 = client.CoreV1Api()

# List pods in default namespace
pods = v1.list_namespaced_pod(namespace="default")
print(pods)
for pod in pods.items:
    print(f"Pod: {pod.metadata.name}, Status: {pod.status.phase}")

# List pods in all namespaces
# all_pods = v1.list_pod_for_all_namespaces()
# for pod in all_pods.items:
#     print(f"{pod.metadata.namespace}/{pod.metadata.name}: {pod.status.phase}")
