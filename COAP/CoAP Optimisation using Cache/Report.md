**Implementation:**
A K-way set associative cache handles the reuests before they're sent to server. 
If cache is hit, it just returns the resource to the client.
In case of miss, the cache forwards the request to server and saves the response for later use and then returns the resource to the client.

**Benefits of Caching in CoAP:
**
Reduced Latency: Clients receive quicker responses from intermediate caches instead of waiting for a round-trip to the origin server.

Bandwidth Savings: Caching reduces the need to transmit the same data repeatedly, conserving network bandwidth.

Server Load Reduction: Origin servers experience lower load as cached responses are served by intermediate nodes.
