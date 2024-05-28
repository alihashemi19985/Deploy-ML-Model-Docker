# Description and  Overview

This project presents a comprehensive workflow encompassing the training, serialization, and deployment of a machine learning model alongside a Flask web application, all encapsulated within a Dockerized environment. Initially, the model is meticulously trained and serialized to ensure efficient storage and retrieval of its predictive capabilities. Subsequently, a Flask application is developed to establish an API endpoint, facilitating seamless communication between users and the trained model. Importantly, the predictions generated by the model are stored in a database, enabling persistent storage and easy retrieval for subsequent analysis or utilization. Finally, the entire project is containerized using Docker, ensuring portability, scalability, and ease of deployment across diverse computing environments. Through the integration of machine learning, web development, database management, and containerization technologies, this project provides a robust and efficient solution for deploying and managing machine learning models in real-world applications.

1. Train the RF model for the iris data set (you can use any model and dataset) 
2. Save and export the ML model.
3. Create a Flask app to API http connection
4. Create a schema to the database (sql.init)
5. Create the dockerfile
6. Create the Docker-compose
7. Run the docker-compose 

# Installation 

Install the docker on Ubuntu 

# Deploy 

To run the app first, in the terminal enter 'sudo docker-compose up'. finally, to API request enter '''curl -X POST ip-address:5000/predict -H "Content-Type: application/json" -d '{"features": [10, 10, 100, 19]}' '''
