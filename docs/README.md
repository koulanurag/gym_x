# Gold Rush Environments
GoldRush is an environment with a single agent that needs to collect gold at every time-step to survive and the objective is to maximize the survival time.
The underlying states of the environment are defined by ```M=4``` modes of operation.

* <b>Observation Space:</b>
    * <i>o<sub>t</sub> ɛ { o<sub>1</sub> ... o<sub>4</sub> }</i>
    * <i>o<sub>*</sub> => Transaction is valid for all possible observations</i>
* <b>Minimal State Machine:</b>
    * GoldRushRead-v0
    <img src="images/1.png" style=" width: 60%; height: 60%; display: block; margin: auto; ">

    * GoldRushBlind-v0
    <img src="images/2.png" style=" width: 60%; height: 60%; display: block; margin: auto; ">

    * GoldRushSneak-v0
    <img src="images/3.png" style=" width: 60%; height: 60%; display: block; margin: auto; ">