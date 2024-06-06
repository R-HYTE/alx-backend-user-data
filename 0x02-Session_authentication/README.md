# Implementing Session Authentication in Flask

## Project Overview

In this project, you will implement a Session Authentication system using Flask without installing any additional modules. While in professional settings, it's advisable to use established libraries or frameworks for session management (such as Flask-HTTPAuth), this exercise is designed to help you understand the underlying mechanisms by building them from scratch.

## Industry Best Practices

In real-world applications, you should avoid implementing your own session authentication system due to potential security risks and complexities. Instead, you should rely on well-tested modules or frameworks that handle authentication securely and efficiently. However, for educational purposes, this project will guide you through the implementation process step-by-step.

## Resources

To complete this project, refer to the following resources:

- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY): Focus on the session authentication part.
- [HTTP Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie)
- [Flask Documentation](https://palletsprojects.com/p/flask/)
- [Flask Cookie](https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies)

## Learning Objectives

By the end of this project, you will be able to explain the following concepts clearly:

### General

- **What authentication means:** Authentication is the process of verifying the identity of a user or system, typically by requiring credentials (e.g., username and password).

- **What session authentication means:** Session authentication involves maintaining a session for each user after they log in, using session IDs stored in cookies to track and authenticate the user's subsequent requests.

- **What Cookies are:** Cookies are small pieces of data sent from a server to a client's web browser and stored on the client's device. They are used to remember stateful information for the user's subsequent visits.

- **How to send Cookies:** Cookies can be sent from the server to the client using the `Set-Cookie` HTTP header in the server's response.

- **How to parse Cookies:** Cookies sent by the client in subsequent requests can be parsed from the `Cookie` HTTP header to retrieve session information.

## Implementation Steps

1. **Setup Flask Project:**
   - Create a basic Flask application.
   - Define routes for login, logout, and protected resources.

2. **User Authentication:**
   - Implement a simple user authentication mechanism.
   - Verify user credentials and create a session.

3. **Session Management:**
   - Generate session IDs and store them on the server.
   - Send session IDs to clients via cookies.
   - Retrieve and verify session IDs from incoming requests.

4. **Cookie Handling:**
   - Use Flask to set and read cookies.
   - Understand how to securely handle cookies.

5. **Protecting Routes:**
   - Implement route protection to ensure only authenticated users can access certain endpoints.

By following these steps, you will build a simple yet functional session authentication system in Flask, enhancing your understanding of web authentication mechanisms and cookie handling.

---

### Practical Exercise

Let's start by setting up the basic structure of our Flask application and implementing user login and session management.

#### Step 1: Setup Flask Project

Create a file named `app.py` and add the following code:

```python
from flask import Flask, request, jsonify, make_response
import uuid

app = Flask(__name__)

# In-memory storage for users and sessions
users = {
    "john": "hello",
    "susan": "bye"
}
sessions = {}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        session_id = str(uuid.uuid4())
        sessions[session_id] = username
        response = make_response(jsonify({"message": "Login successful"}))
        response.set_cookie('session_id', session_id)
        return response
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/protected', methods=['GET'])
def protected():
    session_id = request.cookies.get('session_id')
    if session_id and session_id in sessions:
        return jsonify({"message": f"Hello, {sessions[session_id]}!"})
    else:
        return jsonify({"message": "Unauthorized"}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session_id = request.cookies.get('session_id')
    if session_id in sessions:
        sessions.pop(session_id)
        response = make_response(jsonify({"message": "Logged out"}))
        response.delete_cookie('session_id')
        return response
    else:
        return jsonify({"message": "No active session"}), 401

if __name__ == '__main__':
    app.run()
```

# Conclusion

By completing this project, you'll gain a solid understanding of how session authentication works and how to manage cookies in a Flask application. This knowledge will be beneficial for understanding more complex authentication mechanisms and for developing secure web applications.
