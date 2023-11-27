# CSN-341-Project_Group10
This project involves implementation of MQTT QoS versions and CoAP along with their
comparisons to each other as well as to HTTP versions. It also involves some
optimizations made to the CoAP for energy efficiency and performance as well as
several other approaches were discussed.
## MQTT : MQTT (Message Queuing Telemetry Transport) 
- It is a lightweight messaging protocol designed for low-bandwidth, high-latency, or unreliable networks.
- It operates on a publish-subscribe model, where clients communicate through a broker.
  **Key features**
  - Include Quality of Service (QoS) levels (0, 1, 2) for message delivery assurance, a nsimple header structure, and support for last will and testament.
  - It uses TCP/IP or other transport protocols and is widely used in IoT (Internet of Things) and real-time communication applications due to its efficiency and reliability.
  - MQTT (Message Queuing Telemetry Transport) Provides three Quality of Service (QoS) levels:
    **1. QoS 0(At most once):**
    -Messages are delivered with no confirmation. This leveloffers the least reliability, as there is no acknowledgment of message receipt.
    **2.QoS 1 (At least once):**
    - Messages are delivered at least once, and acknowledgment is requested.
    - If acknowledgment isn't received, the message is resent, ensuring delivery but possibly resulting in duplicates.
    **3. QoS 2 (Exactly once):**
    - Messages are delivered exactly once through a four-step handshake process, ensuring no duplicates and guaranteeing message delivery.
    - QoS 2 provides the highest level of reliability but involves more overhead.
    **4 The different MQTT QoS versions are compared here :**
      -https://1drv.ms/w/s!AhlNMIrAhB6ngxoqF9Pf6M-VPpDO?e=ChpRL4
## CoAP : CoAP (Constrained Application Protocol)
-It is s a lightweight, Restful communication protocol designed for resource-constrained devices and low-power,lossy networks. 
-Operating over UDP, CoAP enables efficient data exchange and interaction between devices in the Internet of Things (IoT).
-It supports basic request-response, resource discovery, and asynchronous communication. 
-CoAP is designed to be simple, scalable, and suitable for devices with limited resources, making it a preferred choice for IoT applications where efficiency
and constrained environments are paramount.

## Summary: 
- This project implements MQTT protocols in Python, comparing its performance with HTTP.
- Client script facilitates interactive MQTT message sending and records response times.
- Graph scripts visualize message counts and response times.
- HTTP server script establishes a basic server for handling POST requests.
- Files store response times for various message sizes.
- It simulates concurrent MQTT and HTTP operations, logging results.
- Overall, the project enables practical analysis of MQTT and the version comparisons.

In the realm of optimizing CoAP for challenging network conditions, a nuanced strategy
emerges.Intelligent retransmission strategies, including dynamic timeout adjustments
and exponential backoff, tackle packet loss issues. The adaptive resizing of block sizes
for block-wise transfers responds dynamically to observed network conditions,
optimizing data transfer efficiency.Priority handling mechanisms ensure critical messages take precedence, offering a
strategic edge where time-sensitive processing is paramount. Congestion control
mechanisms, dynamic resource discovery, and asynchronous communication through
CoAP's observe option contribute to network stability, adaptability, and reduced latency.
Efficient payload compression and strategic proxy deployment enhance message flow
and overall network efficiency. Adaptive security measures, dynamic resource
discovery, energy-efficient communication for constrained devices, and mechanisms for
graceful degradation further fortify CoAP's performance in challenging scenarios.
Rigorous testing in realistic conditions remains imperative to validate the effectiveness
of these optimizations across diverse use cases.
