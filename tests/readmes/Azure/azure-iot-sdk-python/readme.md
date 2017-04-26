# Microsoft Azure IoT SDKs for Python

This repository contains the following:

* **Azure IoT Hub Device SDK for Python**: to connect client devices to Azure IoT Hub
* **Azure IoT Hub Service SDK for Python**: enables developing back-end applications for Azure IoT

To find SDKs in other languages for Azure IoT, please refer to the [azure-iot-sdks][azure-iot-sdks] repository.

To create and manage an instance of IoT Hub in your Azure subscription using Python, you can use the [Azure IoT Hub management library for Python][azure-iot-mgmt-lib]. Read more [here][azure-iot-mgmt-lib-doc].

To manage all your Azure resources using Python, you can leverate the [Azure CLI v2][azure-cli-v2].

## Developing applications for Azure IoT
Visit [Azure IoT Dev Center][iot-dev-center] to learn more about developing applications for Azure IoT.

## How to clone the repository
The repository is using [GitHub Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) for its dependencies. In order to automatically clone these submodules, you need to use the --recursive option as described here:

```
git clone --recursive https://github.com/Azure/azure-iot-sdk-python.git 
```

If you have downloaded the zip instead of cloning the repository, you will need to run the following command to restore submodules:
```
git submodule update --init --recursive
```

## How to use the Azure IoT SDKs for Python
Devices and data sources in an IoT solution can range from a simple network-connected sensor to a powerful, standalone computing device. Devices may have limited processing capability, memory, communication bandwidth, and communication protocol support. The IoT device SDKs enable you to implement client applications for a wide variety of devices.
* **Using PyPI package on Windows (coming soon for Linux)**: the simplest way to use the Azure IoT SDK for Python to develop device apps on Windows is to leverage the PyPI package which you can install following these [instructions][PyPI-install-instructions]
* **Building the libraries and working with the SDK code**: follow [these instructions][devbox-setup].

## Samples
This repository contains various Python sample applications that illustrate how to use the Microsoft Azure IoT SDKs for Python.
* [Samples showing how to use the Azure IoT Hub device client][device-samples]
* [Samples showing how to use the Azure IoT Hub service client][service-samples]

## Contribution, feedback and issues
If you encounter any bugs, have suggestions for new features or if you would like to become an active contributor to this project please follow the instructions provided in the [contribution guidelines](.github/CONTRIBUTING.md).

## Support
If you are having issues using one of the packages or using the Azure IoT Hub service that go beyond simple bug fixes or help requests that would be dealt within the [issues section](https://github.com/Azure/azure-iot-sdks/issues) of this project, the Microsoft Customer Support team will try and help out on a best effort basis.
To engage Microsoft support, you can create a support ticket directly from the [Azure portal](https://ms.portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade).
Escalated support requests for Azure IoT Hub SDKs development questions will only be available Monday thru Friday during normal coverage hours of 6 a.m. to 6 p.m. PST.
Here is what you can expect Microsoft Support to be able to help with:
* **Client SDKs issues**: If you are trying to compile and run the libraries on a supported platform, the Support team will be able to assist with troubleshooting or questions related to compiler issues and communications to and from the IoT Hub.  They will also try to assist with questions related to porting to an unsupported platform, but will be limited in how much assistance can be provided.  The team will be limited with trouble-shooting the hardware device itself or drivers and or specific properties on that device. 
* **IoT Hub / Connectivity Issues**: Communication from the device client to the Azure IoT Hub service and communication from the Azure IoT Hub service to the client.  Or any other issues specifically related to the Azure IoT Hub.
* **Portal Issues**: Issues related to the portal, that includes access, security, dashboard, devices, Alarms, Usage, Settings and Actions.
* **REST/API Issues**: Using the IoT Hub REST/APIs that are documented in the [documentation]( https://msdn.microsoft.com/library/mt548492.aspx).

## Read more
* [Azure IoT Hub documentation][iot-hub-documentation]

## Long Term Support branches

The project is using LTS branches to allow users that do not need the latest and greatest features to be shielded from unwanted changes.

An LTS branch will be created every 6 months. The lifetime of an LTS branch is currently 1 year.
LTS branches receive all bug fixes that fall in one of these categories:

- security bugfixes
- critical bugfixes (crashes, memory leaks, etc.)

No new features or improvements will be picked up on LTS branches.

LTS branches are named lts_*mm*_*yyyy*, where *mm* and *yyyy* are the month and year when the branch was created. An example of such a branch is *lts_03_2017*.

![](./lts_branches.png)

---
This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

[iot-dev-center]: http://azure.com/iotdev
[iot-hub-documentation]: https://docs.microsoft.com/en-us/azure/iot-hub/
[azure-iot-sdks]: http://github.com/azure/azure-iot-sdks
[PyPI-install-instructions]: doc/python-devbox-setup.md#windows-wheels
[devbox-setup]: doc/python-devbox-setup.md
[device-samples]: device/samples/
[service-samples]: service/samples/
[azure-iot-mgmt-lib]: https://pypi.python.org/pypi/azure-mgmt-iothub
[azure-iot-mgmt-lib-doc]: http://azure-sdk-for-python.readthedocs.io/en/latest/sample_azure-mgmt-iothub.html
[azure-cli-v2]: https://github.com/Azure/azure-cli
