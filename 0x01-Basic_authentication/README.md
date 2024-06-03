# Basic Authentication Project

## Background Context

In this project, you will learn about the authentication process and how to implement Basic Authentication on a simple API. While in a professional setting, it is recommended to use established modules or frameworks for authentication (such as Flask-HTTPAuth in Python), this project aims to provide a hands-on understanding of the basic mechanism by building it from scratch.

## Resources

To help you through this project, refer to the following resources:

- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)
- [Base64 in Python](https://docs.python.org/3.7/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask](https://palletsprojects.com/p/flask/)
- [Base64 - concept](https://en.wikipedia.org/wiki/Base64)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without external references:

### General

- **What authentication means**: Understand the purpose and importance of verifying the identity of users or systems interacting with an application.
- **What Base64 is**: Learn about this binary-to-text encoding scheme that is commonly used to encode data in a way that can be safely transmitted over protocols that are designed to handle textual data.
- **How to encode a string in Base64**: Gain practical skills in converting strings to Base64 format using Python.
- **What Basic authentication means**: Comprehend the method for an HTTP user agent to provide a user name and password when making a request.
- **How to send the Authorization header**: Learn how to include the appropriate header in an HTTP request to provide credentials for Basic Authentication.

## Project Structure

This project is structured to gradually introduce you to the concepts and implementation details of Basic Authentication. You will start with the basics of authentication and encoding, and then move on to implementing these in a simple Flask-based API.

### Steps

1. **Understanding Authentication**: 
   - Study the concept of authentication and why it is necessary.
   - Learn about different authentication mechanisms, with a focus on Basic Authentication.

2. **Learning Base64 Encoding**:
   - Understand what Base64 encoding is and why it is used.
   - Practice encoding and decoding strings using Base64 in Python.

3. **Implementing Basic Authentication**:
   - Learn how Basic Authentication works and how to implement it in an HTTP context.
   - Implement a simple API using Flask that uses Basic Authentication.

4. **Sending the Authorization Header**:
   - Understand the structure of the HTTP Authorization header.
   - Learn how to include this header in your HTTP requests.

### Practical Implementation

You will implement a Flask API that requires Basic Authentication for access. The steps will include:

1. Setting up a Flask application.
2. Creating routes that require authentication.
3. Implementing Base64 encoding for the username and password.
4. Validating the encoded credentials on the server side.
5. Testing the API with authenticated and unauthenticated requests.

## Conclusion

By the end of this project, you will have a solid understanding of how Basic Authentication works and how to implement it in a Flask API. This foundational knowledge will be valuable as you move on to more complex authentication systems and frameworks in professional settings.
