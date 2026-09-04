# ClashOrigins Client
An easy to set up Clash of Clans v1.7.0 client. It is also optimized for iPhones with a 4 inch screen such as the iPhone 5, 5c and 5s.

[![Telegram](https://img.shields.io/badge/Telegram-@ClashOrigins-26A5E4?logo=telegram&logoColor=white)](https://t.me/ClashOrigins) [![Download IPA](https://img.shields.io/badge/Download-IPA-blue?logo=apple&logoColor=white)](https://github.com/frmnnet/ClashOrigins-Client/releases/latest)

## Requirements
- *Python 3.6+*
- *A jailbroken ARMv7 iOS device running iOS 4.3-10.3.3, with AppSync installed*
- *A Clash of Clans v1.7.0 server*

## Configuration
Edit the IP and port to yours at the top of `Patcher.py` first.


# Setup

## Step 1

Rename the IPA to ZIP format:

```bash
ClashOrigins.ipa → ClashOrigins.zip
```

Extract it

A `Payload` folder will appear containing `ClashOrigins.app`.

## Step 2
Open terminal and navigate to the app bundle:

```bash
cd Payload/ClashOrigins.app
```

Run the python script:

```bash
# MacOS & Linux
python3 patcher.py

# Windows 
py patcher.py
```

If the binary was successfully patched, go to step 3.

## Step 3

Compress `Payload` and rename it to ipa.

```bash
Payload → Payload.zip → Payload.ipa
```

## Step 4
Install the IPA using your preferred sideloading method.

## If you have encountered any problems, feel free to open an issue.
