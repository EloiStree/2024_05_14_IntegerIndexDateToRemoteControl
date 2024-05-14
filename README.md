# 2024_05_14_IntegerIndexDateToRemoteControl

You can find here an example of how you can push integer values on IID without RSA system.

In the context of remote control, you want to be able to read input and simulate input on devices.

Because Bluetooth is very slow, I realized that you need to send a minimum of 2 bytes to have a large range of actions on it. But as for the use of 99 instead of 1999, we are quickly short. So I decided to create some tools around 4 bytes that are represented by an integer.

As hosting a server and having a fixed IP cost and is not easy to set up, I created a WebSocket server with an RSA key to make the communication on devices on a shared server for all.

That's cool and all, but the DateTime of devices are not the same everywhere and networks have some latency. So, in order to do macros and actions at precise times, you also need a ulong used to store the date and the kind of date you are using.

You can find the server code in WebSocket version here: [https://github.com/EloiStree/2024_04_04_IndexIntegerDateTunnelingRSA](https://github.com/EloiStree/2024_04_04_IndexIntegerDateTunnelingRSA)

In order to not have the RSA key that identifies you everywhere, I created some gates that are UDP and WebSocket localhost: [https://github.com/EloiStree/2024_05_11_GateIID_WS_Python](https://github.com/EloiStree/2024_05_11_GateIID_WS_Python)

What is left to do is to provide a range of scripts that allow you to read input from your devices and push them as input to be simulated by actions on the target devices.

That's where this repository aims to be. Provide a range of samples to be used to do remote control.

Note that I had a tool called OMI in Unity that was doing that. But can you trust an app that does lots of things you can't understand? That's why I switched to small Python scripts. If you can understand it, you can use it.
