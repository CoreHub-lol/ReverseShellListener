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
    host = "0.0.0.0" 
    port = 9001       # Change Port 
    start_listener(host, port)