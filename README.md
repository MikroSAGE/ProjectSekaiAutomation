# Project Sekai Automation with Python, OpenCV, and PythonADB

This project aims to automate certain aspects of the mobile rhythm game "Project Sekai: Colorful Stage!" using Python along with OpenCV, PythonADB, and PyAutoGUI. The automation prototype utilizes PyAutoGUI for basic interaction with the game, OpenCV for computer vision tasks, and PythonADB for controlling an Android device connected to your computer.

## Requirements

To run this project, you need to have the following components installed:

- Python 3.x (https://www.python.org/downloads/)
- OpenCV (https://opencv.org/)
- PythonADB (https://pypi.org/project/pythonadb/)
- PyAutoGUI (https://pyautogui.readthedocs.io/)

It is recommended to set up a virtual environment to keep the project dependencies isolated.

## Setup

1. Clone the repository to your local machine:

```
git clone https://github.com/MikroSAGE/project-sekai-automation.git
```

2. Navigate to the project directory:

```
cd ProjectSekaiAutomation
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

4. Connect your Android device to your computer and ensure USB debugging is enabled.

## Usage

1. Launch the "Project Sekai: Colorful Stage!" game on your Android device.

2. Run the Python script:

```
python main.py
```

3. The script will utilize the connected Android device to perform various actions in the game, such as tapping notes and navigating menus. Make sure to keep the game window visible and in the foreground while the script is running.

## Customization

The `automate_project_sekai.py` script provides a basic prototype for automating the game. You can modify and extend the script according to your specific needs. Some possible customizations include:

- Adding additional computer vision tasks using OpenCV to detect game elements.
- Implementing advanced automation logic based on game state.
- Integrating AI techniques for more intelligent gameplay.

Feel free to explore the script and make changes based on your requirements.

## Limitations

Please note that automating games can be against the terms of service or rules set by the game developers. Make sure to review the game's terms and conditions before using any automation tools or techniques.

Additionally, the effectiveness and stability of this automation script may vary depending on factors such as game updates, device configurations, and screen resolutions. It is recommended to test the script thoroughly and adapt it as needed.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have ideas for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

This project is for educational and personal use only. The developers of this project are not responsible for any consequences resulting from the misuse or unethical use of the automation tools provided.
