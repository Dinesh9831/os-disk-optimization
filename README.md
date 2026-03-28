# Disk Scheduling Simulator

## Overview

This project is a Disk Scheduling Algorithm Simulator developed using Python and Flask. It provides an interactive platform to simulate and analyze various disk scheduling algorithms used in Operating Systems.

The application allows users to input disk requests, initial head position, disk size, and select a scheduling algorithm. Based on the input, the system computes total seek time, average seek time, seek sequence, and performs starvation analysis for specific algorithms.

## Features

- Supports multiple disk scheduling algorithms:
  - FCFS (First Come First Serve)
  - SSTF (Shortest Seek Time First)
  - SCAN (Elevator Algorithm)
  - CSCAN (Circular SCAN)
  - LOOK
  - CLOOK

- Computes:
  - Total seek time
  - Average seek time
  - Seek sequence

- Starvation analysis:
  - Implemented for SSTF algorithm
  - Identifies delayed requests and evaluates starvation risk

- Web-based interface using Flask
- Supports both browser-based UI and JSON API responses

## Algorithms Description

FCFS processes disk requests in the order they arrive. It is simple but not optimized for seek time.

SSTF selects the request closest to the current head position. It reduces seek time but may cause starvation for distant requests.

SCAN moves the disk head in one direction servicing requests and reverses at the disk boundary.

CSCAN moves the head in one direction only and jumps back to the beginning after reaching the end.

LOOK is similar to SCAN but stops at the last request instead of going to the disk boundary.

CLOOK is the circular version of LOOK and jumps back to the lowest request after reaching the highest.

## Starvation Analysis

Starvation analysis is implemented for the SSTF algorithm. It detects whether certain requests are delayed excessively compared to others.

The output includes:
- Starvation risk level (High or Low)
- List of starved requests

## Input Parameters

- Requests: Comma-separated disk requests (example: 98,183,37,122)
- Head Position: Initial position of disk head
- Disk Size: Maximum range of the disk
- Algorithm: Selected disk scheduling algorithm
- Direction: Required for SCAN and LOOK (up or down)

## How to Run

1. Install Flask:
   pip install flask

2. Run the application:
   python app.py

3. Open in browser:
   http://127.0.0.1:5000/

## API Support

The application also supports JSON responses.

To get JSON output, send a POST request with header:
Accept: application/json

Example response:
{
  "result": {
    "seek": 640,
    "avg_seek": 80.0,
    "sequence": [50, 82, 170],
    "starvation_risk": "Low",
    "starved_items": []
  }
}

## Core Logic

All disk scheduling algorithms are implemented in the backend logic. Seek time is calculated as the sum of absolute differences between consecutive head movements.

## Technologies Used

- Python
- Flask
- HTML
- CSS

## Learning Outcome

This project demonstrates practical understanding of disk scheduling algorithms, their performance trade-offs, and real-world simulation of Operating System concepts. It also showcases backend and frontend integration using Flask.

## Future Enhancements

- Graphical visualization of disk head movement
- Comparative analysis of algorithms
- Enhanced starvation detection techniques
- Improved user interface

## Author

Developed as part of an Operating Systems academic project.
