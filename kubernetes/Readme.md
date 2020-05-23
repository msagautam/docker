# Create Pod from Yaml file
kubectl create -f pod.yaml

# Describe Pod
kubectl describe pod my-first.pod

# Delete Pod
kubectl delete -f pod.yaml
kubectl delete pod/nginx

# List Pods in vanilla Kube system namespace
kubectl -n kube-system get pods

# Create Yaml file of a Pod "kube-proxy"
kubectl -n kube-system get pod kube-proxy -o yaml 

# Create service to open/expose ports
kubectl create -f service.yaml
# Update the service if we have changed configuration in the yaml file
kubectl apply -f service.yaml
