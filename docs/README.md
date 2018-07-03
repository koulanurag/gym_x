# Gold Rush Environments
GoldRush is an environment with a single agent that needs to collect gold at every time-step to survive and the objective is to maximize the survival time.
The underlying states of the environment are defined by ```M=4``` modes of operation.

* <b>Observation Space:</b>
    * <i>o<sub>t</sub> ɛ { o<sub>1</sub> ... o<sub>4</sub> }</i>
    * <i>o<sub>*</sub> => Transaction is valid for all possible observations</i>
* <b>Minimal State Machine:</b> States are denoted by <i>S<sub>( action) (clock-id)</sub></i>

    * GoldRushRead-v0

       ![images/1.png](images/1.png) <!-- .element style=" width: 60%; height: 60%; display: block; margin: auto; " -->

    * GoldRushBlind-v0

        ![images/2.png](images/2.png) <!-- .element style=" width: 60%; height: 60%; display: block; margin: auto; " -->

    * GoldRushSneak-v0

        ![images/3.png](images/3.png) <!-- .element style=" width: 60%; height: 60%; display: block; margin: auto; " -->