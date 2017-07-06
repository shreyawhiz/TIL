**Load balancing** refers to efficiently distributing incoming network traffic across a group of backend servers, also known as a server farm or server pool.


Modern high-traffic websites must serve hundreds of thousands, if not millions, of concurrent requests from users or clients and return the correct text, images, video, or application data, all in a fast and reliable manner. 

To cost-effectively scale to meet these high volumes, modern computing best practice generally requires adding more servers.

>A load balancer acts as the **traffic cop** sitting in front of your servers and routing client requests across all servers capable of fulfilling those requests in a manner that maximizes speed and capacity utilization and ensures that no one server is overworked, which could degrade performance. 

>If a single server goes down, the load balancer redirects traffic to the remaining online servers. When a new server is added to the server group, the load balancer automatically starts to send requests to it.

So, a load balancer performs the following functions:
1. Distributes client requests or network load efficiently across multiple servers
2. Ensures high availability and reliability by sending requests only to servers that are online
3. Provides the flexibility to add or subtract servers as demand dictates


