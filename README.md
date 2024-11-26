# Trip Stitching using beckn protocol

## Project Overview

This project aims to implement the **Trip Stitching Algorithm** for multi-modal transportation using the **Beckn protocol**. The goal is to create an API that efficiently integrates multiple mobility catalogs (e.g., ride-hailing, public transit, rentals) and provides optimized trip options for users based on parameters like cost or distance.

### Key Objectives:
- Develop a **RESTful API** that allows users to search for travel options between two points.
- Optimize multi-modal trip options by sorting them based on parameters such as **cost** or **distance**.
- Integrate multiple mobility catalogs (e.g., ride-hailing, public transit, car rentals) for a seamless user experience.
- Implement the **Beckn protocol** for real-time.

### My Contributions:
  # I reffered the official documentation of beckn:-# https://developers.becknprotocol.io/docs/developer-documentation/transaction-layer/getting-a-list-of-mobility-service-providers-that-can-transport-a-traveller-from-a-pickup-location-to-a-drop-location-node-js/

- **Implementation of the Trip Stitching Algorithm**: I worked on implementing the core algorithm that stitches different travel modes into a seamless journey.
- **API Development**: I contributed to the development of a RESTful API that can efficiently search for and return multi-modal trip options.
- **Optimization**: Focused on improving the efficiency of the algorithm by considering optimization parameters like **cost** and **distance**.
- **Integration of Mobility Catalogs**: Worked on integrating multiple mobility catalogs into the trip stitching algorithm, ensuring that the final trips returned are accurate and optimal.

### Current Issues:
  - **API Endpoints Not Working**: API endpoints are currently non-functional, facing an issue with the pickup and drop location fields in the API request. The API does not properly handle these fields, causing errors when they are missing or incorrectly formatted.
  - **Current Status**: I am in the process of fixing this issue but I would appreciate it if you could review the implementation and guide me on how best to resolve this issue.
  - 
### Technologies Used:
- **Programming Languages**: Python
- **Web Framework**: Flask
- **Data Formats**: JSON
- **Protocol**: Beckn

### How It Works:
- **Input**: Pickup and drop locations, a list of available mobility catalogs (ride-hailing, public transit, rentals), and an optimization parameter (cost or distance).
- **Output**: An array of multi-modal trip options, sorted by the selected optimization parameter (e.g., lowest cost or shortest distance).
- **Working**: The API integrates with the Beckn protocol to fetch real-time trip data, process it using the Trip Stitching Algorithm, and return the best multi-modal travel options based on the input parameters.

