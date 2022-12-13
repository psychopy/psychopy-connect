# psychopy-connect

Extension package for adding support to PsychoPy for connectivity i.e. serial and parallel ports.

## Supported Devices

Installing this package alongside PsychoPy will enable support for the following devices:

* Generic serial and parallel ports
* [USB2TTL8](http://labhackers.com/usb2ttl8.html) USB TTL Interface
* Various U3 compatible [LabJack](https://labjack.com/) devices
    
## Installing

Install this package with the following shell command:: 

    pip install psychopy-connect

You may also use PsychoPy's builtin package manager to install this package.

## Usage

Once the package is installed, PsychoPy will automatically load it when started and make objects available within the
following namespaces:

* `psychopy.hardware.serialdevice`
* `psychopy.parallel`

This also adds the following components to Builder:

* Serial Out
* Parallel Out