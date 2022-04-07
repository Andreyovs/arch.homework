### Инструкция по запуску

victory@edg-xps:~/otus/arch_homework/HW1$ docker build -t otus_hw1 .

victory@edg-xps:~/otus/arch_homework/HW1$ docker login
    Authenticating with existing credentials...
    Login Succeeded
victory@edg-xps:~/otus/arch_homework/HW1$ docker tag otus_hw1 andreyovs/otus_hw1:1.0.0
victory@edg-xps:~/otus/arch_homework/HW1$ docker push andreyovs/otus_hw1:1.0.0
victory@edg-xps:~/otus/arch_homework/HW1$ minikube delete --all --purge
victory@edg-xps:~/otus/arch_homework/HW1$ minikube start --vm-driver=virtualbox
victory@edg-xps:~/otus/arch_homework/HW1$ minikube addons enable ingress
victory@edg-xps:~/otus/archeval $(minikube -p minikube docker-env)
victory@edg-xps:~/otus/arch_homework/HW1$ kubectl apply -f .

victory@edg-xps:~/otus/arch_homework/hw1$ kubectl config set-context --current --namespace=otus
    Context "minikube" modified.
victory@edg-xps:~/otus/arch_homework/hw1$ kubectl get pods
    NAME                         READY   STATUS    RESTARTS   AGE
    otus-hw-1-7469c8cc49-4r755   1/1     Running   0          34m
    otus-hw-1-7469c8cc49-c496j   1/1     Running   0          34m
victory@edg-xps:~/otus/arch_homework/hw1$ kubectl describe svc otus-hw-1
    Name:                     otus-hw-1
    Namespace:                otus
    Labels:                   app=otus-hw-1
    Annotations:              <none>
    Selector:                 app=otus-hw-1
    Type:                     NodePort
    IP Family Policy:         SingleStack
    IP Families:              IPv4
    IP:                       10.99.3.17
    IPs:                      10.99.3.17
    Port:                     <unset>  8000/TCP
    TargetPort:               8000/TCP
    NodePort:                 <unset>  30690/TCP
    Endpoints:                172.17.0.4:8000,172.17.0.5:8000
    Session Affinity:         None
    External Traffic Policy:  Cluster
    Events:                   <none>

#### Тест

victory@edg-xps:~/otus/arch_homework/hw1$ minikube ip
    192.168.59.104
victory@edg-xps:~/otus/arch_homework/hw1$ kubectl get svc
    NAME             TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)          AGE
    health-service   LoadBalancer   10.103.219.63   10.103.219.63   8000:31917/TCP   78m
    otus-hw-1        NodePort       10.99.3.17      <none>          8000:30690/TCP   44m
victory@edg-xps:~/otus/arch_homework/hw1$ curl 192.168.59.104:30690
    {"Hello":" from docker otus-hw-1-7469c8cc49-c496j"}
victory@edg-xps:~/otus/arch_homework/hw1$ curl 192.168.59.104:31917
victory@edg-xps:~/otus/arch_homework/hw1$ curl 192.168.59.104:30690/health
    {"status":"OK"}
