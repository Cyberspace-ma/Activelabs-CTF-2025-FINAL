# Waving Writeup

## Overview

The "waving" challenge is an audio forensics puzzle that involves hidden information embedded within a WAV file. To uncover the hidden flag, you need to use Audacity, an audio editing software, to manipulate the file and reveal the flag. This challenge tests your ability to analyze audio files and interpret spectrograms.

## Solution

To extract the hidden flag from the WAV file, follow these steps:

### Step 1: Open the File in Audacity

1. **Download the WAV file** (in this case, `waving.wav`).
2. **Install Audacity** if you don't have it already (it is a free and open-source audio editing software available for Windows, macOS, and Linux).
3. **Open Audacity** and load the WAV file by clicking on `File` > `Open`, then selecting `waving.wav`.

### Step 2: Switch to Spectrogram View

1. Once the file is loaded into Audacity, you should see the waveform of the audio.
2. To view the hidden flag, we need to switch to a **spectrogram view**:
   - Click on the track name (usually at the left, where it says "Audio Track").
   - Select `Spectrogram` from the dropdown menu. You might need to select `Waveform (dB)` first and then change it to `Spectrogram`.
   
### Step 3: Analyze the Spectrogram

After switching to the spectrogram view, you should now see visual patterns. Hidden within the spectrogram is a **flag** that looks like text. The flag might be hidden in the form of a pattern that can be revealed through this view.

### Step 4: Extract the Flag

- Carefully analyze the spectrogram, and you should see a hidden string of text. This string represents the **flag**.
- The flag will be in the format `CSP{...}`, and it might appear as a series of frequencies or shapes within the spectrogram.
