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

1. Save the following Python script

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