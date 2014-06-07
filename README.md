# Raspberry Pi Door Opener

This is the software and hardware needed to build an almost-open door.

The only exceptions are the keylock and the RFID readers, wich we're
not provided.

Any keylock working with a pulse of anything that your relay can move 
would work, anyway.

Also, for the RFID readers you'd need a HID RFID device, that is, a
rfid device that identifies itself as a HID and puts the key id on.

Some people would say that's dangerous, or insecure, but the reality
is that any RFID chip is dangerous, they're crackable in a few hours
so anyone can dupe it.

On the other hand, to duplicate de 0-sector of a RFID card, you need
special (and hard to get) cards, or a 300€ RFID card emulator.

A normal RFID reader writer for 40€ can break the security of anything
that is not using the 0-sector id for its auth.

# Hardware

You'll need:

- 2 * RFID readers able to work as HID devices
- 1 * Raspberry PI with raspian
- 1 * Electronic lock
- A relay board:
   - 5v relay
   - 1 Diode
   - 1 PNP Transistor
   - 1k resistor

Follow the schematics in hardware/ folder, but it's a satndard relay board.

# Installation

First of all, note that the gpio library for python needs you to be able to
access to /dev/mem, wich means you'll need to execute it as root.
As this is not safe at all, I recommend adding a sudo exception to nopasswd
open_door and simpledod

Originally the [simpledo](https://github.com/XayOn/simpledo) project included both the door opener and the web interface. Now, the software is divided in two parts:

- [Erpil](https://github.com/tnarik/erpil) : The management system.
- [Raspido](https://github.com/tnarik/raspido) : The main daemon, listens to cards and opens the door if the card is allowed.

The startup daemon has a few requisites, first of all configure your sudoers so everyone can open the door.

Now, add a user for the door opener (for example, `dooropener`)

    adduser dooropener

Now, put the `confs/bashrc` into `~dooropener/.bashrc`
    
    cp confs/bashrc ~dooropener/.bashrc

And configure your inittab (dangerous, be careful!) to have tty1 autologin as dooropener user.

It should en something like this:

    1:2345:respawn:/sbin/getty -a dooropener 38400 tty1

And you're ready to go!
Just remember to buy compatible cards!
