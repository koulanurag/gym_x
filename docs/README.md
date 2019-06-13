# Gold Rush Environments
GoldRush is an environment with a single agent that needs to collect gold at every time-step to survive and the objective is to maximize the survival time.
The underlying states of the environment are defined by ```M=4``` modes of operation.

* <b>Observation Space:</b>
    * <i>o<sub>t</sub> ɛ { o<sub>1</sub> ... o<sub>4</sub> }</i>
    * <i>o<sub>*</sub> => Transaction is valid for all possible observations</i>
* <b>Minimal State Machine:</b>
    * <b>GoldRushRead-v0</b>
        * requires attention to current observation only. (No Memory required)
        * States are denoted by <i>S<sub>(action)</sub></i>

        <p align="center">
            <img src="./images/1.png" width="600"/>
        </p>

    * <b>GoldRushBlind-v0</b>
        * Only Memory required (Observations are irrelevant)
        * States are denoted by <i>S<sub>( action) (clock-id)</sub></i>

        <p align="center">
            <img src="./images/2.png" width="600"/>
        </p>

    * <b>GoldRushSneak-v0</b>
        * requires attention to both memory and observations
        * States are denoted by <i>S<sub>( action) (clock-id)</sub></i>
        <p align="center">
            <img src="./images/3.png" width="600" height="450"/>
        </p>
   
# Tomita Grammar

|#|Name|Description|
|---|---------|-----------|
|1.|TomitaA-v0|1\*|
|2.|TomitaB-v0|(10)\*|
|3.|TomitaC-v0|An odd number of consecutive 1s is always followed by an even number of consecutive 0s|
|4.|TomitaD-v0|any string not containing "000" as a substring|
|5.|TomitaE-v0| even number of 0's and even number of 1s|
|6.|TomitaF-v0|the difference between number of 1s and number of 0s is a multiple of 3|
|7.|TomitaG-v0| 0\*1\*0\*1\*|





