# pacemaker_3x03_27

Group #: 27
Group members:  Eddy Su             400263717
                Daniel Young        400304153
                Paul Shenoda        400312110
                Abdul Nasir Noori   400325387
                Jaideep Pannu       400114712
                
The purpose of this project is to create a pacemaker device using a custom developed PCB. 
The project is split into two sections: Device Control Monitor (DCM) and Simulink teams. 
The DCM team creates a functional UI that is capable of controlling the pacemarker by Serial Communication to the Pacemarker board.
The Simulink team creates a model of the packmakers that is capable of taking inputs from the DCM and adpats the pacemaker behaviour accordingly. 

Supported pace modes include: AOO, VOO, AAI, VVI, AOOR, VOOR, AAIR, VVIR. 
Rate adaptive pacing is enabled to support AAIR and VVIR modes. 
Serial Communication is setup between Simulink and DCM to establish mannual control
