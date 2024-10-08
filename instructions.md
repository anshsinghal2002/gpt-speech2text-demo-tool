# Speech-Prompt-Demo Instructions
## FFmpeg Installation Guide for Windows

This guide will help you install FFmpeg on a Windows system from a downloaded build file.

## Step 1: Download FFmpeg

1. Download the ffmpeg build zipfile attached

## Step 2: Extract the Files

1. Locate the downloaded `.zip` file in your Downloads folder.
2. Right-click on the `.zip` file and select "Extract All."
3. Choose a destination folder (e.g., `C:\Program Files\ffmpeg`) and click "Extract."

## Step 3: Move FFmpeg to a System Path

1. **Add FFmpeg to System PATH:**
   - Right-click on "This PC" or "My Computer" and select "Properties."
   - Click on "Advanced system settings."
   - In the System Properties window, click the "Environment Variables" button.
   - In the "System variables" section, find the `Path` variable and select it, then click "Edit."
   - Click "New" and add the following path:
     ```
     C:\Program Files\ffmpeg\bin
     ```
     You may also click `browse` and use the file explorer GUI to select the `C:\Program Files\ffmpeg\bin` folder
   - Click "OK" to close all dialog boxes.

## Step 4: Verify the Installation

1. Open the Command Prompt:
   - Press `Win + R`, type `cmd`, and hit `Enter`.

2. In the Command Prompt, run the following command:
   ```bash
   ffmpeg -version

# Running the code
- Update the CONFIG.json file with a valid OpenAI Secret Key
- Run 

    ```bash
    pip install --no-cache-dir -r requirements.txt
    python main.py
    ```
- Once the program starts, it should say 'Recording', give it a prompt, then hit `Ctrl+C` to stop recording
- gpt-4o generated response should be printed to console.
