# Wi-Fi and WARP Auto-Connect

This script allows automatic connection to a specific Wi-Fi network and enables WARP if connected. It periodically checks the Wi-Fi connection status and the connectivity to a remote server to determine the actions to be taken.

## Prerequisites

- Python 3.x
- `warp-cli` command-line tool (installed and accessible in the system's PATH)
- Windows operating system (the script uses Windows-specific commands)

## Installation

1. Clone the repository or download the `auto_connect.py` script.

   ```shell
   git clone https://github.com/kvxrun/auto-WARP-connect.git
   ```

2. Install the required Python packages.

   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Modify the `REMOTE_SERVER` variable in the `auto_connect.py` script to specify the remote server you want to use for connectivity testing.

2. Open a command prompt or terminal and navigate to the directory containing the `auto_connect.py` script.

3. Run the script.

   ```shell
   python auto_warp_connect.py
   ```

4. The script will start monitoring the Wi-Fi connection and perform automatic actions based on the status.

   - If connected to the specified Wi-Fi network and able to reach the remote server, it will check if WARP is connected. If not, it will connect to WARP.
   - If not connected to the specified Wi-Fi network or unable to reach the remote server, it will check if WARP is connected. If connected, it will disconnect WARP.

5. To stop the script, press `Ctrl+C` in the command prompt or terminal.

## Customization

You can customize the script by modifying the following variables:

- `REMOTE_SERVER`: Specify the remote server hostname or IP address to test connectivity.
- `ssid`: Specify the Wi-Fi network where you want WARP to be enabled.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```
