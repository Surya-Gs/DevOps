Kubernetes is a portable, extensible and open source platform for managing containerized workload and services, which faciliates for declarative configuration and automation



Deployment:
1) Traditional-Many applications in a single physical server
2) Virtualization- 
3) Containerization
Containers ares similar to VM's




Benifits of containers:
1. Agile application creattion and Deployment.
2. Continous development integration and Deployment
3. Dev and ops seperation concers
4. Observability
5. Environmental consistency
5. Cloud and OS level portability
6. Application-centric management
7. Loosely couple distributed, elastic, liberated, microservices
8. Resource Isolation
9. Resource utilization 

why kubernetes

Service discovery and load balancing
Storage orchestration
Automated rollouts and rollbacks
Automatic rollouts and rollbacks
Automatic bin packing
self healing
secret and configuration manmagement
Batch execution
Horizontal scaling
Ipv4/Ipv6 dual stack




Kubernetes components

Control Plane(master node)
    -Kube-api-server
    -etcd
    -kube-scheduler
    -controller-mangeSlice controller
        -ServiceAccountController
        -Node controller
        -Job controller
        -Endpoint 
    -cloud-control-plane-manager
Worker node
    -kubelet
    -kube-proxy




Kubernetes api server
    -kubectl-command line tool for communicating with kubernetes control plane server
     -kube-adam
