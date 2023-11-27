# CoAP Simulation with Block-Wise Transfer

This repository contains Python scripts for simulating CoAP communication with a focus on block-wise transfer for optimized performance. The simulation includes both the CoAP server and client, implementing the vanilla CoAP approach and an optimized block-wise transfer approach.

## Contents:

1. **CoAP Server Scripts:**
   - **coap_server_simulation.py:** Basic CoAP server simulation.
   - **coap_server_optimized_blockwise.py:** CoAP server with block-wise transfer optimization.

2. **CoAP Client Scripts:**
   - **coap_client_simulation.py:** Basic CoAP client simulation.
   - **coap_client_optimized_blockwise.py:** CoAP client with block-wise transfer optimization.

3. **Additional Scripts:**
   - **coap_client_results.csv:** CSV file storing results from the basic CoAP client simulation.
   - **coap_client_results_blockwise.csv:** CSV file storing results from the CoAP client with block-wise transfer simulation.

## How to Run:

1. **CoAP Server:**
   - Run `coap_server_simulation.py` for the basic CoAP server.
   - Run `coap_server_optimized_blockwise.py` for the optimized CoAP server with block-wise transfer.

2. **CoAP Client:**
   - Run `coap_client_simulation.py` for the basic CoAP client.
   - Run `coap_client_optimized_blockwise.py` for the CoAP client with block-wise transfer.

## Dependencies:

- [aiocoap](https://aiocoap.readthedocs.io/en/latest/index.html): Library for CoAP communication in Python.

## Results:

- Basic CoAP client results are stored in `coap_client_results.csv`.
- Optimized CoAP client (block-wise) results are stored in `coap_client_results_blockwise.csv`.

## Notes:

- Adjust server address and parameters in the client scripts as needed.
- Ensure that dependencies are installed (`pip install aiocoap`).

## References:

- [RFC 7252 - The Constrained Application Protocol (CoAP)](https://datatracker.ietf.org/doc/rfc7252/)
- [Block-Wise Transfer in CoAP (RFC 7959)](https://datatracker.ietf.org/doc/rfc7959/)

Feel free to explore and modify the scripts based on your specific use case and requirements. For any questions or issues, please refer to the provided references or open an issue in the repository.
